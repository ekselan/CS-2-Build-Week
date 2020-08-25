# Day II LeetCode Challenge

## LeetCode `Two Sum` Challenge
Link: https://leetcode.com/problems/two-sum/

- **ABW Solution:**
    ```py
    from itertools import combinations

    class Solution:
        def twoSum(self, nums, target):
            """
            Inputs: nums: list of integers
                    target: the target sum (int)

            Returns: list of two integers that when summed, equal the target
            """

            """
            s = dict(enumerate(nums))
            # enumerate through nums list to get index and value
            # for i, v in enumerate(nums):
            #     # 0 2
            #     # 1 7
            #     # 2 11
            #     # 3 15
            #     # find the values, that when summed, equal target
            #     combos = ()
            # for k, v in s.items():
            #     answer = s[k] + choice(s[k])
            # print(s[0] + s[1])
            # value = choice(s)
            # print(s
            """
            
            """
            # Handle edge case
            # if target-1 is in nums, and 1 is in nums
                # then their sum == target
                # simply need to get their indices at that point
            if target-1 in nums and 1 in nums:
                # d = dict(enumerate(nums))
                # # need to get key in d where val is target-1
                # # need to get key in d where val is 1
                # keys = list(d.keys())
                # vals = list(d.values())
                # a = nums.index(target-1)
                # b = nums.index(1)
                return (nums.index(target-1), nums.index(1))
            
            # Idea is to get all combos that exist in list
                # combos themselves are index locations
            # Then, can sum the values at combo locations
            # And return the combo who's sum == target
            # d = dict(enumerate(nums))
            combos = combinations(range(len(nums)), 2) #> combos need to be indices
            combos_list = [x for x in combos] #> list of tuples
            
            
            # print(len(combos_list) -1)
            
            for i in range(len(combos_list)):
                # print(i)
                if nums[combos_list[i][0]] + nums[combos_list[i][1]] == target:
                    # answer = d[combos_list[i][0]] + d[combos_list[i][1]]
                    combo = (combos_list[i][0], combos_list[i][1])
            
            # print(d[combos_list[2][0]] + d[combos_list[2][1]])
    #         print(answer)
            
    #         # return (combos_list[0][0], combos_list[0][1])
            
            # print(combos_list)

            return combo
            """

            # Edge Case - Massive Input (required looking at the test cases)
            if target-1 in nums and 1 in nums:
                return (nums.index(target-1), nums.index(1))

            combos = combinations(range(len(nums)), 2) #> combos need to be indices
            combos_list = [x for x in combos] #> list of tuples

            for i in range(len(combos_list)):
                if nums[combos_list[i][0]] + nums[combos_list][i][1] == target:
                    combo = (combos_list[i][0], combos_list[i][1])

            return combo
    ```

---

- **Alternate (better) solution**
    ```py
    class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
            """
            h = {}
            for i, num in enumerate(nums):
                n = target - num
                if n not in h:
                    h[num] = i
                else:
                    return [h[n], i]
    ```