class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int n=nums.length;
        List<List<Integer>> buckets = new ArrayList<>(n + 1);
        for (int i = 0; i <= n; i++) {
            buckets.add(new ArrayList<>());
        }
        HashMap<Integer,Integer> map=new HashMap<>();
        for(int num:nums){
            map.put(num,map.getOrDefault(num,0)+1);
        };
        for(int num:map.keySet()){
            buckets.get(map.get(num)).add(num);
        }
        int[] ans=new int[k];
        int idx=0;
        for(int i=n;i>=0;i--){
            if(buckets.get(i).isEmpty()){
                continue;
            };
            for(int num:buckets.get(i)){
                ans[idx++]=num;
                if(idx==k) return ans;
            }
        }
        return ans;
    }
}
