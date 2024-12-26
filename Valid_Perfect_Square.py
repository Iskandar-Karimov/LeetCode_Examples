class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        This uses binary search because the runtime is O(log(n)). 
        """
        low = 1
        high = num
        while high >= low:
            mid = (low + high) // 2
            if mid **2 == num:
                return True
            elif mid ** 2 > num:
                high = mid - 1
            else:
                low = mid + 1
        return False