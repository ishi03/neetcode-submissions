class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        res = 0
        while res not in seen and res != 1:
            seen.add(n)
            dig = n
            res = 0
            while dig > 0:
                res += (dig%10)**2
                dig = dig // 10
            # res += dig
            # if res in seen:
            #     return False
            # seen.add(res)
            n = res
        return res == 1