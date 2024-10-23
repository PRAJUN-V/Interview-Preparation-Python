# find total number of vowels in string list
from typing import List
def count_vowels(strings: List[str]) -> int:
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in strings:
        for j in i:
            if j.lower() in vowel_list:
                count += 1
    return count

input_list = ["hello", "world", "Python", "programming"]

print(count_vowels(input_list))
