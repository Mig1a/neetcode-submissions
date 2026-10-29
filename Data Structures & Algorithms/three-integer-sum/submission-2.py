class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       so = sorted(nums)
       res = []
       for i in range(len(nums)):
        l,r = i+1, len(nums) -1
        while l < r:
            con =[]
            if so[i] + so[l] + so[r] > 0:
                r -= 1
            elif so[i] + so[l] + so[r] < 0:
                l += 1
            else:
                con.append(so[i])
                con.append(so[l])
                con.append(so[r])
                if con not in res:
                    res.append(con)
                l+=1
                r-=1
       return res
        