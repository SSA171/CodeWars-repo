# inverts the value of the list
def invert(lst):
    return [-x for x in lst]

def main():
    print(invert([1,2,3,4,5]))
    print(invert([-1,-2,-3,-4,-5]))

if __name__ == "__main__":
    main()