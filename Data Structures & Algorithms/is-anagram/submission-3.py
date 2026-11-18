class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        sMap = {}
        tMap = {}

        for value1,value2 in zip(s,t):
            if value1 in sMap:
                sMap[value1] = sMap[value1] + 1
            else:
                sMap[value1] = 1
            if value2 in tMap:
                tMap[value2] = tMap[value2] + 1
            else:
                tMap[value2] = 1

        if sMap == tMap:
            return True
        
        return False
