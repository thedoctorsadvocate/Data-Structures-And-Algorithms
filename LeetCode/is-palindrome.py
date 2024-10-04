# Notes for my Valid Palindrome solution
#
#
#
# Given a string, determine if the string is a palindrome (where a palindrome is a string that reads the same forwards as it does backwards)
# ie. "racecar" should return true, "a man, a plan, a canal: panama" should also return true, but "a racecar" should return false
#
#
#
# This intially seemed straight-forward enough
# First thing we need to do is remove any blank spaces as well as lowercase the entire string
# Second thing I iterated through a loop to add the letters (if they were alphanumeric only) to a new string
# Third I iterated through another loop to check indices of the string forwards and backwards and compared them
# This solution worked, but was suboptimal
#
#
#
# My optimized solution uses two pointers, one at the beginning of the string and one at the end
# While the left pointer is less than the right and the values are alpha numeric, I check the lowercased instance of the character and compare it to the left and right
# Regardless of the punctuation and spacing, this gives us the same positional character and allows us to compare without needing to remove the excess from the string


# Here is the slower solution

def isPalindrome(s: str) -> bool:
    # Create a new string to store the alphanumeric values only
    newStr = ""
    # Remove whitespaces and lowercase the entire string
    s = s.strip().lower()

    for letter in s:
        # For each letter, if the letter is an alpha numeric, add it to our new string
        if letter.isalnum():
            newStr += letter
    
    length = len(newStr)

    for letter in range(length):
        # For each letter in the range of the length of our new condesed string, check if that letter matches the letter on the other end of the string
        if newStr[letter] != newStr[length - letter - 1]:
            # If ever there is no match, we can return false
            return False
    
    # If we execute the loop without reaching our return, then we have a palindrome
    return True

# Here is my optimized solution
# This utilizes a pointer at the beginning and end and has a case to pass over spaces and punctuation

def isPalindromeOptimized(s: str) -> bool:
    # Left Pointer at the 0 index and the Right Pointer at the index of the end of the string
    lPointer = 0
    rPointer = len(s) - 1

    while lPointer < rPointer:
        # While the left does not pass the right pointer index value

        while lPointer < rPointer and not s[lPointer].isalnum():
            # Check if the left pointer is an alphanumeric or not, if it is we will add 1 to that pointer
            lPointer += 1
        while lPointer < rPointer and not s[rPointer].isalnum():
            # Check if the right pointer is an alphanumeric or not, if it is we will minus 1 to that pointer
            rPointer -= 1
            
        if s[lPointer].lower() != s[rPointer].lower():
            # If ever the left pointer value and the right pointer value do not match, we can return false
            return False
        
        # Remember to increment the pointers to iterate through the string
        lPointer += 1
        rPointer -= 1
    
    # If we exit the loop without hitting the return conditional, we can say we have a palindrome
    return True


if __name__ == '__main__':
    print(isPalindrome("A man, a plan, a canal: Panama"))
    print(isPalindromeOptimized("A man, a plan, a canal: Panama"))