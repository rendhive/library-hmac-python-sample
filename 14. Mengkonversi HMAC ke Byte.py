import hmac
import hashlib

def hmac_in_bytes(key, message):
    return hmac.new(key.encode(), message.encode(), hashlib.sha256).digest()

key = "key_in_bytes"
message = "Hello Byte World"
hmac_bytes = hmac_in_bytes(key, message)
print(f"HMAC in bytes: {hmac_bytes}")
# Fungsi: Menghasilkan HMAC dalam format byte.
# Kondisi: Ketika Anda membutuhkan hasil dalam bentuk byte untuk penggunaan lebih lanjut.