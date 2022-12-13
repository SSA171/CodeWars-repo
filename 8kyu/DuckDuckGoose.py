def duck_duck_goose(players, goose):
    while len(players) < goose:
        goose = goose - len(players)
    return players[goose - 1].name

def main():
    while True:
        a = input("Enter input: ").split(",")
        b = int(input("Enter input: "))
        print(duck_duck_goose(a,b))
        if input("Do You Want To Continue [y/n] ? ") != "y":
            break

if __name__ == '__main__':
    main()
