class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();

        for(String s : strs){

            int[] freq = new int[26];

            for(char c : s.toCharArray()){
                freq[c - 'a']++;
            }

            StringBuilder key = new StringBuilder();
            for(int i = 0; i < 26; i++){
                key.append(freq[i]).append(',');
            }

            if(!map.containsKey(key.toString())){
                map.put(key.toString(), new ArrayList<>());
            }

            map.get(key.toString()).add(s);
        }

        List<List<String>> result = new ArrayList<>();

        for (String key : map.keySet()) {
            result.add(map.get(key));
        }

        return result;
    }
}
