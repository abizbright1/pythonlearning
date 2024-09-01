# use list to convert tuple and also use tuple to convert list to tuple

nur_tuple = (300, 400, 500, 600, 990)



def tuple_update_element():
    global nur_tuple
    nur_list = list(nur_tuple)
    nur_list[1] = 4
    nur_tuple = tuple(nur_list)
    return nur_tuple

def delete_element():
    global nur_tuple
    nur_list = list(nur_tuple)
    nur_list.remove(600)
    nur_tuple = tuple(nur_list)
    return nur_tuple


def add_element():
    global nur_tuple
    nur_list = list(nur_tuple)
    nur_list.append(877)
    nur_tuple = tuple(nur_list)
    return nur_tuple



print(tuple_update_element())
print( delete_element())
print( add_element())


account=


