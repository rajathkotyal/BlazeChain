from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from flask import jsonify
import base64


with open("/Users/rajath/Documents/MainChain/publicKeys/public_key5002.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )

message = b'yo babydoll'


enc = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
# from nacl.encoding import Base64Encoder
# print(encrypted.encode(Base64Encoder).decode())

#sample_string_bytes = sample_string.encode("ascii")

encrypted = base64.b64encode(enc)
#base64_string = base64_bytes.decode("ascii")
decrypted = base64.b64decode(encrypted)


print(f"Encoded string: {decrypted}")


transaction = {
   "sender" : "23b29de5b670fb99193246dffd09b519df26a8064b22cc49a4bcd773b937941a",
   "receiver" : "d36ec61a9d0f22119644b7ae0474f39ac6842e6f22899ea94095083840cf6b12",
   "message" : str(encrypted)
}

print(transaction)
