# LeetCode 151. Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75

# Approach:
# Split → Reverse → Join
# Time: O(n)
# Space: O(n)

# Better Solution
class SolutionBetter:
    def reverseWords(self, s: str) -> str:
        list_s = s.split()      # .split() creates a list with words, no spaces
        list_s = list_s[::-1]   # [start : stop : step] slicing. -1 step
                                # reverses the list
        return " ".join(list_s) # " ".join(list) joins the list adding one
                                # space in between the elements

# More time-consuming and messy
class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0
        word = ""
        new_s = ""
        len_s = len(s)

        while i < len_s:
            current = (s[i] != " ")
            right = (i == len_s - 1 or s[i + 1] == " ")

            if current:
                word += s[i]
                if right:
                    new_s = word + " " + new_s
                    word = ""

            i += 1

        return new_s[0 : len(new_s) - 1]

sol = Solution()
print(sol.reverseWords("the sky is blue"))