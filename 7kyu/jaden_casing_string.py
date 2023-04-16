def to_jaden_case(string):
    x = quote.split()
    list= ''
    for i in x:
            list += (i.capitalize()) + ' '
    return str(list.strip())


quote = "How can mirrors be real if our eyes aren't real"

print(to_jaden_case(quote))