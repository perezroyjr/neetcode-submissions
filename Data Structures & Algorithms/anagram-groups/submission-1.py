class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in str_map:
                str_map[sorted_word].append(word)
            else:
                str_map[sorted_word] = [word]
        return list(str_map.values())