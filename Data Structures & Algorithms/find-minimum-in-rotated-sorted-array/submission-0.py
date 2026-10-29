class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l != r:#0!=5, 3!=5, 3!=4, 4 == 4
            mid = (r + l) // 2 #2, 4, 3

            if nums[mid] < nums[l]:#5 < 3 no, 1 < 2 yes, 6 < 6 no
                r = mid# 4
            elif nums[mid] > nums[r]:#5 > 2 yes, 6 > 1 yes
                l = mid + 1#3 , 4
            else:
                return nums[l]
        return nums[l]#1