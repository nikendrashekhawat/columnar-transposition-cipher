import math
from pprint import pprint
from TranspositionCipher import TranspositionCipher

class Decryption(TranspositionCipher):
    
    def __init__(self, key):
        super().__init__(key)
    
    def decrypt(self, message) -> str:
        message_decrypted = ""
        message_length = len(message)
        
        if isinstance(self.key, str):
            rows = TranspositionCipher.get_columns(self)
            sorted_rows = sorted(rows)
            ncols = math.ceil(message_length/self.key_length)
            sorted_key_dict = {}
            nlast = (ncols * self.key_length) - message_length
            last_rows = rows[-nlast:]
            message_key_dict = {}
            temp = 0
            
            for i in range(self.key_length):
                if sorted_rows[i] not in last_rows:
                    sorted_key_dict.update({sorted_rows[i]: message[temp: temp+ncols]})
                    temp = temp + ncols
                else:
                    sorted_key_dict.update({sorted_rows[i]: message[temp: temp+ncols-1]})
                    temp = temp + ncols - 1   
            
            for char in rows:
                message_key_dict.update({char: sorted_key_dict[char]})
            
            for i in range(ncols):
                for k, v in message_key_dict.items():
                    if i < ncols-1:
                        message_decrypted += v[i]
                    else:
                        if k not in last_rows:
                            message_decrypted += v[i]              
            del temp, i, char, k, v, ncols, sorted_key_dict, message_key_dict
            del message, message_length, rows, sorted_rows, nlast, last_rows
        
        if isinstance(self.key, int):
            columns = math.ceil(message_length/self.key)
            full_rows = message_length % self.key
            
            for i in range(columns):
                if i != (columns - 1):
                    while i <= message_length:
                        if i >= columns * (full_rows + 1):
                            message_decrypted += message[i-1]
                        else:
                            message_decrypted += message[i]
                        i += columns
                else:
                    while i <= message_length and i < columns * full_rows:
                        message_decrypted += message[i]
                        i += columns
            del columns, full_rows, i, message, message_length

        return message_decrypted


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