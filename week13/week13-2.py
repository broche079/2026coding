from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0]) # 長 寬
        visited = set()
        queue = deque()
        fresh = 0 # 先統計有幾個新鮮的橘子

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 2:
                    visited.add((i, j))
                    queue.append((i, j, 0)) # 把爛掉的橘子放入 queue，時間從 0 開始
                if grid[i][j] == 1:
                    fresh += 1 # 多 1 個新鮮的橘子

        if fresh == 0: return 0 # 題目如果都沒有新鮮的橘子，要 return 0

        ans = -1 # 用來紀錄最後一隻橘子腐爛的時間

        while queue:
            i, j, t = queue.popleft()
            ans = t # 更新最後腐爛的時間
            for ii, jj in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if ii < 0 or jj < 0 or ii >= M or jj >= N: continue
                if (ii, jj) in visited: continue
                if grid[ii][jj] == 1: # 這格是還沒爛掉的橘子 可感染他
                    fresh -= 1 # 好可憐 他爛了
                    visited.add((ii, jj))
                    queue.append((ii, jj, t+1)) # 將在 t+1 時爛掉

        # 關鍵檢查：如果排空 queue 之後，還有新鮮橘子沒被連通到
        if fresh > 0:
            return -1

        return ans # 如果大家都爛完了，回傳最後的時間
