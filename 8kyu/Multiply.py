def multi(a, b):
    return a * b


def main():
    while True:
        a = float(input("Enter input: "))
        b = float(input("Enter input: "))
        print(multi(a,b))
        if input("Do You Want To Continue [y/n] ? ") != "y":
            break

if __name__ == '__main__':
    main()
