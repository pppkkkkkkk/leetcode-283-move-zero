class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0 # idx
        j = 0 # search for num > 0

        while j < n:
            while j < n and nums[j] == 0:
                j+=1
            if j<n:
                nums[i] = nums[j]
                i += 1
            j += 1
        while i < n:
            nums[i] = 0
            i += 1

        return nums
                