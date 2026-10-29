class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Function takes multiple int in arrays, 
        #return the longest consecutive sequence of elements that can be formed

        #sort in a set
        #a list that collects the counts
        #a count var
        #for loop to check a preceding item is greater than by one from the previous item
        #if its just by one increase count by one, 
        #else append count to the collector list and make it 1 again
        #sort the collector list and return the hihest value

        if not nums:
            return 0
        clean = sorted(set(nums))
        collect = list([1])
        count = 1
        for i in range(len(clean) - 1):
            if clean[i+1] - clean[i] == 1 or clean[i+1] - clean[i] == -1:
                collect[-1] += 1
            else:
                collect.append(count)
        return sorted(collect, reverse = True)[0]
        