#use of eval function
def basic_op1(operator, value1, value2):
    return eval(str(value1) + operator + str(value2))

def basic_op2(operator, value1, value2):
    return eval("{}{}{}".format(value1, operator, value2))

# It's often recommended to avoid using eval() with user input unless absolutely necessary due to security risks.
