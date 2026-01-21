import hmac
import hashlib

def get_user_hmac():
    key = input("Masukkan kunci: ")
    message = input("Masukkan pesan: ")
    return hmac.new(key.encode(), message.encode(), hashlib.sha256).hexdigest()

hmac_value = get_user_hmac()
print(f"HMAC dari input pengguna: {hmac_value}")
# Fungsi: Menghasilkan HMAC berdasarkan input dari pengguna.
# Kondisi: Ketika Anda ingin memproses dinamika input pengguna untuk keamanan.