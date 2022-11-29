# inverts the value of the list
def invert(lst):
    return [-x for x in lst]

def main():
    while True:
        n = input("Enter input: ").split()
        f = [float(x) for x in n]
        print(invert(f))
        if input("Do You Want To Continue [y/n] ? ") != "y":
            break

if __name__ == '__main__':
    main()
