MAX_LENGTH = 3  # Constant defining the maximum allowed length

def shorten(lst):
    """
    Removes elements from the end of lst until it's MAX_LENGTH items long.
    Prints each removed item.
    Does nothing if lst is already <= MAX_LENGTH.
    """
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()  # Remove and get the last element
        print(removed_item)

# There is no need to edit code beyond this point
def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()
    shorten(lst)
    print("Final list:", lst)

if __name__ == '__main__':
    main()