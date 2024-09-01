# x = lambda a:a + 10

# print(x(5))
# a = int(input("what number do you want here:"))
# b = int(input("what number do you want here 2:"))
# c = int(input("what number do you want here 3:"))
# x = lambda a,b,c:a*b*c
#
# print(x(a,b,c))


def myfuncjtion(n):
    return lambda a:a + n
x = myfuncjtion(6)
print(x(5))

