class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        for i in range(max(len(word1), len(word2))):
            if len(word1) > i:
                merged += word1[i]
            else:
                merged += word2[i : len(word2)]
                break
            if len(word2) > i:
                merged += word2[i]
            else:
                merged += word1[i + 1 : len(word1)]
                break
        return merged


class SolutionBetter:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        len1 = len(word1)
        len2 = len(word2)
        minLen = min(len1, len2)
        for i in range(minLen):
                merged += word1[i]
                merged += word2[i]
        if len1 > len2:
            merged += word1[minLen: len1]
        else:
            merged += word2[minLen: len2]
        return merged

sol_test = SolutionBetter()
print(sol_test.mergeAlternately("abskl", "de"))