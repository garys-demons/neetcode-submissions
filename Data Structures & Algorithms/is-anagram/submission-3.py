class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        shs, ths = {}, {}

        for i in s:
            shs[i] = shs.get(i, 0) + 1

        for i in t:
            ths[i] = ths.get(i, 0) + 1

        return shs == ths