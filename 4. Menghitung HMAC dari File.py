import hmac
import hashlib

def hmac_from_file(key, filename):
    h = hmac.new(key.encode(), digestmod=hashlib.sha256)
    with open(filename, 'rb') as f:
        while chunk := f.read(4096):
            h.update(chunk)
    return h.hexdigest()

# Ubah 'example.txt' ke nama file Anda.
hmac_value = hmac_from_file("my_secret_key", "example.txt")
print(f"HMAC dari file: {hmac_value}")
# Fungsi: Menghasilkan HMAC berdasarkan konten file.
# Kondisi: Ketika Anda perlu memastikan integritas file secara aman.