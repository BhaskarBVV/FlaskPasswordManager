import base64
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


class EncryptionHelper:

    SECRET_KEY = os.getenv("ENCRYPTION_SECRET_KEY")
    print(SECRET_KEY)

    if not SECRET_KEY:
        raise KeyError("Could not find the secret key")

    SECRET_KEY = bytes.fromhex(SECRET_KEY)

    def encrypt_data(data: str) -> str:
        iv = os.urandom(16)  # Generate a random initialization vector (IV)
        cipher = Cipher(
            algorithms.AES(EncryptionHelper.SECRET_KEY),
            modes.CBC(iv),
            backend=default_backend(),
        )
        encryptor = cipher.encryptor()

        # Pad the data to be multiple of block size (AES block size is 16 bytes)
        pad_length = 16 - (len(data) % 16)
        padded_data = data + chr(pad_length) * pad_length
        encrypted_data = (
            encryptor.update(padded_data.encode("utf-8")) + encryptor.finalize()
        )

        # Return the base64-encoded encrypted data along with the IV for decryption
        return base64.b64encode(iv + encrypted_data).decode("utf-8")

    # Helper function to decrypt data
    def decrypt_data(encrypted_data: str) -> str:
        encrypted_data_bytes = base64.b64decode(encrypted_data)
        iv = encrypted_data_bytes[:16]  # Extract the IV from the beginning
        encrypted_data_bytes = encrypted_data_bytes[
            16:
        ]  # Remaining bytes are the encrypted data

        cipher = Cipher(
            algorithms.AES(EncryptionHelper.SECRET_KEY),
            modes.CBC(iv),
            backend=default_backend(),
        )
        decryptor = cipher.decryptor()

        decrypted_data = decryptor.update(encrypted_data_bytes) + decryptor.finalize()

        # Remove padding from decrypted data
        pad_length = ord(decrypted_data[-1])
        return decrypted_data[:-pad_length].decode("utf-8")
