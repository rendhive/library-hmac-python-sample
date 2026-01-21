import hmac
import hashlib
import os

def generate_secret_key():
    return os.urandom(32)  # Menghasilkan kunci acak 32 byte

key = generate_secret_key()
message = "Secure Message"
hmac_value = hmac.new(key, message.encode(), hashlib.sha256).hexdigest()
print(f"HMAC dengan kunci rahasia: {hmac_value}")
# Fungsi: Menghasilkan HMAC menggunakan kunci acak yang dihasilkan.
# Kondisi: Ketika Anda perlu menggunakan kunci yang aman untuk HMAC.