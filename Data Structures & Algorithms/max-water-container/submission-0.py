class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        function takes 1 arg,

        a list of int - representing a height

        find the max size where max = height * width from the list

        create left and right pointer
        create a var that holds the max value
        iterate till left less than right
        take the minimum value from both side
        multiply it with the width or the len difference of the pointers
        and compare it with var that holds the max value
        replace if it is larger than the current value

        """
        l,r = 0, len(heights) - 1
        large = 0

        while l < r:
            mi = min(heights[r],heights[l])
            cont = mi * (r - l)
            val = max(large,cont)
            large = val
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return large

        