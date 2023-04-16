
# function takes as parameter the number of times the cube has been cut. You must return the number of smaller cubes created by the cuts that have at least one red face.

# Path: 8kyu\CountTheCubes.py

def count_squares(cuts):
    return 6*(cuts + 1)**2 - 12*(cuts - 1) - 16

def main():
    while True:
        try:
            #put code here that we suspect may cause an error to occur
            n = float(input("Enter input: "))
            print(count_squares(n))
        except KeyError:
            #put code here that will gracefully deal with the error
            print('You have tried to access an item that does not exist in the dictionary')
        if input("Do You Want To Continue [y/n] ? ") != "y":
            break

if __name__ == '__main__':
    main()
