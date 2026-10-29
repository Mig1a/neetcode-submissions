class Solution:
    def isPalindrome(self, s: str) -> bool:

        #function takes a str, 
        #return true if the str have the same chr when reading forward and backward.
        # else False

        #case insensitive, ignore non alphanumeric chr
        

        # join s
        #empty str, to hold thr reverse str
        #reverse the str using while loop
        #compare if they are the same


        
        res = ''
        for i in s:
            if i.isalnum():
                res += i.upper()
        return res == res[::-1]

        