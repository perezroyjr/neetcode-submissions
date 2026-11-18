class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe_map = {}

        for num in nums:
            if num not in dupe_map:
                dupe_map[num] = 1
            else:
                return True
        
        return False


        