def grow(arr):
    res = 1
    for i in arr:
        res = res * i
    return res


def main():
    while True:
        n = input("Enter input: ").split(",")
        f = [float(x) for x in n]
        print(grow(f))
        if input("Do You Want To Continue [y/n] ? ") != "y":
            break

if __name__ == '__main__':
    main()
