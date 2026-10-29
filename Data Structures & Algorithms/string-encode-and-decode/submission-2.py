class Solution:
    """
    input:list of str
    output:encode - single str,
    decode input: single str
    output: list of str
    """
    def encode(self, strs: List[str]) -> str:
        res = ''

        for i in strs:
            num = str(len(i))
            res += num
            res += '-'
            res += i
            
        return res

    def decode(self, s: str) -> List[str]:
        
        count = 0
        res = []

        while count < len(s):
            j = count
            

            while s[j] != '-':
                j += 1
            num = int(s[count : j])
            count = j + 1
            j = count + num   
            res.append(s[count:j])
            count = j
        return res


