class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        i = 0
        r = len(nums)
        t = r
        while(i<r):
            if nums[i] == 0:
                del nums[i]
                r = r -1
            else :
                i = i +1

        
        for i in range(t -r):
            nums.append(0)
