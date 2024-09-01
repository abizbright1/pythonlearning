# use list to convert tuple and also use tuple to convert list to tuple

nur_tuple = (300,400,500,600,990)
nur_list = list(nur_tuple)
print(nur_list)
nur_list[0]=3
print(nur_list)
nur_tuple = tuple(nur_list)
print(nur_tuple)

def tuple_update_element():
    nur_tuple = list(nur_list)

    return nur_tuple
tuple_update_element()