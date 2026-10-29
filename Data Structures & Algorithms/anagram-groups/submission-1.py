class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #functions accepts multiple str in a array, 
        #group the same characters in a sub array(angram)
        
        s = defaultdict(list)
        for i in strs:
            k = ''.join(sorted(i))
            s[k].append(i)
        return list(s.values())
                




        