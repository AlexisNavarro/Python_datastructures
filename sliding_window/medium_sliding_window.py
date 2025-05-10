class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):

            #remove the duplicates in the set until there are no more
            #also increment the left pointer by 1 after removal
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1

            #add the current character to the set to make sure we know we visited that character
            charSet.add(s[r])

            # res will be the max between res and the current index (right pointer) - left pointer + one for inclusive
            res = max(res, r - l + 1)
        return res
            