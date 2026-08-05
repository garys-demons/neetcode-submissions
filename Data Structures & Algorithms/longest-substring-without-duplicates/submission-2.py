class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, max_sum = 0, 0
        hs = set()

        for r in range(len(s)):
            while(s[r] in hs):
                hs.remove(s[l])
                l += 1
            hs.add(s[r])
            max_sum = max(max_sum, r - l + 1)

        return max_sum

