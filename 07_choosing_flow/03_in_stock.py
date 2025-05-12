def num_in_stock(fruit: str) -> bool:

    inventory = {
        'apple' : 2,
        'banana' : 80,
        'durain' : 22,
        'mango' : 200,
    }

    return inventory.get(fruit.lower(), 0)

def main() -> None:
    fruit = input("Enter a fruit: ").strip()
    stock = num_in_stock(fruit)

    if stock > 0:
        print (f"This fruit is in stock. Here is how much quantity: \n{stock}")
    else:
        print (f"The fruit {fruit} is not in stock.")

    
if __name__ == '__main__':
    main()