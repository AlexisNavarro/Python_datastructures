from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #mapping character count to list of anagrams

        for s in strs:
            count = [0] * 26  # creates a list of length 26 to count letters a-z, this will reset the count being in the loop each time
            
            for c in s:
                #take the current ascii val of a character and subtract it from ascii a
                #get the index of the character in the alphabet
                #ex: ord("a") = 97 -> 0, 97-97 = 0, which is the index 
                #ord("b")= 98 -> 1, 98-97 = 1

                count[ord(c) - ord("a")] +=1
            
            #add the count such as e =1, a = 1, t =1 as a tuple since lists cant be a dictionary key, normally keys are singular and unique
            #tuples are hashable and can represent the character composition of the word

            res[tuple(count)].append(s)
        return list(res.values())
                

