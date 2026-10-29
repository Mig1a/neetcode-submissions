class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return -1
        left = 0
        right = len(nums) - 1

        while left <= right:#0 < 5, 3 < 5, 2
            mid = (right + left) // 2  #5//2 = 2, 5+3//2 = 4

            if nums[mid] == target:#2 == 4 no,6 == 4 no
                return mid
            elif nums[mid] < target:# yes 2<4, no
                left = mid + 1 # left = 3,
            else:#no, yes 6 > 4
                right = mid - 1 #right = 4 - 1= 3

        return -1

        