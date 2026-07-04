class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}

        for i in range(len(nums)):
            ht[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if((diff in ht.keys()) and (ht[diff] != i)):
                return [i, ht[diff]]
            
        return [0,0]