class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        i = 0
        len_flowerbed = len(flowerbed )

        while i < len_flowerbed:
            if n == 0:
                return True

            if flowerbed[i] == 0 and (i + 1) <= len_flowerbed:
                if i + 1 == len_flowerbed or flowerbed[i + 1] == 0:
                    n -= 1
                    i += 2
                else:
                    i += 1
            else:
                i += 2

        if n != 0:
            return False
        return True


# Simpler Solution?

class Solution1:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        i = 0
        len_flowerbed = len(flowerbed)

        while i < len_flowerbed:
            if n == 0:
                return True

            if flowerbed[i] == 0:
                left = (i == 0 or flowerbed[i - 1] == 0)
                right = (i == len_flowerbed - 1 or flowerbed[i + 1] == 0)

                if left and right:
                    n -= 1
                    i += 1

            i += 1

        if n != 0:
            return False
        return True


sol = Solution1()
print(sol.canPlaceFlowers([1,0,0,0,1], 1))