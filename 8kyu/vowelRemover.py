n = ['a','e','i','o','u']
s = ("hello world")
new = []
for i in s:
    if i not in n:
        print(i, end="")
