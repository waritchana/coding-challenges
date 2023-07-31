from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # The challenge is to reach the top which is not the
        # last item but the position after
        cost.append(0)
        # Start from the third item from the last
        # going backward to index 0
        for i in range(len(cost)-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])


#cost = [10,15,20]
cost = [1,100,1,1,1,100,1,1,100,1]
min_cost = Solution().minCostClimbingStairs(cost)
print(f"Minimum cost to reach the top of the floor is {min_cost}")
