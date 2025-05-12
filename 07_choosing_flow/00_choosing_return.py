Adult_Age : int = 18 

def is_adult(age:int) -> bool:  #True if the user is an adult false if less then 18
    return age >= Adult_Age

def main() -> None:
    try:
        age = int(input("How old is this person?: "))
        print(is_adult(age))
    except ValueError:
        print("Please enter a valid integer for age.")


if __name__ == "__main__":
    main()