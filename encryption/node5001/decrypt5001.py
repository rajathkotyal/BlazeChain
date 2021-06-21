from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

with open("private_key5001.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )
