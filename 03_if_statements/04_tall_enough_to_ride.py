MIN_HEIGHT = 50  # Minimum height requirement in chosen units

def tall_enough():
    """Basic version that checks height once"""
    height = float(input("How tall are you? "))
    if height >= MIN_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")

def tall_enough_extension():
    """Extended version that checks repeatedly until empty input"""
    while True:
        height_input = input("How tall are you? ")
        if height_input == "":  # Exit if user just presses Enter
            break
        try:
            height = float(height_input)
            if height >= MIN_HEIGHT:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")
        except ValueError:
            print("Please enter a valid number or press Enter to quit.")

def main():
    print("Basic version:")
    tall_enough()
    
    print("\nExtended version (press Enter to quit):")
    tall_enough_extension()

if __name__ == '__main__':
    main()