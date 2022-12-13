import operator 
def basic_op(operator, value1, value2):
    ops = { '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv}
    
    return ops[operator](value1,value2)

print(basic_op('+',3,5))