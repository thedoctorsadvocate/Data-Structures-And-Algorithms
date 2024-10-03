# Notes for my Two Sum solution
#
#
#
# Given an array of integers, find and return the two integers indices that add up to a provided target
# ie. [1, 2, 3, 4, 5] target 8 should return [2. 4] (the indices of the correct sum values 5 and 3 = 8)
#
#
#
# Typically we would think to use a for loop within a for loop to comparethe remainder of the list to the current index to find the solution
# However, this causes our time complexity to shoot to O(n^2)
# We can use a hashmap to reduce this complexity even further to O(n) constant time


# Here is the slower solution utilizing two for loops in order to iterate through the list
# We may have made the solution slightly faster by using b in range a+1, however this is still O(n^2)

def twoSum(nums: list[int], target: int) -> list[int]:
    for a in range(len(nums)):
        for b in range(a+1, len(nums)):
            if nums[a] + nums[b] == target:
                return [a, b]

# Here is the faster solution utilizing one single for loop to iterate through the list
# We create a hashmap and find the complement (the value needed from the current index value in order to reach the target)
# Then if we find the complent inside of the dictionary, we can return that index value as well as the current index value we're on
# If we don't find it, we can just append the data we've found into the dictionary

def twoSumFaster(nums: list[int], target: int) -> list[int]:
    d = {}
    for a in range(len(nums)):
        complement = target - nums[a]

        if complement in d:
            return[d[complement], a]
        
        d[nums[a]] = a

            
if __name__ == '__main__':
    print(twoSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50], 99))
    print(twoSumFaster([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50], 99))