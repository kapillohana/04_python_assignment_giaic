def main():
    # prmopt the user to enter the number of feet
    feet = float(input("Enter the measurement in feet: "))

    # convert the feet into incches (1 foot = 12 inches)
    inches = feet * 12

    print (f"{feet} feet is equal to {inches} inches")

if __name__ == '__main__':
    main()