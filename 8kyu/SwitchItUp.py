def switch_it_up(number):
    n = {0:"Zero",1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"}
    return str(n[number])

def main():
    while True:
        number = int(input("Enter input: "))
        print(switch_it_up(number))
        if input("Do You Want To Continue [y/n] ? ") != "y":
            break

if __name__ == '__main__':
    main()
