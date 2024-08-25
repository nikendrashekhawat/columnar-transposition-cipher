class TranspositionCipher(object): 
    
    def __init__(self, key):
        if isinstance(key, str):
            self.key = key
            self.key_length = len(key)
        if isinstance(key, int):
            self.key = key
     
    @staticmethod       
    def get_columns(self) -> list:
        unique_chars = []
        KEY_UPPER = self.key.upper()
        for i, c in enumerate(KEY_UPPER):
            unique_chars.append(c + str(i))
        return unique_chars
        
        

if __name__ == "__main__":
    pass