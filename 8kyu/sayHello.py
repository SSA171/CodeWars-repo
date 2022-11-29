def say_hello(name):
    return f"Hello, {name}"

def main():
    while True:
        n = input("Enter input: ")
        print(say_hello(n))
        if input("Do You Want To Continue [y/n] ? ") != "y":
            break

if __name__ == '__main__':
    main()
