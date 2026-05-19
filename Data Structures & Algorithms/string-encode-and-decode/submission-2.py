class Solution:

    def encode(self, strs: List[str]) -> str:
        #nword
        res = ""
        for word in strs:
            res += str(len(word))
            res += "#"
            res += word
        return res

    def decode(self, s: str) -> List[str]:
        "5#Hello5#World"
        res = []
        i, j = 0, 0
        while i < len(s):
            l = ""
            while s[i] != "#":
                l += s[i]
                i+=1
            l = int(l)
            i += 1
            res.append(s[i:i+l])
            i+=l
        return res
