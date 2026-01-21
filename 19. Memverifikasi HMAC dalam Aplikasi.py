import hmac
import hashlib

def verify_application_data(key, data, hmac_value):
    calculated_hmac = hmac.new(key.encode(), data.encode(), hashlib.sha256).hexdigest()
    return hmac.compare_digest(calculated_hmac, hmac_value)

key = "app_secret_key"
data = "Application specific data"
expected_hmac = hmac.new(key.encode(), data.encode(), hashlib.sha256).hexdigest()

is_valid = verify_application_data(key, data, expected_hmac)
print(f"HMAC is valid for application data: {is_valid}")
# Fungsi: Memvalidasi HMAC dalam konteks aplikasi.
# Kondisi: Ketika Anda perlu memastikan data aplikasi tetap tidak diubah.