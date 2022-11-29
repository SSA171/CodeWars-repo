# module provides access to some objects used or maintained and to functions that interact with the interpreter
import sys 
# return the total byte size of the object. 
def total_bytes(object):
    # returns the size of the object in bytes
    return sys.getsizeof(object)

def main():
    print(total_bytes("hello"))
    print(total_bytes("Said"))
    print(total_bytes("Hannah"))
    print(total_bytes("Nasser"))

if __name__ == "__main__":
    main()