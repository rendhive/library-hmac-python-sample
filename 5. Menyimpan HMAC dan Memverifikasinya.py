import hmac
import hashlib

def create_hmac(key, message):
    return hmac.new(key.encode(), message.encode(), hashlib.sha256).hexdigest()

def verify_hmac(key, message, provided_hmac):
    calculated_hmac = create_hmac(key, message)
    return hmac.compare_digest(calculated_hmac, provided_hmac)

key = "secret_key"
msg = "Important message"
generated_hmac = create_hmac(key, msg)

is_valid = verify_hmac(key, msg, generated_hmac)
print(f"HMAC valid: {is_valid}")
# Fungsi: Menghitung HMAC untuk pesan dan memverifikasi keasliannya.
# Kondisi: Ketika Anda ingin memvalidasi apakah pesan tidak diubah.