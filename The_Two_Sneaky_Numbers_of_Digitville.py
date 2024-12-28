class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = []
        dupes = []
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.append(nums[i])
            else:
                dupes.append(nums[i])
        return dupes
