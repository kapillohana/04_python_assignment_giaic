def Averages(a:float, b:float) -> float:
    return (a + b) / 2

def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = Averages(num1, num2)

    print (f"The average of {num1} and {num2} is {result}")


if __name__ == '__main__':
    main()