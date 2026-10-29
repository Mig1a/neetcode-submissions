class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        input: list of int
        output: list of list of int

        look for 3 int where they add up their value is 0. and their indices are different.

        sort the nums increasing order
        create a list

        loop i - through the sorted list
            set a pointer j = i + 1 from left and right - k
            loop from j to k
                check if j + k + i == 0, if it equals add them as a list to the var list
                elif j + k + i > 0 decrease k, if < 0 increase j
        """
        so = sorted(nums)
        res = []

        for i in range(len(so)-1):
            if so[i] > 0:
                break
            if i > 0 and so[i] - 1 == so[i]:
                continue
           
            j = i + 1
            k = len(so) - 1

            while j < k:
                if so[j] + so[k] + so[i] > 0: 
                    k -= 1
                elif so[j] + so[k] + so[i] < 0:
                    j += 1
                else:
                    li = [so[i],so[j],so[k]]
                    if li not in res:
                        res.append(li)
                    k -= 1
        return res
        


                    

