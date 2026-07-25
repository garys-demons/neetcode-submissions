class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr_sum = 0
        seen = {0: 1}
        for num in nums:
            curr_sum += num
            count += seen.get(curr_sum - k, 0)
            seen[curr_sum] = seen.get(curr_sum, 0) + 1
        return count