list=[100,200,300,400]

def funct(list2):
    index = 0
    sum1 = 0
    while index < len(list2):

        sum1 = sum1 + (list2[index])

        index += 1
    return sum1

print(funct(list))

name = input("what is your name: ")
univesity = input("what is the name of your univeristy:")

def univs():
    global univesity
    univesity  = "grambling"
    return univesity

print(univs())
print(univesity)