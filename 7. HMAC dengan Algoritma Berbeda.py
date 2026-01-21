import hmac
import hashlib

def hmac_with_algorithm(key, message, algorithm):
    if algorithm == 'sha256':
        h = hmac.new(key.encode(), message.encode(), hashlib.sha256)
    elif algorithm == 'sha1':
        h = hmac.new(key.encode(), message.encode(), hashlib.sha1)
    else:
        raise ValueError("Unsupported algorithm")
    return h.hexdigest()

key = "another_key"
message = "Using different algorithm"
hmac_value_sha1 = hmac_with_algorithm(key, message, 'sha1')
print(f"HMAC SHA-1: {hmac_value_sha1}")
# Fungsi: Menghasilkan HMAC menggunakan algoritma yang ditentukan.
# Kondisi: Ketika Anda ingin fleksibilitas dalam memilih algoritma hashing.