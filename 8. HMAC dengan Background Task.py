import hmac
import hashlib
import threading

def hmac_thread(key, message):
    print(f"HMAC for Thread: {hmac.new(key.encode(), message.encode(), hashlib.sha256).hexdigest()}")

key = "thread_key"
messages = ["Thread 1", "Thread 2", "Thread 3"]
threads = []

for msg in messages:
    thread = threading.Thread(target=hmac_thread, args=(key, msg))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
# Fungsi: Menghasilkan HMAC di latar belakang menggunakan threading.
# Kondisi: Ketika Anda ingin menghitung HMAC dengan beberapa thread secara bersamaan.