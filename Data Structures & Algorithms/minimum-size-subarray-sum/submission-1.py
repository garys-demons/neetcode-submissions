class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        sas, left = 0, 0

        for right in range(len(nums)):
            sas += nums[right]

            while(sas >= target):
                res = min(right - left + 1, res)
                sas -= nums[left]
                left += 1

        return 0 if res == float("inf") else int(res)