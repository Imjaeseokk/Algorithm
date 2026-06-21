class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        sorted_costs = sorted(costs)
        cnt = 0
        for i, cost in enumerate(sorted_costs):
            if cost <= coins:
                cnt += 1
                coins -= cost
            else:
                return cnt
        return cnt

        
        