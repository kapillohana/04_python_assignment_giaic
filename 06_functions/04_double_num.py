def double (num):
    return num * 2

def main():
    try:
        num = float(input("Enter a number: "))
        print(f"Double is {double(num)}")
    except ValueError:
        print ("Invalid number")

if __name__ == '__main__':
    main()