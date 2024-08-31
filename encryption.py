from TranspositionCipher import TranspositionCipher

class Encryption(TranspositionCipher):
    
    def __init__(self, key):
        super().__init__(key)
        
    def encrypt(self, message: str) -> str:
        message_encrypted: str = ""
        message_length: int = len(message)
        
        columns = TranspositionCipher.get_columns(self)
        message_dict: dict[str, str] = {}
        
        for i in range(self.key_length):
            temp: str= ""
            j = i
            while j < message_length:
                temp += message[j]
                j += self.key_length
                
            message_dict.update({columns[i] : temp})

        sorted_dict: dict[str, str] = dict(sorted(message_dict.items()))
        
        for _, value in sorted_dict.items():
            message_encrypted += value

        del temp, i, j, value, sorted_dict, message_dict, message, message_length 
        
        return message_encrypted
    
if __name__ == "__main__":
    key_str = input("Enter the Transposition Cipher key: ")
    en = Encryption(key_str)
    message = input("Enter your message: ")
    length = len(message)
    print("Your encrypted message is:")
    print("***" * (length//2))
    print(en.encrypt_message(message))
    print("***" * (length//2))
