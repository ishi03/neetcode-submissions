class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashes = dict()
        for x in strs:
            k = [0] * 26
            for c in x:
                k[ord(c) - ord("a")] += 1
            k = tuple(k)
            if k not in hashes:
                hashes[k] = [x]
            else:
                hashes[k].append(x)
        res = []
        for k, v in hashes.items():
            res.append(v)
        return res