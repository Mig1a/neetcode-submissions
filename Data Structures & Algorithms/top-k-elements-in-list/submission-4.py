class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}

        for i in nums:
            if i in store:
                store[i] += 1
            else:
                store[i] = 1
        
        m = sorted(store.items(), key = lambda x:x[1] ,reverse = True)
        print(m)
        res = []

        for i in range(k):
            res.append(m[i][0])
        return res
        