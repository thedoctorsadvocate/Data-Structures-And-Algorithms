# Notes for my Contains Duplicate solution
#
#
#
# Given an integer array nums, return true if any value appears more than once and false if every element is distinct
# ie. 1231 should return True, 1234 should return False
#
#
#
# This intially seemed straight-forward enough
# for each number in nums, check if it exists in our list and if not add it
# If it's in the list already, we can return True
# If we exit the loop successfully without hitting the return conditional, return False
#
#
#
# However, I found that utilizing a list in this case was suboptimal as the list iteration has an O(n) complexity
# I got a time limit exception for a long nums array that had no duplicates
# It was determined quickly to instead use a set data structure instead as they use a hash algorithm, do not allow duplicates, and have an O(1) complexity


# Here is the slower solution using a list

def containsDupeList(nums: list[int]) -> bool:
    l = []

    for n in nums:
        if n in l:
            return True
        l.append(n)
        
    return False


# Here is the faster solution utilizng a set instead
# Notice that the only change made here was substituing l = [] and l.append with l = set() and l.add

def containsDupeSet(nums: list[int]) -> bool:
    l = set()

    for n in nums:
        if n in l:
            return True
        l.add(n)
        
    return False

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 20, 22, 2]
    print(containsDupeList(nums))
    print(containsDupeSet(nums))