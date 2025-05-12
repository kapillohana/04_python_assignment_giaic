def subtract_seven(num: int) -> int:
    return num - 7

def main() -> None:
    num = 7
    result = subtract_seven(num)
    print (f"This should be zero: {result}")

if __name__ == '__main__':
    main()