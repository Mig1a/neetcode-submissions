class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """ input: list of int, an int
            output: [2 indices]

            from the list if two numbers add and equals the target return the position of 
            these two numbers

            create a dict to the the num difference from the target
            loop and check if the difference is already in the dict
            if the difference isnt in the dict, add the key:item[num] and its index value:
                if its available return the current item index and the coming item index
        """
        store = {}

        for k,i in enumerate(nums):
            if target - i in store:
                return [store[target - i],k]
            else:
                store[i] = k
     
        