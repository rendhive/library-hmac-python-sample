import hmac
import hashlib

def test_hmac(key, message, expected_hmac):
    calculated_hmac = hmac.new(key.encode(), message.encode(), hashlib.sha256).hexdigest()
    return hmac.compare_digest(calculated_hmac, expected_hmac)

key = "test_key"
message = "Test Message"
expected_hmac = hmac.new(key.encode(), message.encode(), hashlib.sha256).hexdigest()

is_valid = test_hmac(key, message, expected_hmac)
print(f"HMAC valid: {is_valid}")
# Fungsi: Menggunakan HMAC untuk memverifikasi keaslian pesan di uji coba.
# Kondisi: Ketika Anda ingin memastikan bahwa pesan tetap utuh setelah pengujian.