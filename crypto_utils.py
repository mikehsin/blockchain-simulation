from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization


def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key


def sign_transaction(private_key, transaction_data):
    """
    Signs the serialized transaction data with the given private key.
    
    Parameters:
    - private_key: The RSA private key for signing the transaction.
    - transaction_data: The serialized transaction data as a string.
    
    Returns:
    - The signature as a bytes object.
    """
    # Ensure the transaction data is a string. Encode it to bytes for signing.
    encoded_transaction_data = transaction_data.encode()

    # Sign the encoded transaction data using the private key and SHA-256 hashing.
    signature = private_key.sign(
        encoded_transaction_data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    
    return signature
    
def verify_signature(public_key, transaction_data, signature):
    """
    Verifies the signature against the transaction data using the public key.
    - public_key: The public key for verification.
    - transaction_data: The serialized transaction data as a string.
    - signature: The signature to verify.
    """
    # Ensure the transaction data is encoded for verification
    encoded_transaction_data = transaction_data.encode()
    
    try:
        public_key.verify(
            signature,
            encoded_transaction_data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        return False


