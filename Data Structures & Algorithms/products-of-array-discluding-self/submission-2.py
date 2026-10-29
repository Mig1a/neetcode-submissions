class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        input: list of int
        output: list of int

        create a list len(nums) int
        
        """
        res = [0] * len(nums)
        left = 1
        count = 0

        while count < len(nums):
            res[count] = left
            left = left * nums[count]
            count += 1

        right = 1
        count = len(nums) - 1

        while count >= 0:
            res[count] = res[count] * right
            right = right * nums[count]
            count -= 1
        
        return res