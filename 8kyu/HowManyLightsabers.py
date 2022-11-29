
# If the name is Zach it wil return 18 anything else is 0 
def how_many_light_sabers_do_you_own(name=""):
    return (18 if name=="Zach" else 0)

def main():
    while True:
        n = input("How many light sabers do you own?: ")
        print(how_many_light_sabers_do_you_own(n))
        if input("Do You Want To Continue [y/n] ? ") != "y":
            break

if __name__ == '__main__':
    main()
