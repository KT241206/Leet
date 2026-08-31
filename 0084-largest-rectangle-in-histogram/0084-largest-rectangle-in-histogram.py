class Solution(object):
    def largestRectangleArea(self,heights):
        stack=[]
        ans =0
        for i in range(len(heights)+1):
            current = heights[i] if i<len(heights) else 0
            while stack and heights[stack[-1]]>current:
                h=heights[stack.pop()]
                left=stack[-1] if stack else -1
                width = i-left-1
                ans=max(ans,h*width)
            stack.append(i)
        return ans