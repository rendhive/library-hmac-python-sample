import hmac
import hashlib

def hmac_with_different_messages(key):
    messages = ["Hello", "World", "HMAC"]
    hmac_results = {msg: hmac.new(key.encode(), msg.encode(), hashlib.sha1).hexdigest() for msg in messages}
    return hmac_results

key = "my_secret_key"
hmac_results = hmac_with_different_messages(key)
for msg, hmac_value in hmac_results.items():
    print(f"HMAC for '{msg}': {hmac_value}")
# Fungsi: Menghasilkan HMAC untuk beberapa pesan.
# Kondisi: Ketika Anda ingin mengevaluasi hasil HMAC untuk berbagai pesan dengan kunci yang sama.