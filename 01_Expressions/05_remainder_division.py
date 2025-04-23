def main():
    # Get the two numbers from the user
    dividend = int(input("Please enter an integer to be divided: "))
    divisor = int(input("Please enter an integer to divided by: "))

    #calculate results
    quotient = dividend // divisor
    remainder = dividend % divisor

    # Print result
    print(f"The result of this division is {quotient} with a remainder of {remainder}")

if __name__ == '__main__':
    main()

