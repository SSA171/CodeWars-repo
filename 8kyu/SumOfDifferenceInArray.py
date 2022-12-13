def sum_of_differences(arr):
    if len(arr) == 0:
        return 0

    # Find the maximum and minimum values in the list
    maximum = max(arr)
    minimum = min(arr)

    # Calculate the sum of the differences
    s = maximum - minimum
    return s

def main():
    while True:
        n = input("Enter a list of array: ").split(",")
        print(sum_of_differences(n))
        if input("Do You Want To Continue [y/n] ? ") != "y":
            break

if __name__ == '__main__':
    main()
