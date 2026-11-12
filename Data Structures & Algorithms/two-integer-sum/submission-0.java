class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] indices = new int[2];
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        
        for(int i = 0; i < nums.length; i++){
            int complement = target - nums[i];

            if(map.containsKey(complement)){
                indices[0] = map.get(complement);
                indices[1] = i;
            }

            map.put(nums[i], i);
        }

        return indices;
    }
}
