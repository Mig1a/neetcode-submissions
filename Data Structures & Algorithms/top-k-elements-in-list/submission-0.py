class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #function takes two args, an int array and and int k, 
        #should return k most frequent elements in the array
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        sortfre = dict(sorted(freq.items(), key = lambda x:x[1],reverse = True))
        result = list(sortfre.keys())[:k]
        return result



        