from TranspositionCipher import TranspositionCipher

class Encryption(TranspositionCipher):
    
    def __init__(self, key):
        super().__init__(key)
    
    def encrypt_message(self, message) -> str:
        encrypt_message = ""
        message_length = len(message)
        for i in range(self.key):
            while i < message_length:
                encrypt_message += message[i]
                i += self.key
        return encrypt_message

if __name__ == "__main__":
    try:
        key_str = input("Enter the Transposition Cipher key: ")
        
        try:
            key = int(key_str)
        except ValueError:
            raise TypeError("unsupported type: key must be a integer")
        
        if key <= 0 :
            raise ValueError("unsupported key: must be a positive integer")
        else:
            en = Encryption(key)
            message = input("Enter your message: ")
            length = len(message)
            print("Your encrypted message is:")
            print("***" * (length//2))
            print(en.encrypt_message(message))
            print("***" * (length//2))
    except (TypeError, ValueError) as err:
        print(err)