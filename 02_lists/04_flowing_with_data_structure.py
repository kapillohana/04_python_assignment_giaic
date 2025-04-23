def add_three_copies(target_list, data):
    """
    Adds three copies of the data to the target list.
    Modifies the list in place (mutates it).
    
    Args:
        target_list (list): The list to modify
        data: The data to add three copies of
    """
    target_list.append(data)
    target_list.append(data)
    target_list.append(data)

# Example usage
if __name__ == '__main__':
    my_list = []
    message = input("Enter a message to copy: ")
    
    print(f"List before: {my_list}")
    add_three_copies(my_list, message)
    print(f"List after: {my_list}")