def myfuction(): #parameter
    global c
    c= 7
    global d
    d= 8

c = 88
d = 99
#Arbitrary function
myfuction()
print(c, d)


def func(*kids):
    print(kids[0:3])
    print(kids[1])

func("nur", 'what do you', 'want') #