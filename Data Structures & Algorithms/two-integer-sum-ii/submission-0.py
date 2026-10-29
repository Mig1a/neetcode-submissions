class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #function takes an int in array sorted in increasing order - 1,2,3,4
        # function takes another target
        #returns the index's if there is two numbers that sum up and equals to target
        #index1 and 2 cant be equal

        #0 or -nums?
        #empty list?

        #change the list in to set to remove depulicate and sort it
        #initalize a dict to store differnces of items compared to target
        #for loop to check if differnces of items compared to target is in the dict
        #if the compared value is not in the dict add the item as key with its index as value
        #else return the index from the dict as dict[value] and sortlist[i]


        
        di = {}

        for i in range(len(numbers)):
            if target - numbers[i] in di:
                return [di[target - numbers[i]], i + 1]
            else:
                di[numbers[i]] = i + 1

        