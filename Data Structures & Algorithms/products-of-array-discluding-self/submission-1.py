class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we are given an int array and we are suppose to return an array 
        # where output[i] is the product of nums except nums[i], 
        # meaning one item is not included

        # would i get negative integers or any zeros in the arg? yes
        # a variable of an empty array to store the products - the nums[i]
        # a variable to the total product of the nums
        # a for loop to find the product and incremnet the var
        # another for loop to divide the total product and num[i],
        # then store it in the array

        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
       
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
        
        
        




        