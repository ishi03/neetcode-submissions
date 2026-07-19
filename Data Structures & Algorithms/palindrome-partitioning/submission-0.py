class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []
        # explore each possible substring and check if palindrome
        def dfs(subset, i):
            if i >= len(s):
                # we are done w this branch
                res.append(subset.copy())
                return
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    subset.append(s[i: j+1])
                    dfs(subset, j+1) # this part is a palindrome. make parts henceforth n check
                    subset.pop() # I do not understnad this
        dfs([], 0)
        return res

    def isPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True