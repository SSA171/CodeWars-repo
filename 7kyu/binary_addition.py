def add_binary(a,b):
    c=a+b
    x = bin(c)
    return x[2:]

print(add_binary(51,12))