# LeetCode 3, palindrome checking 

def isPalindrome(input):
    reversed = str(input)[::-1]
    return reversed == str(input)


print(isPalindrome(-121))