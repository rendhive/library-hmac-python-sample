import hmac
import hashlib

def hmac_stream(key):
    h = hmac.new(key.encode(), digestmod=hashlib.sha256)
    while True:
        data = yield
        h.update(data.encode())
        yield h.hexdigest()

key = "stream_key"
hmac_gen = hmac_stream(key)
next(hmac_gen)  # Starting the generator

# Simulating streaming data
hmac_gen.send("First packet of data.")
print("Current HMAC:", hmac_gen.send("Second packet of data."))  # Yields HMAC
# Fungsi: Menghasilkan HMAC secara real-time dari aliran data.
# Kondisi: Ketika ingin memproses data saat streaming dan memverifikasi integritasnya pada saat yang sama.