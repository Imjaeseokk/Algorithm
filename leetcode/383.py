class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomList = list(ransomNote)
        magazine = list(magazine)
        for char in sorted(set(ransomList)):
            if (ransomList.count(char)) > magazine.count(char):
                return False

        return True