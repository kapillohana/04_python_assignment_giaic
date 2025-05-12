def greet (name:str) -> str:
    return f"Greetings {name}!"

def main() -> None:
    name = input("What is your name? ").strip() #Remove any whitespace if added accidentally
    print(greet(name))

if __name__ == '__main__':
    main()