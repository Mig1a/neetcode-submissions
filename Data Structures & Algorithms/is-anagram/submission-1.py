class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        """
        input: 2 str
        output: Boolean

        var t needs to have the same chr as var s to be called anagram
        check the len is equal
        create a hash
        loop and add the chr in s to the hash and increment the num of the chr
        loop and sub the chr in t to the hash and if chr isnt avail in hash 
        return false
        loop to check any thing <> 0
        """

        if len(s) != len(t):
            return False
        
        store = {}
        for i in s:
            if i in store:
                store[i] += 1
            else:
                store[i] = 1
        for i in t:
            if i not in store:
                return False
            else:
                store[i] -= 1
        for i in store.values():
            
            if i != 0:
                return False
        return True

        

            

        

        