# returns the mininum value in list
def minimum(arr):
    return min(arr)
# returns the maximum value in list
def maximum(arr):
    return max(arr)


def main():
    while True:
        n = input("enter an array of numbers from 0 to 9 [with a space between]: ").split()
        print(f"min number in array: {minimum(n)}")
        print(f"max number in array: {maximum(n)}")
        if input("Do You Want To Continue [y/n] ? ") != "y":
            break

if __name__ == '__main__':
    main()
