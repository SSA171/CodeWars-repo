def square(n):
    return int(n)

def main():
    while True:
        n = float(input("Enter a string number: "))
        print(square(n))
        if input("Do You Want To Continue [y/n] ?") != "y":
            break

if __name__ == '__main__':
    main()
