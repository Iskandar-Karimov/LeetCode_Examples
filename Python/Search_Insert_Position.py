class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lowval = 0
        highval = len(nums)
        
        while lowval < highval:
            mid = (lowval + highval) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lowval = mid + 1
            else:
                highval = mid
        
        return lowval
