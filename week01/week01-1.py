#week01-1.py
#leetcode 1404. Number of Steps to Reduce a Number in Binary Representation to One
#案计//2 计+1 拜ぐ或跑1
class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0 #羆璶ǐ碭˙
        n = int(s, 2) #р﹃ s 讽2秈俱计跑Θn
        while n > 1:#ヘ夹:n程跑Θ1
            if n%2==0: n = n // 2 #案计//2
            else: n = n + 1#计+1
            ans += 1#暗˙
        return ans#羆璶ǐ碭˙
