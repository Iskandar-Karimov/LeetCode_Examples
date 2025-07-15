class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        #Get rid of uppercase (not relevant)
        word = word.lower().strip()

        #Creating sets to search through faster than lists
        abcs = set(list("abcdefghijklmnopqrstuvwxyz0123456789"))
        vowels = set(list("aeiou"))
        cons = set(list("bcdfghjklmnpqrstvwxyz"))

        #first case (shorter than 3)
        if len(word) < 3:
            return False
        
        #check if all characters are letter and digits
        for char in word:
            if char not in abcs:
                return False
        
        #check for at least 1 vowel and 1 consonant
        numofvowels = 0
        numofcons = 0

        for char in word:
            if char in vowels:
                numofvowels += 1

        for char in word:
            if char in cons:
                numofcons += 1
        
        if numofcons > 0 and numofvowels > 0:
            return True
        else:
            return False
        
