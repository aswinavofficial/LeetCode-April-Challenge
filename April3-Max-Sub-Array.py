class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum = 0
        max_sum = nums[0]
        index = 0
        
        if len(nums) == 1 :
            return nums[0]
        
        for i in nums :
            current_sum = current_sum + i
            
            max_sum = max(max_sum,current_sum)
            current_sum = max(0,current_sum)
        return max_sum
              
