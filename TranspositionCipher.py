class TranspositionCipher(object): 
    
    def __init__(self, key: str):
            self.key: str = key
            self.key_length: int = len(key)
     
    @staticmethod       
    def get_columns(self) -> list:
        unique_key_chars: list[str] = []
        KEY_UPPER = self.key.upper()
        for i, c in enumerate(KEY_UPPER):
            unique_key_chars.append(c + str(i))
        return unique_key_chars
        
        

if __name__ == "__main__":
    pass