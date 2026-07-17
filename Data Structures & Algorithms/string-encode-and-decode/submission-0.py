class Solution:
    def encode(self, strs: List[str]) -> str:
        ans = ""
        for st in strs:
            ans += str(len(st)) + "#" + st
        return ans
    def decode(self, s: str) -> List:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            size = int(s[i:j])
            # extract the string
            res.append(s[j + 1 : j + 1 + size])
            # move to the next encoded string
            i = j + 1 + size
        return res