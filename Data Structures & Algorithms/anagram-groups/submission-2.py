class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        function takes 1 arg,

        1. a list of str representing same charachters but different meaning, anagrams

        group the items with the same chr together in a 2d array

        create a dict to hold the sorted items and their index in the out put var
        create a list
        iterate through the list
        ind var
        sort the chr and check if they are in the dict, if not in the dict add it with the current ind var
        and append it to the out put var
        if it is already in the dict, just get the index and append it to the out put var
        """
        cont = {}
        result = []
        index = 0
        for item in strs:
            
            s = ''.join(sorted(item))
            print(s)
            if s in cont:
                result[cont[s]].append(item) 
            else:
                cont[s] = index
                result.append([item])
                index += 1
        print(cont)
        return result 

        