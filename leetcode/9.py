class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        x_reverse = x_str[::-1]

        result = True
        for i,v in enumerate(x_str):
            if x_str[i] != x_reverse[i]:
                result = False
                return result
        
        return result