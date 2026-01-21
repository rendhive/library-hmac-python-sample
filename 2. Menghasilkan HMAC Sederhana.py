import hmac
import hashlib

def simple_hmac(key, message):
    return hmac.new(key.encode(), message.encode(), hashlib.sha256).hexdigest()

key = "my_secret_key"
message = "Hello, World!"
hmac_value = simple_hmac(key, message)
print(f"HMAC: {hmac_value}")
# Fungsi: Menghasilkan HMAC dari kunci dan pesan yang diberikan.
# Kondisi: Ketika Anda ingin memverifikasi integritas dan keaslian pesan.