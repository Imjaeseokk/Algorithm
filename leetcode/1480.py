class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [0 for _ in range(len(nums))]
        for i, v in enumerate(nums):
            if i == 0: 
                result[i] = nums[i]
                continue
            result[i] = result[i-1]+v
                    
        return result