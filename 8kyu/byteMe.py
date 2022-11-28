import sys 
# return the total byte size of the object. 
def total_bytes(object):
    return sys.getsizeof(object)

def main():
    print(total_bytes("hello"))

if __name__ == "__main__":
    main()