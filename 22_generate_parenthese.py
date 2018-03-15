class Solution:
    def generateParenthese(self, n):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2*n:
                ans.append(S)
                return
            if left < n:
                backtrack(S + '(', left + 1, right)
            if right < left:
                backtrack(S + ')', left, right + 1)
            backtrack()
            return ans
        
class solution2(object):
    def generateParenthese(self, n):
        if n == 0:
            return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthese(c):
                for right in self.generateParenthese(n-1-c):
                    ans.append('({}){}'.format(left,right))
        return ans






