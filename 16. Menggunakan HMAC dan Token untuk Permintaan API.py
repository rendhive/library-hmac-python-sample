import hmac
import hashlib
import time

def generate_api_request_signature(secret_key, api_key):
    timestamp = str(int(time.time()))
    message = f"{api_key}:{timestamp}"
    return hmac.new(secret_key.encode(), message.encode(), hashlib.sha256).hexdigest(), timestamp

api_key = "my_api_key"
secret_key = "my_secret_key"
signature, timestamp = generate_api_request_signature(secret_key, api_key)
print(f"API Signature: {signature}, Timestamp: {timestamp}")
# Fungsi: Menghasilkan signature untuk otentikasi permintaan API.
# Kondisi: Ketika Anda ingin memastikan bahwa permintaan aman dan tidak dapat dipalsukan.