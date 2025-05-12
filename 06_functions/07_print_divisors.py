def print_divisors(num: int):
    """Print all divisors of a given number."""
    divisors = [str(i) for i in range(1, num + 1) if num % i == 0]
    print(f"Here are the divisors of {num} : {' '.join(divisors)}")

def main():
    try:
        num = int(input("Enter a number: "))
        print_divisors(num)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == '__main__':
    main()