class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        mySet = set()
        
        for value in nums:
            if value in mySet:
                return True
            mySet.add(value)
        return False