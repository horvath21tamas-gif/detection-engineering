.PHONY: help install check test validate wazuh bundle siem lint all clean

PY ?= python3

help:  ## list targets
	@grep -E '^[a-z-]+:.*##' $(MAKEFILE_LIST) | awk -F':.*## ' '{printf "  %-10s %s\n", $$1, $$2}'

install:  ## install the toolkit + dev tools into the current environment
	$(PY) -m pip install -e ".[dev,siem]"

validate:  ## validate Sigma rules (read-only)
	dectools-validate rules/sigma

test:  ## unit, differential and gate tests
	$(PY) -m pytest

lint:  ## ruff
	ruff check src tests tools/convert_siem.py

wazuh:  ## compile Sigma -> Wazuh rules into build/wazuh
	dectools-wazuh build --check-registry --max-unsupported 80

bundle: wazuh  ## package build/wazuh for wazuh-deploy-gate
	dectools-wazuh bundle --git-sha "$$(git rev-parse --short HEAD)"

siem:  ## Splunk + Elastic queries into build/siem
	$(PY) tools/convert_siem.py --max-failures 1

check: validate lint test wazuh  ## everything CI runs before merging

clean:
	rm -rf build .pytest_cache .ruff_cache
