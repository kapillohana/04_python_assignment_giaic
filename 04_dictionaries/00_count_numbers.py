def get_user_numbers():
    """
    Collect numbers from user input until a blank line is entered.
    Returns a list of integers.
    """
    user_numbers = []
    while True:
        user_input = input("Enter a number: ").strip()
        
        if user_input == "":
            break
            
        try:
            num = int(user_input)
            user_numbers.append(num)
        except ValueError:
            print("Please enter a valid number or press Enter to finish.")
    
    return user_numbers

def count_nums(num_lst):
    """
    Count occurrences of each number in the list.
    Returns a dictionary with numbers as keys and counts as values.
    """
    num_dict = {}
    for num in num_lst:
        num_dict[num] = num_dict.get(num, 0) + 1
    return num_dict

def print_counts(num_dict):
    """
    Print the count for each number in a readable format.
    """
    for num in sorted(num_dict):
        print(f"{num} appears {num_dict[num]} time{'s' if num_dict[num] != 1 else ''}.")

def main():
    """
    Main program flow: get numbers, count them, and print results.
    """
    print("Enter numbers one at a time. Press Enter on an empty line to finish.")
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)

if __name__ == '__main__':
    main()