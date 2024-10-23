str1 = 'prajun4 my1 name2 is3'
l = str1.split(' ')
l2 = [None for x in range(len(l))]
for i in l:
    l2[int(i[-1])-1] = i[:-1]
print(' '.join(l2))
