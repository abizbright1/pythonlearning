my_set ={1,2,3,12,1,2,1,21,21,21,2,1323,2324,454,5,46,443,'what are you saying'}
set1 = {48,9,9,2,3,4,5,6,7,7,3,1,3343,4,3,43,4,3}
set3 = set1 and my_set
print(my_set)
print(len(my_set))

# for x in my_set:
#     print(x)
# #lis1 = list(my_set)
# # print(lis1)
#
# # my_set.add(299)
# # print(my_set)
# # my_set.remove(454)
# # print(my_set)
# #
# # set1.update(my_set)
# # print(set1)
# # print(my_set)
#
# set3.update(set1)# to add set1 into set3
#
# my_set.discard(2)# doesnt give any error but can be used tot remove a specific element
# print(my_set)
# my_set.remove(12)# it showa\s error when you remove an element not in the set and tis can be used to remove a specific elemet
# print(my_set)
# # it is used to empty the set but keeps it empty
# # set1.clear()
# # print(set1)
# #del set1# this is used to delete everything on about the set
# print(set1)
# set4 = set1.union(my_set) # union is used to add the other set into the other and creating a new set, the other set can be added into the other sets.
#
# print(set4)
# #operator | or union
# set5= my_set | set1# this works with just sets
# print(set5)
#
# set6 = my_set.intersection(set1)# to find the point of intersections
# print(set6)
# my_set.intersection_update(set1)# this only update the contents of interception into the my_set
# print(my_set)
# my_set3 = my_set.difference(set6) # this reomves the interceptions of my_set in set6
# print(my_set)
# #note when you use operators it has to be set files to set files but when you use words it can to be with any other element typew
# my_set3.difference_update(set1)
print(my_set)

my_set.symmetric_difference_update(set1)
print(my_set)
# union operator creates new file
#update works with the existing files


