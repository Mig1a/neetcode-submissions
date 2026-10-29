class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        input: list of str
        output: 2d array with str

        group all anagrams into a sublist

        index count = 0
        create a dict to store the index for each sublist
        create a list of list
        loop through and sort each item, if item not in the store add it and increment the index count
        and append the [item] in to the list

        if the sorted item is in the store dict, take its index and append it to the sublist
        return the sublist 2d array
        """

        count = 0
        store = {}
        sub = []

        for i in strs:
            so = ''.join(sorted(i))
            print(so)

            if so not in store:
                store[so] = count
                count += 1

                sub.append([i])
            else:
                sub[store[so]].append(i)
        return sub

         

        