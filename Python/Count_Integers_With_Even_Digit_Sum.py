class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        found = []
        for i in range(1, num + 1):
            i = str(i)
            if sum(map(int, i)) % 2 == 0:
                found.append(i)
        return len(found)
            
        