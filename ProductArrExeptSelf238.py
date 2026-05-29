# LeetCode 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=leetcode-75

# Approach:
# - left[i] stores the product of all elements to the left of i
# - right[i] stores the product of all elements to the right of i
# - answer[i] = left[i] * right[i]

# Note for Self:
# The task had two constraints: time complexity is O(n), and the algorithm
# cannot use division. Hint for such questions is to use more than one loop
# instead of nested loops. In here the time complexity is linear, but if I were
# to use nested loops it would be O(n^2).

# Time: O(n)
# Space: O(n)

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = []
        nums_len = len(nums)
        left = [1] * nums_len
        right = [1] * nums_len

        i = 0
        j = nums_len - 1
        while i < nums_len - 1:
            left[i + 1] = left[i] * nums[i]
            right[j - 1] = right[j] * nums[j]
            i += 1
            j -= 1

        i = 0
        while i < nums_len:
            answer.append(left[i] * right[i])
            i += 1

        return answer

sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))