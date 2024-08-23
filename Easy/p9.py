testTrue = 12234543221
testFalse = 12

print(testTrue % 10)

def isPalindrome(x: int) -> bool:
    myX = x
    digits = []
    while (myX != 0):
        remainder = myX % 10
        myX = myX // 10
        digits.append(remainder)
    
    isTrue = True
    for i in range(len(digits)//2):
        if (digits[i] != digits[-(i+1)]):
            return False
        else:
            continue
    
    return isTrue

print(f"{testTrue} is a palindrome : {isPalindrome(testTrue)}")
print(f"{testFalse} is a palindrome : {isPalindrome(testFalse)}")
print(f"{-101} is a palindrome : {isPalindrome(-101)}")