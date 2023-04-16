def alphabet_position(text):
    text = text.lower()
    char = 'abcdefghijklmnopqrstuvwxyz'
    replace= ''
    for i in text:
        if i in char:
            replace +=str(ord(i)- 96) + ' '
    return replace.strip()

print(alphabet_position("The sunset sets at twelve o' clock."))