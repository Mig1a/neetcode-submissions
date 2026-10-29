class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       """
        input: list of int, sorted in increasing order 123456789
        output: list if int, two indices

        look for 2 numbers that equal to a target number and return their indices, location

        create a dict that holds the int and their index
        create an array that holds the result
        loop through the list-input
            - check if the target int minus the incoming item-int value exists in the dict
            - if this value exsits return the index of the value from the dict and the index
                of the incoming item-int
            - if the difference of target and incoming item is not in the dict 
              just add the item as a key and the index as a value
       """

       cont = {}
       

       for k,i in enumerate(numbers):
        if target - i in cont:
            return [cont[target - i], k + 1]
        else:
            cont[i] = k +1