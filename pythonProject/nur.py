class students:
    university = "latech"
    state = "louisiana"
    def __init__(self, name, id, max1, max2,max3, max4):


        self.name = name
        self.id = id
        self.max1 = max1
        self.max2 = max2
        self.max3 = max3
        self.max4 =max4

    def myfuntion(self):
        sum1 = (self.max3 + self.max2 + self.max1)/3
        return sum1
    def update(self,newUni):
        students.universitjfdjjrsjdjgjgjy=newUni



s1 = students("Nur", 23, 22,33,88)
s1.update("Standford")
s2 = students("sharkor", 455,55,4,44)
s2.update("grabmling")

print(s1.name,students.university,"in the state of ", s1.state, "got",int(s1.myfuntion()),"%")
print(s2.name,students.university,"in the state of ", s2.state, "got",int(s2.myfuntion()),"%")
print("you pussy")
print(s2.name,students.university,"in the state of ", s2.state, "got",int(s2.myfuntion()),"%")
print("you pussy")