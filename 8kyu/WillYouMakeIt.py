def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg*fuel_left >= distance_to_pump
        
def main():
    while True:
        d = int(input("Enter the distance: "))
        m = int(input("Enter the miles: "))
        f = int(input("Enter fuel left: "))
        print(zero_fuel(d,m,f))
        if input("Do You Want To Continue [y/n] ? ") != "y":
            break

if __name__ == '__main__':
    main()


#zero_fuel(50, 25, 2)
#zero_fuel(100, 50, 1)