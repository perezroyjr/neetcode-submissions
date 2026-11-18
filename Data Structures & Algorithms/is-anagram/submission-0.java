class Solution {
    public boolean isAnagram(String s, String t) {

        HashMap<Character,Integer> charMap1 = new HashMap<>();
        HashMap<Character,Integer> charMap2 = new HashMap<>();
        
        if(s.length() != t.length())
            return false;
        
        int x = 0;
        int y = 0;
        for(int i = 0; i < s.length(); i++){

            if(!charMap1.containsKey(s.charAt(i))){
                charMap1.put(s.charAt(i), 1);
            }else{
                charMap1.put(s.charAt(i), charMap1.get(s.charAt(i)) + 1);
            }
            if(!charMap2.containsKey(t.charAt(i))){
                charMap2.put(t.charAt(i), 1);
            }else{
            charMap2.put(t.charAt(i), charMap2.get(t.charAt(i)) + 1);
            }
        }

        if(charMap1.equals(charMap2))
            return true;

        return false;



    }
}
