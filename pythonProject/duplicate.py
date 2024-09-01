

def my_duplicate_function(list1):
    my_set=set()
    for x in list1:
        if x in my_set:
            return True
        else:
            my_set.add(x)

    return False
my_list =[1,2,3,]
print(my_duplicate_function(my_list))

