class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        input: str
        output: Boolean

        check if the input str have the same chr when its reversed

        remove any chr other than A-Z,a-z,0-9 ---- alphanum
            - loop through s check if each chr is alphanum and add it to a new var
        create a pointer from the right side
        loop through the new created alphanum var and reverse all chr to a new chr
        check if they are the same and return a boolean
        """
        clean = ''

        for i in s:
            if i.isalnum():
                clean += i.lower()
        right = len(clean) - 1
        reverse = ''
        while right >= 0:
            reverse += clean[right]
            right -= 1
        
        return clean == reverse
        