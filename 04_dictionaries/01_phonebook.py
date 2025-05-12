def read_phone_numbers():
    """
    Creates and populates a phonebook dictionary from user input.
    Features:
    - Input validation for phone numbers
    - Case-insensitive name handling
    - Duplicate name prevention
    
    Returns:
        dict: Phonebook with names as keys and numbers as values
    """
    phonebook = {}
    print("\n=== PHONEBOOK CREATION ===")
    print("Enter contact information (leave name blank to finish)")
    
    while True:
        name = input("\nContact name: ").strip().title()
        if not name:  # Exit if name is empty
            break
            
        if name in phonebook:
            print(f"⚠️ {name} already exists in phonebook!")
            continue
            
        while True:
            number = input("Phone number (digits only): ").strip()
            if number.isdigit():
                phonebook[name] = number
                print(f"✅ {name} added successfully!")
                break
            print("❌ Invalid number! Please enter digits only.")
    
    return phonebook


def print_phonebook(phonebook):
    """
    Displays all contacts in a formatted manner.
    
    Args:
        phonebook (dict): The phonebook dictionary to display
    """
    if not phonebook:
        print("\nPhonebook is empty!")
        return
        
    print("\n=== CONTACT LIST ===")
    for name, number in sorted(phonebook.items()):
        print(f"📞 {name:20} -> {format_phone_number(number)}")


def lookup_numbers(phonebook):
    """
    Provides interactive contact lookup functionality.
    
    Args:
        phonebook (dict): The phonebook dictionary to search in
    """
    if not phonebook:
        print("No contacts to lookup!")
        return
        
    print("\n=== CONTACT LOOKUP ===")
    print("Enter name to search (leave blank to exit)")
    
    while True:
        query = input("\nSearch name: ").strip().title()
        if not query:
            break
            
        found = False
        for name in phonebook:
            if query.lower() in name.lower():  # Partial match
                print(f"🔍 Found: {name} -> {format_phone_number(phonebook[name])}")
                found = True
                
        if not found:
            print(f"❌ No contacts matching '{query}'")


def format_phone_number(number):
    """
    Formats a phone number string for better readability.
    
    Args:
        number (str): Raw phone number string
        
    Returns:
        str: Formatted phone number
    """
    if len(number) == 10:
        return f"({number[:3]}) {number[3:6]}-{number[6:]}"
    return number  # Return as-is if not standard length


def delete_contact(phonebook):
    """
    Allows user to delete contacts from the phonebook.
    """
    if not phonebook:
        print("No contacts to delete!")
        return
        
    print("\n=== DELETE CONTACT ===")
    print_phonebook(phonebook)
    print("\nEnter name to delete (leave blank to cancel)")
    
    while True:
        name = input("\nDelete contact: ").strip().title()
        if not name:
            break
            
        if name in phonebook:
            confirm = input(f"Delete {name}? (y/n): ").lower()
            if confirm == 'y':
                del phonebook[name]
                print(f"🗑️ {name} removed from phonebook!")
        else:
            print(f"❌ {name} not found in phonebook")


def main():
    """
    Main program flow with enhanced menu system.
    """
    phonebook = read_phone_numbers()
    
    while True:
        print("\n=== PHONEBOOK MENU ===")
        print("1. View all contacts")
        print("2. Search contacts")
        print("3. Add new contacts")
        print("4. Delete contacts")
        print("5. Exit")
        
        choice = input("\nSelect option (1-5): ")
        
        if choice == '1':
            print_phonebook(phonebook)
        elif choice == '2':
            lookup_numbers(phonebook)
        elif choice == '3':
            new_contacts = read_phone_numbers()
            phonebook.update(new_contacts)
        elif choice == '4':
            delete_contact(phonebook)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-5")


if __name__ == '__main__':
    main()