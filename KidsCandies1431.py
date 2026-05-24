class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        biggest = sorted(candies)[len(candies) - 1]
        result = []

        for candy in candies:
            if (candy + extraCandies) >= biggest:
                result.append(True)
            else:
                result.append(False)

        return result

sol = Solution()
print(sol.kidsWithCandies([2,3,5,1,3], 3))