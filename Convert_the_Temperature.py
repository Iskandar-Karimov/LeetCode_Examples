class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        kel = celsius + 273.15
        fah = celsius * 1.80 + 32.00
        ans = []
        ans.append(kel)
        ans.append(fah)
        return ans