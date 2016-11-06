class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len( nums ) <= 1:
            return False
        numDict = {}
        for i in range( len( nums ) ):
            if nums[i] in numDict:
                return [numDict[nums[i]], i]
            else:
                numDict[target - nums[i]] = i
        return False