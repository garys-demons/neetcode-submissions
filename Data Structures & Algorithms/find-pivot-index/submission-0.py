class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)

        for i in nums:
            total += i

        left_sum = 0
        for i in range(n):
            right_sum = total - left_sum - nums[i]
            if(left_sum == right_sum):
                return i 
            left_sum += nums[i]

        return -1