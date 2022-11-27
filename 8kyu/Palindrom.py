
# If the parameters passed are (2, 6), the function should return [2,4, 6] as 2, 4, and 6 ar the multiples of 2 up to 6.

def find(min, max):
    mult= []
    for i in range(min, max+1, min):
        mult.append(i)
    return mult


def main():
    print(find(5, 25))

if __name__ == "__main__":
    main()