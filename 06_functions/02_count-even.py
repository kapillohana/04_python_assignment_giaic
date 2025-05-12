def count_even(lst):

    # Counts and prints the number of even integers in a list.
    
    
    count = 0
    for num in lst:
        if num % 2 == 0:  # Check if number is even
            count += 1
    print(count)

def get_list_of_ints():
    """
    Collects integers from user until empty input is received.
    
    Returns:
        List of integers entered by user
    """
    lst = []
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break
        try:
            lst.append(int(user_input))
        except ValueError:
            print("Please enter a valid integer or press enter to stop.")
    return lst

def main():
    """
    Main program flow:
    1. Gets list of integers from user
    2. Counts even numbers in the list
    3. Prints the count
    """
    print("Even Number Counter")
    print("-------------------")
    numbers = get_list_of_ints()
    print("\nNumber of even numbers:", end=" ")
    count_even(numbers)

if __name__ == '__main__':
    main()