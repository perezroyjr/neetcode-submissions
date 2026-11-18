class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxOnes = 0

        for num in nums:
            if num == 1:
                count = count + 1
                if count >= maxOnes:
                    maxOnes = count
            elif num == 0:
                count = 0
        return maxOnes
