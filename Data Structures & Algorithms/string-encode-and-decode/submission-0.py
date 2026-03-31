class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = []
        for s in strs:
            str_ln = len(s)
            encoding.append(f"{str_ln}#{s}")
        return "".join(encoding)

    def decode(self, s: str) -> List[str]:
        decoding = []
        i = 0
        j = 0
        print(s)
        while j < len(s):
            i = j
            while s[j] != "#":
                j += 1
            str_len = int(s[i:j])
            
            str_start = j+1
            str_end = str_start + str_len 
            decoding.append(s[str_start:str_end])
            j = str_end 
            # break
            j = str_end
        
        return decoding