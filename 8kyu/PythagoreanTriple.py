def pythagorean_triple(integers):
    a, b, c = sorted(integers)
    return a**2 + b**2 == c**2

def main():
    while True:
        n = input("Enter three pythagorean values [seperate with space between]: ").split()
        f = [float(x) for x in n]
        print(pythagorean_triple(f))
        if input("Do You Want To Continue [y/n] ? ") != "y":
            break

if __name__ == '__main__':
    main()
1,2