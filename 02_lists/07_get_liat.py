def main():
    values = []  # Start with an empty list
    
    while True:
        user_input = input("Enter a value: ")  # Ask for input
        if user_input == "":  # If user just presses Enter (empty string)
            break  # Exit the loop
        values.append(user_input)  # Add the value to our list
    
    print("Here's the list:", values)  # Print the final list

if __name__ == '__main__':
    main()