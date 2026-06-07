class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = [target-i for i in nums]
        result = []
        for i,v in enumerate(diffs):
            if v in nums:
                if i == nums.index(v):
                    continue
                result = [i, nums.index(v)]

        return result
        