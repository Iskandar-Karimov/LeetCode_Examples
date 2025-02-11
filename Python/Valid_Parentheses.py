class Stack():
    def __init__(self, mylist = []):
        self.list = mylist

    def is_empty(self):
        return len(self.list) == 0
    
    def add_item(self, element):
        self.list.append(element)

    def remove_item(self):
        return self.list.pop(-1)
    
    def peek(self):
        return self.list[-1]

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        myStack = Stack([])
        open_to_close = {"(":")", "{":"}", "[":"]"}
        close_to_open = {")": "(", "}": "{", "]":"["}
        for character in s:
            if character in open_to_close:
                myStack.add_item(character)
            else:
                if not myStack.is_empty() and myStack.peek() == close_to_open[character]:
                    myStack.remove_item()
                else:
                    return False
        return myStack.is_empty()


        
    