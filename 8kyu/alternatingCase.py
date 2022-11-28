def to_alternating_case(string):
    alternating = ""
    for i in tuple(string):
        if i.isupper():
            alternating += i.lower()
        else:
            alternating += i.upper()
    return ''.join(alternating)

def main():
    print(to_alternating_case("hello world"))

if __name__ == "__main__":
    main()