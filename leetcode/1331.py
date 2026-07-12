class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(arr)

        num_to_rank = dict()
        result = []
        rank = 1

        for i, e in enumerate(sorted_arr):
            if i > 0 and (sorted_arr[i] > sorted_arr[i-1]):
                rank += 1
            num_to_rank[sorted_arr[i]] = rank
        
        for e in arr:
            result.append(num_to_rank[e])

        return result