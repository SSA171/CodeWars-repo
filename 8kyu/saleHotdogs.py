def sale_hotdogs(n):
    if n < 5: return 100* n
    elif n >= 5 and n < 10: return 95 * n
    elif n >= 10: return 90 * n

def main():
    while True:
        n = input("Enter input: ")
        print(sale_hotdogs(float(n)))
        if input("Do You Want To Continue [y/n] ? ") != "y":
            break

if __name__ == '__main__':
    main()
