
my_number=1234567890
mymap_nu = {}

while my_number > 0:
    reminder = my_number % 10
    if reminder not in mymap_nu:
        mymap_nu[reminder]=1
    else:
        mymap_nu[reminder] += 1
    my_number=my_number // 10
print(mymap_nu)