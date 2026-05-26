# LeetCode 334. Increasing Triplet Subsequence
# https://leetcode.com/problems/increasing-triplet-subsequence/description/?envType=study-plan-v2&envId=leetcode-75

# Approach (short version):
# Keep track of the smallest and second-smallest values seen so far.
# If we find a number larger than both, an increasing triplet exists.
# Complexity: O(n)

# Notes to self (deep understanding):
# The approach is very interesting and actually takes advantage of the
# problem conditions. Current algorithm answers the question "is the
# triplet sequence," however if asked what the sequence is the answer would
# be wrong. All because the algorithm aims to find the smallest possible
# values for first and second. If the sequence like [5, 10, 1 ,20] (returns
# true) is taken to consideration here is how iterations will look like:
# 1: first = 5, second = inf
# 2. first = 5, second = 10
# 3. first = 1, second = 10, here is when something interesting happens. The
# indexes for the values are out of order. Let's see next iteration
# 4. returns True since 20 > second (10) > first (1). But wait aren't the
# indexes out of order? Index of first is 2, index of second is 1, and index
# of third is 3.
# However, this doesn't break the algorithm, because it never asked to output
# the indexes, it only asked are there possible arbitrary indexes that
# satisfy the condition?
# Again, the whole idea of the algorith is that it attempts to find the least
# possible number for first and second, that's why during iteration 3 it
# replaces first with 1. The algorithm hopes that in the next iterations we
# will find value for the second that is less than outer current second.
# However, if we do not (as in this example) all we need to know that there
# is the arbitrary sequence that we saw before (5 ,10) that should be less
# then the third num,ber we find.
# TLDR: the algorithm doesn't;t return the correct indexes if asked, it only
# tells whether there is a possibility for those indexes to exist.

class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = float("inf")
        second = float("inf")

        for num in nums:
            if first >= num:            # if current first is more than
                first = num             # offered num, first = num
            elif second >= num:         # if current num more than first and
                second = num            # less than second, second = num
            else:                       # if current num is more than first and
                return True             # second, third = num aka sequence found

        return False

sol = Solution()
print(sol.increasingTriplet([5, 10, 1, -1, 2, 3]))