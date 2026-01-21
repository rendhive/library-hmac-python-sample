import hmac
import hashlib

def long_message_hmac(key, long_message):
    return hmac.new(key.encode(), long_message.encode(), hashlib.sha256).hexdigest()

long_message = "A long message that needs protection with HMAC" * 100  # Duplikasi untuk panjang
hmac_value = long_message_hmac("long_key", long_message)
print(f"HMAC for Long Message: {hmac_value}")
# Fungsi: Menghasilkan HMAC untuk pesan panjang.
# Kondisi: Ketika Anda perlu memproses pesan yang sangat besar dan ingin menjaga integritasnya.