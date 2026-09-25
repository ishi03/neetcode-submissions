class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash = {}
        for x in s:
            hash[x] = hash.get(x, 0) + 1
        for x in t:
            if x not in hash:
                return False
            hash[x] -= 1
            if hash[x] == 0:
                del hash[x]
        return len(hash) == 0