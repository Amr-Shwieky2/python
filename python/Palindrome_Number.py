def palindrome(number):
    temp = str(number)
    rev_number = temp[::-1]
    return temp == rev_number

print(palindrome(121))
print(palindrome(12321))
print(palindrome(12345))