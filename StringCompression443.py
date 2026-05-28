# LeetCode 443. String Compression
# https://leetcode.com/problems/string-compression/description/?envType=study-plan-v2&envId=leetcode-75

# Time: O(n)
# Space: O(1), constant space

class Solution:
    def compress(self, chars: list[str]) -> int:
        counter = 1
        index = 0

        for i in range(len(chars)):
            if i + 1 < len(chars) and chars[i] == chars[i + 1]:
                counter += 1
            else:
                chars[index] = chars[i]
                if counter > 1:
                    for c in str(counter):
                        index += 1
                        chars[index] = c
                counter = 1
                index += 1
        return index

sol = Solution()
print(sol.compress(["a","a","b","b","c","c","c"]))