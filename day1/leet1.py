# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

class Solution:
    """def containsDuplicate(self, nums: List[int]) -> bool:"""
    def containsDuplicate(self, nums):
        """
        First Pass:
        s = set(nums)
            
        # if len(s) == len(nums), then there were no duplicates
        if len(s) == len(nums):
            return False
        # otherwise, there was at least one duplicate
        return True
        """
        
        """
        Second Pass
        s = set(nums)

        return len(s) < len(nums)
        """
        
        """
        Third Pass:
        s = set()
        
        for x in nums:
            if x in s:
                return True
            else:
                s.add(x)
        return False
        """
        
        return True if len(set(nums)) < len(nums) else False

if __name__ == "__main__":
    

    x = Solution()

    nums = [1,2,3,4]

    print("NUMS 1:", x.containsDuplicate(nums)) #> Should return False

    nums = [1,2,2,4]

    print("NUMS 2:", x.containsDuplicate(nums)) #> Should return True
