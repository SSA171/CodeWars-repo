def enough(cap, on, wait):
    return wait - (cap - on) if (cap - on) < wait else 0

def main():
    while True:
        try:
            #put code here that we suspect may cause an error to occur
            a = int(input("Enter cap: "))
            b = int(input("Enter on: "))
            c = int(input("Enter wait: "))
            print(enough(a,b,c))
        except KeyError:
            #put code here that will gracefully deal with the error
            print('You have tried to access an item that does not exist in the dictionary')
        if input("Do You Want To Continue [y/n] ? ") != "y":
            break

if __name__ == '__main__':
    main()
