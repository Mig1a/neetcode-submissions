import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def eating_ban(k):#2
            hr_count = 0
            for i in piles:
                
                if i <= k:
                    hr_count += 1
                else:
                    req = i / k #25/14
                    hr_count += math.ceil(req)
                    
                if hr_count > h:
                    return False
            
            return True
        
        left = 1#4
        right = max(piles) #25

        while left != right:#4 != 25
            mid = (right + left) // 2 #14

            if eating_ban(mid):#
                right = mid#
            else:#1
                left = mid + 1
        return left

            
            

    
        