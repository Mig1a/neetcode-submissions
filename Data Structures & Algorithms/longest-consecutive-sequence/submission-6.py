class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        input: list of int
        output : int

        return the longest consecutive sequence that can be formed from the list
        consecutive means i + 1,i + 2, i + 3
        longest means the largest sequence of the consecutive nums

        convert the nums to a set to eliminate duplicates
        create a var that holds the longest consecutive sequence

        loop through the set
        check the incoming item-num has an item-num exactly one num smaller in the set.
        create a var that counts each consecutive sequences
        loop through the set checking if there is a number greater than the current item
        by just one number, if there is increament the length var
        compare the length vs longest and replace
        return the longest 
        """
        num = set(nums)
        longest = 0

        for i in num:
            length = 1
            if i - 1 in num:
                continue
            while i + length in num:
                length += 1
            longest = max(length, longest)
        return longest
        