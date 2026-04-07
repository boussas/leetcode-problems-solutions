class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,Set=0,set()
        ans=0
        for r in range(len(s)):
            curr=s[r]
            while curr in Set:
                Set.remove(s[l])
                l+=1
            ans=max(ans,r-l+1)
            Set.add(curr)
        return ans