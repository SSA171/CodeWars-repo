def better_than_average(class_points, your_points):
    return your_points > sum(class_points) / len(class_points)

def main():
    while True:
        try:
            #put code here that we suspect may cause an error to occur
            n = input("Enter input: ").split(",")
            a = [int(x) for x in n]
            b = int(input("Enter input: "))
            print(better_than_average(a,b))
        except KeyError:
            #put code here that will gracefully deal with the error
            print('You have tried to access an item that does not exist in the dictionary')
        if input("Do You Want To Continue [y/n] ? ") != "y":
            break

if __name__ == '__main__':
    main()
