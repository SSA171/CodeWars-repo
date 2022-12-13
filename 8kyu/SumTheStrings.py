def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))

def main():
    while True:
        a = input("Enter input: ")
        b = input("Enter input: ")
        print(sum_str(a,b))

        if input("Do You Want To Continue [y/n] ? ") != "y":
            break

if __name__ == '__main__':
    main()
