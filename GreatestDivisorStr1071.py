# Solution 1 -- Brute Force
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        longest, shortest = (str1, str2) if len(str1) > len(str2) else (str2, str1)
        len_long = len(longest)
        len_short = len(shortest)

        if shortest == longest [0: len_short]:
            divisor = shortest
        else: return ""

        len_divisor = len(divisor)
        while len_long % len_divisor != 0 or len_short % len_divisor != 0:
            if len_long % len_divisor != 0:
                divisor = divisor[0 : len_long % len_divisor]
            else:
                divisor = divisor[0: len_short % len_divisor]
            len_divisor = len(divisor)
            if len_divisor == 0:
                return ""

        for i in range(0, len_long - len_divisor + 1, len_divisor):
            if longest[i : i + len_divisor] != divisor:
                return ""

        return divisor



# Solution 2 -- A trick
from math import gcd

class SolutionBetter:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 == str2 + str1:
            return str1[:gcd(len(str1), len(str2))]
        return ""

sol = Solution()
print(sol.gcdOfStrings("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"))