class Solution {

    public String encode(List<String> strs) {
        StringBuilder str=new StringBuilder();
        for(String st:strs){
            str.append(st.length()).append("#").append(st);
        };
        return str.toString();
    }

    public List<String> decode(String str) {
        List<String> strs= new ArrayList<>();
        int i=0,j=0,n=str.length();
        while(i<n){
          while(str.charAt(j)!='#'){
                j++;
          }
          int size=Integer.parseInt(str.substring(i,j));
          strs.add(str.substring(j+1,j+size+1));
          i=j+size+1;
          j=i;
        };
        return strs;
    }
}
