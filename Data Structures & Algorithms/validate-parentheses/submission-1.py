class Solution:
    def isValid(self, s: str) -> bool:
        
        myStack = []

        myMap = {'}':'{', ')':'(', ']':'['}


        for char in s:
            if char in myMap and myStack:
                if myStack[-1] == myMap[char]:
                    myStack.pop()
                else:
                    return False
            else:
                myStack.append(char)
        
        return True if not myStack else False
