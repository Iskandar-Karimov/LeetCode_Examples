class Solution(object):
    def return_binary(self,num):
        binary = ""
        if num == 0:
            binary = "0"
        while num != 0:
            binary = str(num%2) + binary
            num = num // 2
        return binary
        
            
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        split_date = date.split("-")
        for i in range(len(split_date)):
            split_date[i] = self.return_binary(int(split_date[i]))
        joined = "-".join(split_date)
        return joined