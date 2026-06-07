class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        leftSum, totalSum = 0 , 0
        for i in range(len(nums)):
	        totalSum += nums[i]
        for i in range(len(nums)):
	        rightSum = totalSum - leftSum - nums[i]
	        answer.append(abs(leftSum - rightSum))
	        leftSum += nums[i]
        return answer