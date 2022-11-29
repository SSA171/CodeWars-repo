# alter the case based on the case letter
def to_alternating_case(string):
    # storage for the alternating string
    alternating = "" 
    # traverse each letter on the string
    for i in tuple(string):
        # turns letter to lower if letter is upper
        if i.isupper():
            alternating += i.lower() 
        else:
        # turns letter to upper if letter is lower
            alternating += i.upper()
    # returns the alternating letter string to a joined string
    return ''.join(alternating)




def main():
    while True:
        n = input("Enter input: ")
        print(to_alternating_case(n))
        if input("Do You Want To Continue [y/n] ? ") != "y":
            break

if __name__ == '__main__':
    main()
