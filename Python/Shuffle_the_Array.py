class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        x = nums[:len(nums) // 2]
        y = nums[len(nums)//2:]
        together = []
        for i in range(n):
            together.append(x[i])
            together.append(y[i])
        return together
            