class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        input: list of int
        output: int

        each int represent a height and there index is width area = b*h
        find the max area
        set a pointer
        create a var to hold the area
        loop through the list
            take the smallest item from the left and right side
            and multiply it with the index difference of the left and the right items
            and compare the current area with previous areas to find the max
            and move the pointer with the smallest item
        return the area
        """
        
        l,r = 0,len(heights) - 1
        max_area = float('-inf')

        while l < r:
            height = min(heights[l],heights[r])
            base = r - l
            area = base * height
            max_area = max(max_area,area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area
        