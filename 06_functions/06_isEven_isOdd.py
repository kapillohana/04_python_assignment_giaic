def is_odd(value: int) -> bool:
    """Return True if value is odd, False if even."""
    return value % 2 == 1

def main():
    for num in range(10, 20):
        print(f"{num} {'odd' if is_odd(num) else 'even'}")

if __name__ == '__main__':
    main()