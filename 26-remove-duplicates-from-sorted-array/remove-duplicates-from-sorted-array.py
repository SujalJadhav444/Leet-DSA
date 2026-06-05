class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        A = 0
        for B in range(1, len(nums)):
	        if nums[A] != nums[B]:
		        A = A+1 
		        nums[A] = nums[B]
        k = A + 1
        return k