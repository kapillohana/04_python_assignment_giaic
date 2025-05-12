MAX_VALUE = 10000  # Constant for maximum Fibonacci number

def print_fibonacci_sequence():
    """Prints Fibonacci sequence up to MAX_VALUE"""
    a, b = 0, 1  # Initialize first two Fibonacci numbers
    print(a, end=' ')  # Print Fib(0)
    
    while b <= MAX_VALUE:
        print(b, end=' ')
        a, b = b, a + b  # Calculate next Fibonacci number

if __name__ == '__main__':
    print_fibonacci_sequence()