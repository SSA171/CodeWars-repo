def longest(a1, a2):
    letters = "abcdefghijklmnopqrstuvwxyz"
    x = a1 + a2
    string = ''
    for i in letters:
        if i in x:
            string += i
    return string

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"

print(longest(a, b))