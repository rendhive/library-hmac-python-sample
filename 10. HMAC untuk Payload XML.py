import hmac
import hashlib

def hmac_for_xml(key, xml_payload):
    return hmac.new(key.encode(), xml_payload.encode(), hashlib.sha256).hexdigest()

xml_payload = "<note><to>User</to><from>Service</from></note>"
hmac_value = hmac_for_xml("xml_key", xml_payload)
print(f"HMAC for XML Payload: {hmac_value}")
# Fungsi: Menghasilkan HMAC untuk payload XML.
# Kondisi: Ketika Anda perlu memverifikasi integritas XML yang dikirimkan.