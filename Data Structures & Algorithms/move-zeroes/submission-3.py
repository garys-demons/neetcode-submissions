class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if (0 in nums):
            z = nums.index(0)
        else: 
            return
            
        for i in range(z + 1, len(nums)):
            if (nums[i] != 0):
                temp = nums[z]
                nums[z] = nums[i]
                nums[i] = temp
                z += 1
        