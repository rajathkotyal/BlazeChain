from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import ec
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
# private_key = ec.generate_private_key(
# ec.SECP384R1(),
# default_backend()
# )
public_key = private_key.public_key()

from cryptography.hazmat.primitives import serialization

pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

with open('private_key5001.pem', 'wb') as f:
    f.write(pem)

from cryptography.hazmat.primitives import serialization

pubPem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

with open('public_key5001.pem', 'wb') as f:
    f.write(pubPem)
