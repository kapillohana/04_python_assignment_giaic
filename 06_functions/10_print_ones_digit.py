def print_ones_digit(num: int) -> None:
    """Prints the ones digit of a given integer.
    
    Args:
        num: The integer whose ones digit will be printed
    """
    ones_digit = abs(num) % 10  # Handle negative numbers correctly
    print(f"The ones digit is {ones_digit}")

def main() -> None:
    """Main function that gets user input and calls print_ones_digit."""
    try:
        num = int(input("Enter a number: "))
        print_ones_digit(num)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == '__main__':
    main()