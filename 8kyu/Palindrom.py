def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]


def main():
    while True:
        n = input("Enter a string: ")
        print(is_palindrome(n))
        if input("Do You Want To Continue [y/n] ? ") != "y":
            break

if __name__ == '__main__':
    main()
