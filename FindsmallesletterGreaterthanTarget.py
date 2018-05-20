class Solution(object):
    def __init__(self):
        print("init")
    def nextGreatestletter(self,letters,target):
        for c in letters:
            if c > target:
                return c
        return letters[0]