class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left, max_sum = 0, 0
        hs = set()

        for right in range(n):
            while s[right] in hs:
                hs.remove(s[left])
                left += 1
            hs.add(s[right])
            max_sum = max(max_sum, (right - left + 1))

        return max_sum
