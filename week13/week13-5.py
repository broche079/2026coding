from heapq import heapify, heappush, heappop
from typing import List

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # 挑 k 個 index，讓 nums1 對應的 k 個數相加，再乘 min(nums2對應k個數) 希望最大

        N = len(nums1) # 陣列的長度

        # 左右合併起來。為了依據 nums2 由大到小排序，將 nums2 放在 Tuple 的第一項
        a = [(nums2[i], nums1[i]) for i in range(N)]

        # 大到小排好 (依據 nums2 的值)
        a.sort(reverse=True)

        # 找到最前面的 k 組數字，將 nums1 的值加入 heap 資料結構
        heap = [a[i][1] for i in range(k)]
        heapify(heap) # 之後將從小到大依序吐掉 nums1 的這 k 個數，換納入新的 n1, n2 組

        total = sum(heap)
        ans = total * a[k-1][0] # 前 k 項的 nums1 總和 及對應最小的 nums2 (即第 k 個人的 nums2) 相乘

        for i in range(k, len(nums2)): # 後面將加入的數
            n2, n1 = a[i] # 將加入的對應的數
            heappush(heap, n1) # 加 1
            total += n1 - heappop(heap) # 加 1 吐 1 (扣掉 heap 裡最小的 nums1)
            ans = max(ans, total * n2) # 更新答案

        return ans
