class Solution:
    #Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
    def hasDuplicate(self, nums: list[int]) -> bool:
        dupes = set()

        for item in nums:
            if item in dupes:
                return True
            else:
                dupes.add(item)
        return False



def main():
    duplicates = [1,2,3,4,4,5]
    no_duplicates = [1,2,3,4,5]
    solution = Solution()
    print(solution.hasDuplicate(duplicates))
    print(solution.hasDuplicate(no_duplicates))


if __name__ == "__main__":
    main()