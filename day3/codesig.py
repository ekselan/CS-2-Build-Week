# Code Signal Unit Assessment

# Prompt 1: (condesed linked list)
"""
Given a linked list of integers, remove any nodes from the linked list that have values that have previously occurred in the linked list. Your function should return a reference to the head of the updated linked list.

Example:
Input: (3) -> (4) -> (3) -> (2) -> (6) -> (1) -> (2) -> (6) -> N
Output: (3) -> (4) -> (2) -> (6) -> (1) -> N
Explanation: The input list contains redundant nodes (3), (6), and (2), so those should be removed from the list.

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer node

The head node of the linked list.

[output] linkedlist.integer

The head node of the updated linked list.
"""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#


def condense_linked_list(node):
    # x = ListNode() #> Must init with a value

    # First through is to use simple arrays
    # print(type(node)) #> class ListNode
    # print(node) #> ListNode object (does not print out an array
    # First thought will not work, "traversing" LL will be necessary

    # # Init an empty linked list
    # ll = ListNode()

    new_list = []

    # For traversal, start with head node
    cur = node

    while cur.next:
        # print(cur.value)
        if cur.value not in new_list:
            new_list.append(cur.value)
            cur = cur.next
        else:
            cur = cur.next

    # print("Last Node Value:", cur.value)
    # add last value
    if cur.value not in new_list:
        new_list.append(cur.value)

    # print(new_list)

    # At this point, new_list is an array that matches order and vals of expected output
    # Now, need to convert this array into linked list

    # Added helper functions to add nodes and convert array to linked list

    def add_node(root, val):
        temp = ListNode(val)

        if root is None:
            root = temp

        else:
            pointer = root
            while pointer.next is not None:
                pointer = pointer.next
            pointer.next = temp

        return root

    def arr_to_ll(arr, n):
        root = None
        for i in range(0, n):
            root = add_node(root, arr[i])

        return root

        # if not ll.next:
        #     ll.next = val
        #     return ll
        # return add_node(ll.next, val)

    # for x, y in enumerate(new_list): #> x is indices, y is value
    #     if x == 0: #> if it's first item in list, create new ll
    #         ll = ListNode(y)
    #     # otherwise, value is coming after ll has been created, so should be able to just add a next
    #     # print(type(ll))
    #     print(ll.next)
    #     add_node(ll, y)

    n = len(new_list)
    ll = arr_to_ll(new_list, n)

    return ll


# Prompt 2: (tree paths sum) (incomplete)
"""
Given the root of a binary tree where each node contains an integer, determine the sum of all of the integer values in the tree.

Example:

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
The expected output given the above tree is 5 + 4 + 8 + 11 + 13 + 4 + 7 + 2 + 1, so your function should return 55.

[execution time limit] 4 seconds (py3)

[input] tree.integer root

Root node of a binary tree of integers.

[output] integer

The sum of all of the integers in the tree.
"""
#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None


def tree_paths_sum(root):

    # What I'll need to do is traverse the tree, keep track of all ints, and
    # then sum them

    vals = []

    cur = root

    # if there's no child nodes, just return root value
    if not cur.left and not cur.right:
        return root.value

    # # otherwise, there are child nodes

    # def get_vals(root):
    #     vals = []
    #     pointer = root
    #     vals.append(pointer.value) #> start by adding root val to the list
    #     # if left child
    #     if pointer.left


# Prompt 3: (uncover spy)

"""
In a city-state of n people, there is a rumor going around that one of the n people is a spy for the neighboring city-state.

The spy, if it exists:

Does not trust anyone else.
Is trusted by everyone else (he's good at his job).
Works alone; there are no other spies in the city-state.
You are given a list of pairs, trust. Each trust[i] = [a, b] represents the fact that person a trusts person b.

If the spy exists and can be found, return their identifier. Otherwise, return -1.

Example 1:

Input: n = 2, trust = [[1, 2]]
Output: 2
Explanation: Person 1 trusts Person 2, but Person 2 does not trust Person 1, so Person 2 is the spy.
Example 2:

Input: n = 3, trust = [[1, 3], [2, 3]]
Output: 3
Explanation: Person 1 trusts Person 3, and Person 2 trusts Person 3, but Person 3 does not trust either Person 1 or Person 2. Thus, Person 3 is the spy.
Example 3:

Input: n = 3, trust = [[1, 3], [2, 3], [3, 1]]
Output: -1
Explanation: Person 1 trusts Person 3, Person 2 trusts Person 3, and Person 3 trusts Person 1. Since everyone trusts at least one other person, there is no spy.
Example 4:

Input: n = 3, trust = [[1, 2], [2, 3]]
Output: -1
Explanation: Person 1 trusts Person 2, and Person 2 trusts Person 3. However, in this situation, we don't have any one person who is trusted by everyone else. So we can't determine who the spy is in this case.
Example 5:

Input: n = 4, trust = [[1, 3],[1, 4],[2, 3],[2, 4],[4, 3]]
Output: 3
Explanation: Person 1 trusts Person 3 and Person 4, Person 2 trusts Person 3 and Person 4, Person 4 trusts Person 3. Everyone trusts Person 3 but Person 3 does not trust anyone, so they are the spy.

[execution time limit] 4 seconds (py3)

[input] integer n

The number of people in the city-state

[input] array.array.integer trust

Array of pairs indicating who each person in trusts.

[output] integer

The identifier of the spy.
"""


def uncover_spy(n, trust):
    # Can possibly use cache to hold the first item from each pair in the array
    # For the second item in each pair, add it to the first item's position in cache
    # If there is an item in cache that has no items added to it, it's a spy
    # But for this to be true, that item must be "trusted" by everyone else

    fp_cache = {}  # > first position in pairs
    sp_cache = {}  # > second position in pairs

    for pairs in trust:
        # print(pairs) -> [1,2], [3,4], [5,6]
        # Add first item of each pair to cache
        if pairs[0] not in fp_cache:
            # > init with list holding 2nd val in pair
            fp_cache[pairs[0]] = [pairs[1]]

        if pairs[1] not in sp_cache:
            # init with a "counter" of 1 (assume each person trust themselves)
            sp_cache[pairs[1]] = 1
            sp_cache[pairs[1]] += 1  # val has been seen, so increase "counter"

        else:
            # if it's already in cache and we see it again, add whatever new
            # 2nd item to list
            fp_cache[pairs[0]].append(pairs[1])
            # for sp cache, increase counter
            sp_cache[pairs[1]] += 1

    # print("FP CACHE:", fp_cache)
    # print("SP CACHE:", sp_cache)

    # now, can run a check to see if counter val for any key in sp_cache == n
    # is n in sp_cache values?
    if n in sp_cache.values():
        # if it's in there, then I want the key who's value == n
        suspect = [k for k in sp_cache.keys() if sp_cache[k] == n]
        suspect = suspect[0]  # unpack suspect

        # now that there's a suspect, see if the suspect trusts anyone else (suspect in fp_cache?)
        # is suspect in fp_cache keys?
        if suspect in fp_cache.keys():
            # if suspect trusts someone, then we have no spies
            return -1
        else:
            # if suspect trusts no one but themselves, then suspect is spy
            return suspect

    else:
        # if n is not in sp_cache values, then there is no suspect
        return -1

    # print("SUSPECT:", suspect)
