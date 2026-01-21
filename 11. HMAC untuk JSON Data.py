import hmac
import hashlib
import json

def hmac_for_json(key, data):
    json_data = json.dumps(data)
    return hmac.new(key.encode(), json_data.encode(), hashlib.sha256).hexdigest()

data = {"user": "JohnDoe", "action": "login"}
hmac_value = hmac_for_json("json_key", data)
print(f"HMAC for JSON: {hmac_value}")
# Fungsi: Menghasilkan HMAC untuk data JSON.
# Kondisi: Ketika Anda perlu menjamin keaslian dan integritas data JSON dalam komunikasi.