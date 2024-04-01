# 6 kyu
# Highest Perfect Square with Same Digits

# 100 <= lower_limit <= 1e6
# 2 <= k <= 5
# number of tests = 45
from math import *

# def square_number():
#     query_list = [num for num in range(0,100)]
#     return [num for num in query_list if sqrt(num) in query_list]
#     return [num for num in query_list if floor(sqrt(num))==ceil(sqrt(num))] optimized
    
# def square_number():
#     query_list = [num for num in range(100,10000) if '0' not in str(num)]
#     return [num for num in query_list if floor(sqrt(num))==ceil(sqrt(num))]

def square_generator():
    for num in range(10,100):
        if '0' not in str(num):
            yield num**2

print(list(square_generator()))

# def perfect_squares_generator():
#     for num in range(100, 10000):
#         if '0' not in str(num) and sqrt(num).is_integer():
#             yield num

#swapping the item
                
def square_and_swap_generator():
    for num in range(10, 100):
        if '0' not in str(num):
            square = num ** 2
            yield square
            num_str = str(square)
            for i in range(len(num_str) - 1):
                for j in range(i + 1, len(num_str)):
                    swapped_str = num_str[:i] + num_str[j] + num_str[i+1:j] + num_str[i] + num_str[j+1:]
                    yield int(swapped_str)

