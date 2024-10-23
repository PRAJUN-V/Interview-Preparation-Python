str1 = "wwokiohfhkklollol"

def is_palindrome(s):
    return s == s[::-1]

count = 0
length = len(str1)

# Iterate over all possible substrings
for i in range(length):
    for j in range(i + 1, length + 1):
        substring = str1[i:j]
        if is_palindrome(substring):
            count += 1

print("Total number of palindromes:", count)
