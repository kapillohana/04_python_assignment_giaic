def print_multiple(message: str, repeats: int):
    """Print the message the specified number of times."""
    for _ in range(repeats):
        print(message, end=' ')
    print()  # Add a newline at the end

def main():
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    print_multiple(message, repeats)

if __name__ == '__main__':
    main()