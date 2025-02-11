class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        num_of_jewels = 0
        type_of_jewels = list(jewels)
        for i in range(len(type_of_jewels)):
            number = stones.count(type_of_jewels[i])
            num_of_jewels += number
        return num_of_jewels