def other_angle(a, b):
    return round(180 - (a + b))

def main():
    while True:
        a = float(input("Enter input: "))
        b = float(input("Enter input: "))
        print(other_angle(a,b))
        if input("Do You Want To Continue [y/n] ? ") != "y":
            break

if __name__ == '__main__':
    main()
