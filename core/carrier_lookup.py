import json
import os

DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data/prefixes.json")

def load_prefixes():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def prefix_match(e164_number: str):
    prefixes = load_prefixes()
    
    for prefix in sorted(prefixes, key=lambda p: -len(p)):
        if e164_number.startswith(prefix):
            data = prefixes[prefix]
            local_part = e164_number[len(prefix):]

            # Carrier heuristic
            carrier_guess = None
            if len(local_part) >= 2:
                if local_part[:2] in data.get("carriers", {}):
                    carrier_guess = data["carriers"][local_part[:2]]
                elif local_part[0] in data.get("carriers", {}):
                    carrier_guess = data["carriers"][local_part[0]]

            return {
                "country": data.get("country"),
                "timezones": data.get("timezones"),
                "carrier_guess": carrier_guess,
                "local_part": local_part
            }

    return None
