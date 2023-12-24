def isPalindrome(string: str) -> bool:
    length=len(string)
    if length==0 or length==1:
        return True
    elif string[0]!=string[length-1]:
        return False
    return isPalindrome(string[1:length-1])

string=input("Enter a string: ")
print(isPalindrome(string))