def get_user_info() -> tuple [str, str, str]:
    
    first_name = input("What is your first name?: ").strip()
    last_name = input("What is your last name?: ").strip()
    email_address= input("What is your email address?: ").strip().lower()

    return first_name, last_name,  email_address

def main() -> None:
    user_data = get_user_info()
    print("\nReceived the following user data")
    print(f"First Name: {user_data[0]}")
    print(f"Last Name: {user_data[1]}")
    print(f"Email Address: {user_data[2]}")


if __name__ == "__main__":
    main()