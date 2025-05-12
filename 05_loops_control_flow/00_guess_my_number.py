import random
def guess_number():
    secret_number = random.randint(0,99)
    attempts = 0

    print ("I am thinking a number between 0-99...")

    while True:
        try:
            guess = int(input("Enter a guess: "))
            attempts +=1

            #check guess
            if guess < secret_number:
                print("Your guess is too low")
            elif guess > secret_number:
                print ("Your guess is too high")
            else:
                print (f"congrats! The number was: {secret_number}")
                print (f"You guessed it in {attempts} attempts")
                break
        except ValueError:
            print("Please Enter a valid number between (0-99)")

if __name__ == '__main__':
    guess_number()

