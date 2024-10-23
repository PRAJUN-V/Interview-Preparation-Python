# first 100 prime numbers

def is_prime(num):
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

l = []
num = 2
count = 0
while count < 100:
    if is_prime(num):
        l.append(num)
        count += 1
    num += 1


print(l)
print(len(l))
