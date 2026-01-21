import hmac
import hashlib

def store_data_with_hmac(key, data):
    hmac_value = hmac.new(key.encode(), data.encode(), hashlib.sha256).hexdigest()
    # Simulasi penyimpanan
    stored_data = {'data': data, 'hmac': hmac_value}
    return stored_data

data = "Data to be stored securely"
result = store_data_with_hmac("storage_key", data)
print(f"Stored Data: {result}")
# Fungsi: Menyimpan data dengan HMAC untuk keamanan.
# Kondisi: Ketika Anda ingin menjaga keamanan data yang disimpan.