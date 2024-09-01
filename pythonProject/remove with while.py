l2 = [2,0,0,0,3,9,5,0,0,6]
index = l2[0]
while index < len(l2):
    if l2[index] == 0:
        l2.remove(l2[index])
    else:
        index += 1

print(l2)