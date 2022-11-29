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
    print(to_alternating_case("hello world"))
    print(to_alternating_case("HELLO WOlD"))
    print(to_alternating_case("hElLo WoRlD"))
    print(to_alternating_case("HeLlO wOrLd"))


if __name__ == "__main__":
    main()