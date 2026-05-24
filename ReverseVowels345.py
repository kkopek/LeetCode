class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u']
        lst = list(s)

        while i < len(s) and j > i:
            left = lst[i].lower() in vowels
            right = lst[j].lower() in vowels

            if left and right:
                lst[i], lst[j] = lst[j], lst[i]
                j -= 1
                i += 1
            elif left:
                j -= 1
            elif right:
                i += 1
            else:
                j -= 1
                i += 1

        return ''.join(lst)

sol = Solution()
print(sol.reverseVowels("IceCreAm"))