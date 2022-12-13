def get_age(age):
    return int(age[0])
    
def main():
    while True:
        n = input("How old are you?: ")
        print(get_age(n))
        if input("Do You Want To Continue [y/n] ? ") != "y":
            break

if __name__ == '__main__':
    main()
