class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ht = {}
        for i in range(len(nums)):
            ht[nums[i]] = i

        for i in range(len(nums)):
            x = nums[i]
            if((x in ht.keys()) and (ht[x] != i)):
                return True
        
        return False 