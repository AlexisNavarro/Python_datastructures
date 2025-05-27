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

    def characterReplacement(self, s: str, k: int) -> int:
        freq = {} #hashmap to count occurences of each char
        res = 0

        l = 0
        maxf = 0 #frequency of the most common character in the current window

        #r is the right pointer
        for r in range(len(s)):
            
            freq[s[r]] = 1 + freq.get(s[r], 0) #count the character at index r
            maxf = max(maxf, freq[s[r]]) #update max frequency

            #check if the window is valid, window size -frequent character count
            #if the amount of characters needed to replace are greater than k then shrink the window from the left
            while (r-l+1) - max(freq.values()) > k: 
                freq[s[l]]-=1
                l += 1

            res = max(res, r-l+1) #store the largest window size
        return res
