class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        longest, shortest = max(str1, str2, key=len), min(str1, str2, key=len)

