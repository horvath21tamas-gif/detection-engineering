import yaml
import os

def calculate_score(rule_data):
    score = 0
    # Alap metaadatok (30 pont)
    if rule_data.get('author'): score += 10
    if rule_data.get('description'): score += 10
    if rule_data.get('date'): score += 10
    
    # Szakmai tartalom (40 pont)
    tags = rule_data.get('tags', [])
    if any(tag.startswith('attack.t') for tag in tags): score += 20
    if rule_data.get('falsepositives') and rule_data.get('falsepositives') != ['Unknown']:
        score += 20
        
    # Szint (10 pont)
    if rule_data.get('level') in ['high', 'critical']: score += 10
    
    # Referenciák (20 pont)
    refs = rule_data.get('references', [])
    if refs:
        score += min(len(refs) * 10, 20)
        
    return score

def score_all_rules():
    sigma_path = 'rules/sigma'
    results = {}

    for root, _, files in os.walk(sigma_path):
        for file in files:
            if file.endswith(('.yaml', '.yml')):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    try:
                        data = yaml.safe_load(f)
                        if data:
                            results[file] = calculate_score(data)
                    except:
                        continue
    
    # Mentés egy JSON-be a Dashboard számára (UTF-8 támogatással)
    import json
    with open('rule_scores.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4, ensure_ascii=False)
    print(f"✅ {len(results)} szabály pontozva.")

if __name__ == "__main__":
    score_all_rules()
