def remove_exclamation_marks(s):
    return ''.join([char for char in s if char != '!'])

def simple_multiplication(number) :
    return number * 9 if number % 2 else number * 8

#def funtion_name(parameter):
#    reutrn [(try to keep name of var same from the loop when filtering) (if/else condtion goes here) (then for loop) (and then filter goes here where we used if again to filter)]

# you can do this to further shorten the code when checking odd even number
# def simple_multiplication(number) :
#     return number * 9 if number % 2 else number * 8
#initially I worte like this
# def simple_multiplication(number) :
#     return number * 9 if number%2 == 0 else number * 8
#but you can drop == 0 and becareful because the if condition will receive 1 for odd before it receive 1 for even. 