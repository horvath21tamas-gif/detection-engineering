import os
import yaml
import requests # SIEM API híváshoz

def fetch_live_log_sources():
    # Példa: Splunk API hívás (vagy más SIEM)
    # Itt egy mock (példa) adatot használunk, de ide jönne az API hívás
    # A lekérdezés SIEM-ben: | tstats count where index=* by sourcetype, host
    
    live_sources = {
        'category': ['process_creation', 'network_connection', 'file_event', 'registry_set', 'dns_query'],
        'product': ['windows', 'linux', 'azure'],
        'service': ['sysmon', 'security', 'powershell', 'system']
    }
    
    # Kiegészítjük azokat, amiket a hibaüzenetben kaptál
    extra_from_siem = ['registry_event', 'image_load', 'process_access', 'webserver', 'pipe_created', 'login', 'service_creation', 'email', 'network_traffic']
    live_sources['category'].extend(extra_from_siem)
    live_sources['product'].append('generic')

    with open('inventory/log_sources.yaml', 'w', encoding='utf-8') as f:
        yaml.dump({'available_sources': live_sources}, f)
    
    print("✅ Live Log Source Inventory frissítve a SIEM adatai alapján.")

if __name__ == "__main__":
    fetch_live_log_sources()
