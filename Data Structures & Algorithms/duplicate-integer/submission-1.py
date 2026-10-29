class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        input: list[int]
        output: Boolean

        if there is duplicate in list return true else false
        """
        store = set(nums)
        if len(store) == len(nums):
            return False
        return True



        