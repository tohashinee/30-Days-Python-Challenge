# Check for Palindrome
text = input("Enter String: ")
length = len(text)
isPalindrome = True
end = length//2
for i in range(end):
    if text[i] != text[-(i+1)]:
        isPalindrome = False
next
if isPalindrome:
    print(text+ " is a palindrome.")
else:
    print(text+" is not a palindrome.")
    
        
