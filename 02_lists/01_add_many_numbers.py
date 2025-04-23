def add_many_numbers(numbers):
    """
    calculate the sum of numbers in list

    Args: a list of numebr to be summed

    Returns : float or int summed of numbers
    """ 

    total = 0 
    for num in numbers:
        total +=num
    return total

#example usage
if __name__ == '__main__':
    sample_list = [1,2,3,4,5,6]
    print (add_many_numbers(sample_list))

