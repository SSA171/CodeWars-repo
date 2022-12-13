def bmi(weight, height):
    bmi = weight/height ** 2
    if bmi <= 18.5: return "Underweight"
    if bmi <= 25.0: return "Normal"
    if bmi <= 30.0: return "Overweight"
    if bmi > 30: return "Obese"


def main():
    while True:
        weight = float(input("Enter weight: "))
        height = float(input("Enter height: "))
        print(bmi(weight, height))
        if input("Do You Want To Continue [y/n] ? ") != "y":
            break

if __name__ == '__main__':
    main()
