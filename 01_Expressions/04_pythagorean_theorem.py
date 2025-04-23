import math

def main():
    side_ab = float(input("Enter the length of AB: "))
    side_ac = float(input("Enter the length of AC: "))

    hypotenuse = math.sqrt(side_ab ** 2 + side_ac ** 2)
    print (f"The length of BC (The hypotenuse) is {hypotenuse}")

if __name__ == '__main__':
    main()
