class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
        Map<String, List<String>> groupedAnagrams = new HashMap<>();


        for(String s : strs){

            int[] count = new int[26];

            for(char c : s.toCharArray()){
                count[c - 'a'] += 1;
            }
            String key =  Arrays.toString(count);
            if(!groupedAnagrams.containsKey(key)){
                groupedAnagrams.put(key, new ArrayList<String>());
            }
                groupedAnagrams.get(key).add(s);
        
        }


        return new ArrayList<>(groupedAnagrams.values());


    }
}

