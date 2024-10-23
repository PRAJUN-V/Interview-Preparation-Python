# Longest consecutive subsequence from string

str1 = 'abcdpqrstabcdefghiwxyz'
l = len(str1)
temp_string = ''
long_string = ''
for i in range(1, l):
    if ord(str1[i]) == ord(str1[i-1]) + 1:
        if temp_string == '':
            temp_string = str1[i-1] + str1[i]
        else:
            temp_string += str1[i]
    else:
        if len(temp_string) > len(long_string):
            long_string = temp_string
        temp_string = ''

print(long_string)

