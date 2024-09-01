class student:
    latech = " welcome to our university"
    print(latech)
    def __init__(self,name,roll_no,university,lectuer):
        self.name = name
        self.roll = roll_no
        self.university = university
        self.lectuer = lectuer
s1 = student("Nur",30,"latech","pradeep")
s2 = student('brigh',90,'grambling', 'glisson',)
print(s2.lectuer)
