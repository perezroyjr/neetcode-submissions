class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_1 = {}

        dict_2 = {}

        if len(s) != len(t):
            return False

        for char in s:
            dict_1[char] = dict_1.get(char, 0) + 1

        for char in t:
            dict_2[char] = dict_2.get(char, 0) + 1

        
        return dict_1 == dict_2