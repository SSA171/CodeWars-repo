def find_difference(a, b):
    return abs(a[0] * a[1] * a[2] - b[0] * b[1] * b[2])

def main():
    while True:
        c1 = input("Enter 3 positive integers for the first cuboid: ").split()
        a = [float(x) for x in c1]
        c2 = input("Enter 3 positive integers for the second cuboid: ").split()
        b = [float(x) for x in c2]

        print(find_difference(a, b))
        if input("Do You Want To Continue [y/n] ? ") != "y":
            break

if __name__ == '__main__':
    main()
