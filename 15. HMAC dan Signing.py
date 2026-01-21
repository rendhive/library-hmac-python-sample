import hmac
import hashlib

def sign_message(key, message):
    return hmac.new(key.encode(), message.encode(), hashlib.sha256).hexdigest()

message = "Important message"
signature = sign_message("signing_key", message)
print(f"Signature: {signature}")
# Fungsi: Menghasilkan signature untuk pesan yang penting.
# Kondisi: Ketika Anda ingin menandatangani pesan untuk verifikasi.