#list_slicing application
def remove_every_other(my_list):
    return my_list[::3]

print(remove_every_other(['Hello', 'Good Night', 'Hello Again','Hello', 'Good Night', 'Hello Again','Hello', 'Good Night', 'Hello Again']))

# return my_list[1:6:2] it means [a:b:c] here a and b are same as before where it defines the slicing elements position
# c defines a jumps distance meaning it will ignore other elements and jump to +3 position

#my attempt
def remove_every_other(my_list):
    return [item for index,item in enumerate(my_list) if (index % 2) == 0]


