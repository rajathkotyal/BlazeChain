from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from Crypto.PublicKey import RSA


with open('keyB.pem','rb') as key_file :
    private_key = serialization.load_pem_private_key(
                    key_file.read(),
                    password = None,
                    backend = default_backend()
    )

publicKey_B = private_key.public_key()
print(publicKey_B)
message = b"what up hoe?"
ciphertext = publicKey_B.encrypt(
    message,
    padding.OAEP(
        mgf = padding.MGF1(algorithm = hashes.SHA256()),
        algorithm = hashes.SHA256(),
        label = None
    )
)
# import rsa

# ciphertext = rsa.encrypt(message.encode(), publicKey_B)

transaction = {
   "sender" : "23b29de5b670fb99193246dffd09b519df26a8064b22cc49a4bcd773b937941a",
   "receiver" : "d36ec61a9d0f22119644b7ae0474f39ac6842e6f22899ea94095083840cf6b12",
   "message" : ciphertext
}

print(transaction)
