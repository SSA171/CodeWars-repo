
# If the name is Zach it wil return 18 anything else is 0 
def how_many_light_sabers_do_you_own(name=""):
    return (18 if name=="Zach" else 0)

def main():
    print(how_many_light_sabers_do_you_own("Zach"))
    print(how_many_light_sabers_do_you_own("Baki"))
    print(how_many_light_sabers_do_you_own("Said"))
    print(how_many_light_sabers_do_you_own("Hannah"))

if __name__ == "__main__":
    main()