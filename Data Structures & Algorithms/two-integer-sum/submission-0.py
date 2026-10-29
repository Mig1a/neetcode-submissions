class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #a list of int, and a target
        # return the index if two items sumation equals the target 
        #and these two items shoud not be equal

        #would there be any negative numbers or zeros? for both list and target
        #no reptition in the list.

        cont = {}
        for index,i in enumerate(nums):
            if target - i not in cont:
                cont[i] = index
            else:
                h = [cont[target - i],index]
                return h



        