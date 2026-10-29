
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       dic = {} 
       sub = []
       num = 0

       for i in strs:
        ang = ''.join(sorted(i))
        if ang not in dic:
            
            dic[ang] = num
            sub.append([i])
            num += 1
        elif ang in dic:
            sub[dic[ang]].append(i)
       return sub
        