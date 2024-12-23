class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen_numbers = {}
        for i in range(len(nums)):
            current_number = nums[i]
            complement_number = target - nums[i]
            if complement_number in seen_numbers:
                return i, seen_numbers[complement_number]
            else:
                seen_numbers[current_number] = i