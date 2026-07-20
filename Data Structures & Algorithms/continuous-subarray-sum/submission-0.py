class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d={0:-1}
        s=0
        for i,e in enumerate(nums):
            s+=e
            rem=s%k
            if rem in d:
                if i-d[rem]>1:
                    return True
            else:
                d[rem]=i
        return False