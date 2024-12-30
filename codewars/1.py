#given a number, square its ech digit and concatenate the result
def square_digits(num):
    return ''.join([str(int(i)**2) for i in str(num)])

print(square_digits(9841)) #81-64-16-1
print(square_digits(9842341)) #81-64-16-4-9-16-1