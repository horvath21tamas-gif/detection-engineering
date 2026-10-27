#!/usr/bin/env bash
# One-time setup of the deploy path on the Wazuh manager (run as root, on the manager).
#
#   sudo ./install.sh "ssh-ed25519 AAAA... ci-runner@lab" [allowed_source_ip]
#
# Creates the restricted user `wazuh-deploy`, installs wazuh-deploy-gate and the sudoers
# rule. The SSH key can ONLY run the gate (forced command): no shell, no port forwarding.
set -euo pipefail

PUBKEY="${1:?usage: install.sh \"<ssh public key line>\" [allowed_source_ip]}"
FROM="${2:-}"
DEPLOY_USER=wazuh-deploy
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

[[ $EUID -eq 0 ]] || { echo "run as root" >&2; exit 1; }
[[ "$PUBKEY" =~ ^ssh-(ed25519|rsa)[[:space:]] || "$PUBKEY" =~ ^ecdsa-sha2- ]] || { echo "not a public key line" >&2; exit 1; }
[[ "$PUBKEY" == *"PRIVATE"* ]] && { echo "that looks like a PRIVATE key - never paste those" >&2; exit 1; }
[[ -x /var/ossec/bin/wazuh-analysisd ]] || { echo "Wazuh manager not found in /var/ossec" >&2; exit 1; }

id "$DEPLOY_USER" &>/dev/null || useradd --system --create-home --shell /usr/sbin/nologin "$DEPLOY_USER"
install -m 0750 -o root -g root "$HERE/wazuh-deploy-gate" /usr/local/sbin/wazuh-deploy-gate
install -d -m 0750 -o root -g root /var/lib/wazuh-deploy /etc/wazuh-deploy

# sudo: exactly one command, no arguments
echo "$DEPLOY_USER ALL=(root) NOPASSWD: /usr/local/sbin/wazuh-deploy-gate" > /etc/sudoers.d/wazuh-deploy
chmod 0440 /etc/sudoers.d/wazuh-deploy
visudo -cf /etc/sudoers.d/wazuh-deploy >/dev/null

# SSH: forced command, optional source restriction
SSH_DIR="/home/$DEPLOY_USER/.ssh"
install -d -m 0700 -o "$DEPLOY_USER" -g "$DEPLOY_USER" "$SSH_DIR"
OPTS='command="sudo /usr/local/sbin/wazuh-deploy-gate",restrict'
[[ -n "$FROM" ]] && OPTS="from=\"$FROM\",$OPTS"
echo "$OPTS $PUBKEY" > "$SSH_DIR/authorized_keys"
chown "$DEPLOY_USER:$DEPLOY_USER" "$SSH_DIR/authorized_keys"
chmod 0600 "$SSH_DIR/authorized_keys"
# usermod needed because nologin shells refuse forced commands on some sshd setups
usermod --shell /bin/sh "$DEPLOY_USER"

if [[ ! -f /etc/wazuh-deploy/api.env ]]; then
  cat > /etc/wazuh-deploy/api.env <<'ENV'
# Wazuh API user used ONLY for `PUT /logtest`. Create a dedicated low-privilege user
# (read-only role plus logtest) in Security > Users and put its credentials here.
WAZUH_API_URL=https://127.0.0.1:55000
WAZUH_API_USER=CHANGE_ME
WAZUH_API_PASSWORD=CHANGE_ME
ENV
  chmod 0600 /etc/wazuh-deploy/api.env
  echo ">> edit /etc/wazuh-deploy/api.env (dedicated API user) before the first deployment"
fi

echo "installed. test from the runner:  printf 'status\n' | ssh $DEPLOY_USER@<manager>"
