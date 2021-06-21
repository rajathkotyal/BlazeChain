from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
import base64
import sys
with open("private_key5003.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


baseStr = b'1T2255gvtBv+LQBMdEd/EWgeFv11VKc9Bu77xexNKXSo0DXFaNzfC/V+qq7lZ8jh6Qbu2NJJSSV/BK+znsQax9+cXkTTF66boyLQGQnyzcFCMcMEr6wXetBpZnvIyQg2t70BUATN5UZAGaqGtGdIIoILeYk3v/h2kx0W60afs9QBOQzQ5le4feBzp/eSbF0z9Ql/4PbN34mxTMoDstIpGnwn7NWwqOtkUxGAvYEkTQ4vg0jDgCWyx67o8t99oStl4V4USlkK347dJyPigOoAeEtFCrbvGNUOoIGNtAByf5J3QfTlZdLVJQhSrGfVuBSVdroDWkjfLqi5+3wjILEAOA=='
encrypted = base64.b64decode(baseStr)

original_message = private_key.decrypt(
    encrypted,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print(original_message)
