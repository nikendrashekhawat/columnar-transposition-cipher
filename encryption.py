from TranspositionCipher import TranspositionCipher

class Encryption(TranspositionCipher):
    
    def __init__(self, key):
        super().__init__(key)
        
    def encrypt(self, message: str) -> str:
        message_encrypted: str = ""
        message_length: int = len(message)
        
        if isinstance(self.key, str):
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
            
        if isinstance(self.key, int):
            for i in range(self.key):
                while i < message_length:
                    message_encrypted += message[i]
                    i += self.key
            del i, message, message_length
        
        return message_encrypted
    
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