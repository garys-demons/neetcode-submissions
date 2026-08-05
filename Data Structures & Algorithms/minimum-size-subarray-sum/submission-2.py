class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        sas, l = 0, 0

        for r in range(len(nums)):
            sas += nums[r]

            while(sas >= target):
                res = min(res, r - l + 1)
                sas -= nums[l]
                l += 1

        return 0 if res == float("inf") else int(res)