import math
from TranspositionCipher import TranspositionCipher

class Decryption(TranspositionCipher):
    
    def __init__(self, key):
        super().__init__(key)
    
    def decrypt_message(self, message) -> str:
        decryption = ""
        message_length = len(message)
        columns = math.ceil(message_length/self.key)
        full_rows = message_length % self.key
        for i in range(columns):
            if i != (columns - 1):
                while i <= message_length:
                    if i >= columns * (full_rows + 1):
                        decryption += message[i-1]
                        i = i - 1
                    else:
                        decryption += message[i]
                    i += columns
            else:
                while i <= message_length and i < columns * full_rows:
                    decryption += message[i]
                    i += columns
        return decryption

if __name__ == "__main__":
    key_str = input("Enter the Transposition Cipher key: ")
    
    try:
        key = int(key_str)
    except ValueError:
        raise TypeError("unsupported type: key must be a integer")
        
    if key <= 0 :
        raise ValueError("unsupported key: must be a positive integer")
    else:
        de = Decryption(key)
        message = input("Enter your encrypted message: ")
        length = len(message)
        print("The message is:")
        print("***" * (length//2))
        print(de.decrypt_message(message))
        print("***" * (length//2))