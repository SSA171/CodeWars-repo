def find_multiples(integer, limit):
    multiplies = []
    for num in range(integer, limit+1, integer):
        multiplies.append(num)
    return multiplies





def main():
    print(find_multiples(5, 25))

if __name__ == "__main__":
    main()