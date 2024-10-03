# Notes for my Longest Substring Without Repeating Characters solution
#
#
#
# Given a string of s, find and return the longest substring without repeating characters
# ie. abcabcbb should return 3 as the longest length is abc
#
#
#
# My initial thought was to use a for loop and a while loop
# while the next character was not repeated, continue checking next characters
# In the outer for loop, iterating through the characters of the string


# Here is the slower solution utilizing two loops in order to iterate through the string


def lengthOfLongestSubstring(s: str) -> int:
    # initiate a max of zero as the string could be empty
    max = 0

    for a in range(len(s)):
        # each time we go through a character in the string, append it to another string. We will use this to reset and check lengths later
        substring = s[a]

        # a right pointer to iterate through the next characters in the string
        r = a + 1

        while r < len(s):
            # while the right pointer is within bounds of the length of the string, we will iterate through checing if that character exists in the substring
            if s[r] in substring:
                # If the character is in the substring, we will exit the loop and figure out the length, if not then we add the character to the substring and continue on
                break   
            substring += s[r] 
                
            r += 1
        
        # Get the length and store it. Each time checking the new length against our max
        if len(substring) > max:
            max = len(substring)
        
    return max
    


def lengthOptimized(s: str) -> int:
    # In this solution we will initiate a left pointer value, a list to store the characters (to easily manipulate them), as well as initate the max length to 0
    left_pointer = 0
    substring = []
    max_length = 0

    for right_pointer in range(len(s)):
        # Same for loop as above, this time using it as our right pointer value

        while s[right_pointer] in substring:
            # If the right pointer character is in the substring, then we will remove the left pointer value and increment the left pointer by one
            substring.remove(s[left_pointer])
            left_pointer += 1
        
        # If the right is not in the substring, then we'll go ahead and add it in there
        substring.append(s[right_pointer])

        # Get the length and store it. Each time checking the new length against our max
        # the MAX function simply returns whichever value of the two inputs is greater
        max_length = max(max_length, right_pointer - left_pointer + 1)
        
    return max_length

if __name__ == '__main__':
    print(lengthOfLongestSubstring("pwwkew"))
    print(lengthOptimized("pwwkew"))