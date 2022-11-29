# module provides access to some objects used or maintained and to functions that interact with the interpreter
import sys 
# return the total byte size of the object. 
def total_bytes(object):
    # returns the size of the object in bytes
    return sys.getsizeof(object)


def main():
    while True:
        n = input("Enter input: ")
        print(total_bytes(n))
        if input("Do You Want To Continue [y/n] ? ") != "y":
            break

if __name__ == '__main__':
    main()

