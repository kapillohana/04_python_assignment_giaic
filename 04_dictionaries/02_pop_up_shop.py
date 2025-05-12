def main():
    # Fruit with names and prices
    fruits = {
        'apple': 1.5, 
        'durian': 50, 
        'jackfruit': 80, 
        'kiwi': 1, 
        'rambutan': 1.5, 
        'mango': 5
    }
    
    total_cost = 0
    print("Welcome to the Fruit Shop!")
    print("Available fruits and prices:")
    
    # Displayyy availale fruits and prices
    for fruit, price in fruits.items():
        print(f"- {fruit.capitalize():<9} ${price:.2f} each")
    
    print("\nPlease enter how many of each fruit you want:")
    
    for fruit_name in fruits:
        while True:
            try:
                user_input = input(f"How many ({fruit_name}) do you want? (0 if none): ")
                amount = int(user_input)
                if amount >= 0:
                    break
                print("Please enter a positive number or 0")
            except ValueError:
                print("Please enter a valid whole number")
        
        total_cost += fruits[fruit_name] * amount
    
    #  the total cost 
    print(f"\nYour total is ${total_cost:.2f}")

if __name__ == '__main__':
    main()