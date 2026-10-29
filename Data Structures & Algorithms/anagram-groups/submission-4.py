class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}
        res = []
        pos = 0

        for word in strs:
            order = ','.join(sorted(word))
            print(order)

            if order in store:
                res[store[order]].append(word)
            else:
                store[order] = pos
                res.append([word])
                pos += 1
        
        return res
        