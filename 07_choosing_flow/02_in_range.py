def in_range(n: int, low: int, high: int) -> bool:
    
    return low <= n <= high

def main() -> None:
    """Test the in_range function with some examples."""
    # Example test cases
    print(in_range(5, 1, 10))    # True
    print(in_range(10, 1, 10))   # True
    print(in_range(0, 1, 10))    # False
    print(in_range(11, 1, 10))   # False

if __name__ == '__main__':
    main()