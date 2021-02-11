class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        ans = 0
        heights = [0] + heights + [0]
        print(heights[stack[-1]])
        for right in range(len(heights)):
            while (heights[stack[-1]] > heights[right]):
                height = heights[stack.pop()]
                left_border_of_popped = stack[-1]
                width = right - left_border_of_popped - 1
                ans = max(ans, width * height)
            stack.append(right)
        return ans