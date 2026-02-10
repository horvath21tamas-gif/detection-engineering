import yaml
import os
import json
import time
from googletrans import Translator

# --- KONFIGURÁCIÓ ---
LANGUAGES = ['hu', 'en', 'de'] 
CACHE_FILE = 'tools/translation_cache.json'
translator = Translator()

# --- CACHE BETÖLTÉSE ---
translation_cache = {}
if os.path.exists(CACHE_FILE):
    try:
        with open(CACHE_FILE, 'r', encoding='utf-8') as f:
            translation_cache = json.load(f)
        print(f"ℹ️ Gyorsítótár betöltve ({len(translation_cache)} elem).", flush=True)
    except Exception as e:
        print(f"⚠️ Cache betöltési hiba: {e}", flush=True)
        translation_cache = {}

def translate_text(text, target_lang):
    """Szöveg fordítása cache-eléssel és hibakezeléssel."""
    if not text or target_lang == 'en':
        return text
    
    cache_key = f"{target_lang}_{text}"
    
    if cache_key in translation_cache:
        return translation_cache[cache_key]

    try:
        # Rövid szünet a Google API miatt
        time.sleep(0.4) 
        translated = translator.translate(text, dest=target_lang).text
        translation_cache[cache_key] = translated
        # Kiírjuk, hogy lássuk a haladást
        print(f"  [API] Fordítás ({target_lang}): {text[:30]}...", flush=True)
        return translated
    except Exception as e:
        print(f"⚠️ Fordítási hiba ({target_lang}): {e}", flush=True)
        return text

def save_cache():
    """Fordítások mentése fájlba."""
    try:
        # Biztosítjuk, hogy a mappa létezik
        os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)
        with open(CACHE_FILE, 'w', encoding='utf-8') as f:
            json.dump(translation_cache, f, ensure_ascii=False, indent=4)
        print(f"💾 Gyorsítótár elmentve: {CACHE_FILE}", flush=True)
    except Exception as e:
        print(f"⚠️ Cache mentési hiba: {e}", flush=True)

def get_stars(score, lang):
    rating_text = ""
    if score >= 90: rating_text = "Kiváló"
    elif score >= 70: rating_text = "Jó"
    elif score >= 50: rating_text = "Közepes"
    else: rating_text = "Fejlesztendő"
    
    stars = "⭐⭐⭐⭐⭐" if score >= 90 else "⭐⭐⭐⭐" if score >= 70 else "⭐⭐⭐" if score >= 50 else "⭐⭐"
    return f"{stars} ({translate_text(rating_text, lang)})"

def get_lolbas_info(rule_data, lang):
    lolbas_links = []
    try:
        if os.path.exists('inventory/lolbas_map.json'):
            with open('inventory/lolbas_map.json', 'r') as f:
                lolbas_map = json.load(f)
            yaml_str = str(rule_data).lower()
            for proc, link in lolbas_map.items():
                if proc in yaml_str:
                    lolbas_links.append(f"[{proc.upper()}]({link})")
    except: pass
    
    if lolbas_links:
        label = translate_text("LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint", lang)
        return f"\n> ⚠️ **{label}:** {', '.join(lolbas_links)}\n"
    return ""

def get_estimated_volume(category, lang):
    volumes = {
        'process_creation': ('Magas', 'Erős szűrés javasolt (sok log)'),
        'network_connection': ('Kritikusan Magas', 'SIEM gyilkos kategória!'),
        'registry_event': ('Közepes', 'Mérsékelt zajszint'),
        'file_event': ('Magas', 'Tárolás-igényes'),
        'email': ('Alacsony', 'Jól monitorozható')
    }
    vol_raw, advice_raw = volumes.get(category, ('Ismeretlen', 'Nincs adat'))
    
    label = translate_text("Becsült zajszint", lang)
    vol = translate_text(vol_raw, lang)
    advice = translate_text(advice_raw, lang)
    return f"- **{label}:** {vol} ({advice})\n"

def get_playbook(category, level, lang):
    pb_label = translate_text("Response Playbook", lang)
    playbook = f"#### 🚨 {pb_label}\n"
    
    steps = []
    if category == 'process_creation':
        steps.append("Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.")
        steps.append("Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.")
    elif category == 'network_connection':
        steps.append("IP hírnév: Ellenőrizd a távoli IP címet hírnév-adatbázisokban.")
        steps.append("Forgalom elemzés: Vizsgáld meg a küldött adatmennyiséget.")
    else:
        steps.append("Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.")
    
    if level in ['high', 'critical']:
        steps.append("Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!")

    for i, step in enumerate(steps, 1):
        playbook += f"{i}. **{translate_text(step, lang)}**\n"
    
    return playbook

def generate_docs():
    sigma_path = 'rules/sigma'
    scores_path = 'rule_scores.json'
    scores = {}
    
    if os.path.exists(scores_path):
        with open(scores_path, 'r', encoding='utf-8') as f:
            scores = json.load(f)

    rules_data = []
    for root, _, files in os.walk(sigma_path):
        for file in sorted(files):
            if file.endswith(('.yaml', '.yml')):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    try:
                        d = yaml.safe_load(f)
                        if d: rules_data.append({'filename': file, 'data': d})
                    except: continue

    for lang in LANGUAGES:
        print(f"🌐 Wiki generálása ({lang.upper()})...", flush=True)
        
        main_title = translate_text("Detection Rule Knowledge Base", lang)
        toc_title = translate_text("Tartalomjegyzék", lang)
        
        wiki_content = f"# 🛡️ {main_title}\n\n"
        wiki_content += f"## 📖 {toc_title}\n"
        
        for item in rules_data:
            title = translate_text(item['data'].get('title', 'Névtelen szabály'), lang)
            anchor = title.lower().replace(' ', '-').replace('.', '').replace('/', '').replace(',', '')
            wiki_content += f"- [{title}](#{anchor})\n"

        for item in rules_data:
            file = item['filename']
            d = item['data']
            title = translate_text(d.get('title', 'Névtelen szabály'), lang)
            level = d.get('level', 'n/a')
            category = d.get('logsource', {}).get('category', 'unknown')
            
            wiki_content += f"\n---\n## {title}\n"
            wiki_content += f"- **ID:** `{file}`\n"
            wiki_content += f"- **{translate_text('Minőségi mutató', lang)}:** `{scores.get(file, 0)}/100` {get_stars(scores.get(file, 0), lang)}\n"
            
            crit_label = translate_text("Kritikusság", lang)
            wiki_content += f"- **{crit_label}:** {'🔴' if level == 'critical' else '🟠' if level == 'high' else '🟡'} ({level})\n"
            
            wiki_content += get_estimated_volume(category, lang)
            wiki_content += get_lolbas_info(d, lang)
            
            desc_label = translate_text("Leírás", lang)
            desc_val = translate_text(str(d.get('description', 'Nincs leírás')), lang)
            wiki_content += f"- **{desc_label}:** {desc_val}\n"
            
            wiki_content += "\n" + get_playbook(category, level, lang) + "\n"

        filename = f'DETECTION_WIKI_{lang.upper()}.md'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(wiki_content)
        print(f"✅ {filename} elkészült.", flush=True)

    save_cache()

if __name__ == "__main__":
    generate_docs()
