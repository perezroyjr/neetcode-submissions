class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        concatted_array = []
        count = 0

        for i in range((len(nums) * 2)):
            if i >= len(nums):
                concatted_array.append(nums[count])
                count += 1
            else:
                concatted_array.append(nums[i])

        return concatted_array