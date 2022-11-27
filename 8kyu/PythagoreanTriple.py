def pythagorean_triple(integers):
    a, b, c = sorted(integers)
    return a**2 + b**2 == c**2

def main():
    print(pythagorean_triple([3,4,5]))

if __name__ == "__main__":
    main()