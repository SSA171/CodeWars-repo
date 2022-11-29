# returns how many times the integer can be multiplies to the limit
def find_multiples(integer, limit):
    # storage for multiplies list
    multiplies = []
    # traverse integer - limit, until limit is met.
    for num in range(integer, limit+1, integer):
        # adds integer to list, then increase integer + integer until hit limit value.
        multiplies.append(num)
    # returns the list of multiples
    return multiplies

def main():
    print(find_multiples(5, 55))

if __name__ == "__main__":
    main()