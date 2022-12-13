class Ship:
    def __init__(self, draft, crew):
        self.draft = draft # estimate of ship's weight
        self.crew = crew # count of crew on board, each crew adds 1.5 units to ship draft

    # if after removing the weight of the crew, the draft is sitll more then 20, then the ship is worth looting.
    def is_worth_it(self):
        draft = self. draft - (self.crew * 1.5)
        if draft > 20:
            return True
        else:
            return False

            
def main():
    while True:
        a = int(input("Enter a ship's draft: "))
        b = int(input("Enter a ship's crew: "))
        n = Ship(a,b)
        if input("Do You Want To Continue [y/n] ? ") != "y":
            break

if __name__ == '__main__':
    main()
