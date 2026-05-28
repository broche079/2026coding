#week14-2c.py 學習計劃 1D DP 第1題
#LeetCode 1137. N-th N-th Tribonacci Number
class Solution:
    def tribonacci(self, n: int) -> int:
        a = [0, 1, 1]
        if n<3: return a[n]
        return self.tribonacci(n-1) + self.tribonacci(n-2) +  self.tribonacci(n-3)
