class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        i = 0
        left = s[i]
        right = s[len(left):]

        while(i < len(s) - 1):
            score = left.count("0") + right.count("1")
            max_score = max(max_score, score)
            i += 1
            if (i < len(s)):
                left = s[:i + 1]
                right = s[i + 1:]

        return max_score
