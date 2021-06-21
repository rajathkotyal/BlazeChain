from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
import sys

with open('keyB.pem','rb') as key_file :
    private_key = serialization.load_pem_private_key(
                    key_file.read(),
                    password = None,
                    backend = default_backend()
    )


ciphertext = sys.argv[0]

plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
            mgf = padding.MGF1(algorithm = hashes.SHA256()),
            algorithm = hashes.SHA256(),
            label = None
    )
)

print(plaintext)
