#week08-4.py 學習計畫Binary Search第2題
#LeetrCode 2300. Successful Pairs of Spells and Potions
#想知某種 spells[i]魔法 配給種藥水可以成功?
#魔法師 施咒spell 配合 藥水potion 要乘起來
#spell[i] vs. potion[j] 希望乘起來後 >= success值
#但陣列很大 不能暴力 全部都試乘一次 可potion先sort後 再binary search
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort() #藥水小到大排好
        P = len(potions) #有p種藥水
        ans = []
        for spell in spells: #每一種魔法 都試一次
            now = len(potions) - bisect_left(potions, success/spell)
            ans.append(now) #全部藥水有p瓶 - 會失敗的藥水??瓶,便是成功的藥水數量
        return ans

