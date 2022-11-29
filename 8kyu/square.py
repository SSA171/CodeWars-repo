import math
def square(n):
    return math.pow(n,2)


def main():
    while True:
        n = input("Enter input: ")
        print(square(float(n)))
        if input("Do You Want To Continue [y/n] ? ") != "y":
            break

if __name__ == '__main__':
    main()
