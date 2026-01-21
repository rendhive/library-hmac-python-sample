import hmac
import hashlib

def generate_token(user_id):
    secret_key = "secret_key_here"
    token = hmac.new(secret_key.encode(), user_id.encode(), hashlib.sha256).hexdigest()
    return token

user_token = generate_token("user123")
print(f"User Token: {user_token}")
# Fungsi: Menghasilkan token otentikasi HMAC untuk pengguna.
# Kondisi: Ketika Anda perlu memberikan token yang aman untuk sesi pengguna.