class Solution:
    #Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
    def hasDuplicate(self, nums: list[int]) -> bool:
        #create an empty set that will be used to store unique values from the nums array
        dupes = set()

        for item in nums:
            #if the nums val exists in the set then return true, if not add that value to the set and continue checking the array
            if item in dupes:
                return True
            else:
                dupes.add(item)
        return False

    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        s_map, t_map ={},{}

        for item in s:
            if item in s_map:
                s_map[item] +=1
            else:
                s_map[item] = 1

        for item2 in t:
            if item2 in t_map:
                t_map[item2] +=1
            else:
                t_map[item2] = 1

        return s_map == t_map
    
    def twoSum(self, nums, target: int):
        #make a hash map that will have the difference 
        mapping = {}

        for i,n in enumerate(nums):
            diff = target-nums[i]
            if diff in mapping:
                return [mapping[diff], i]
            mapping[n] = i
    

def main():
    # duplicates = [1,2,3,4,4,5]
    # no_duplicates = [1,2,3,4,5]
    # solution = Solution()
    # print(solution.hasDuplicate(duplicates))
    # print(solution.hasDuplicate(no_duplicates))

    solution2 = Solution()
    s1 = "racecar"
    t1 = "carrace"
    print(solution2.isAnagram(s1,t1))
    s2 = "raceca"
    t2 = "carrac"
    print(solution2.isAnagram(s2,t2))

if __name__ == "__main__":
    main()