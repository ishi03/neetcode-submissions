class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        # "HelloWorld"
        # "5#Hello5#World"
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # we first need the len of string to extract
            n = ""
            while s[i] != "#":
                n += s[i]
                i += 1
            # now we are at hash#
            n = int(n)
            i += 1 # now i am at start of the word
            res.append(s[i: i+n])
            i += n
        return res
