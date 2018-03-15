"""Next Greater Element II"""

"""Example: input = [1,2,1], output = [2,-1,2]"""

class solution(object):
    def nextGreaterElements(self, nums):
        i, s = len(nums),[]
        ans = [-1 for j in range(l)]
        for i in range(l) * 2:
            while s and nums[s[-1]] < nums[i]:
                x = s.pop()
                ans[x] = nums[i]
            s.append(i)
        return ans
