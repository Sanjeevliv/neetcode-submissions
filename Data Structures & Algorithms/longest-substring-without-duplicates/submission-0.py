class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    # Brute Force using empty set(), add till find 
    # duplicate, new empty set() repeat for max len of set
        res = 0 
        for i in range(len(s)):
            charSet = set()
            for j in range(i, len(s)):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
            res = max(res, len(charSet))
        return res
        
        
    