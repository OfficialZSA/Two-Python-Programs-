## Question 1 ##
import random

def compare_guess_to_secret(user_guess, secret_letter):
    user_guess = user_guess.upper()  # Convert both inputs to uppercase
    secret_letter = secret_letter.upper()

    if user_guess < secret_letter:
        return -1
    elif user_guess > secret_letter:
        return 1
    else:
        return 0

def guessing_game():
    secret_letter = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    score = 0

    for attempt in range(1, 4):
        print("Guess the secret letter (A-Z): ")
        user_guess = input().upper()
        comparison = compare_guess_to_secret(user_guess, secret_letter)

        if comparison == -1:
            print("Your guess is too low.")
        elif comparison == 1:
            print("Your guess is too high.")
        else:
            score = 26 / 3  # Corrected the score calculation
            print(f"Congratulations! You guessed the secret letter '{secret_letter}' on attempt {attempt}")
            print(f"You scored {score} points.")
            break  # Exit the loop if the guess is correct

    if score == 0:
        print("Sorry, you didn't guess the letter correctly. You scored 0 points.")

guessing_game()

## Question 2 ##
import random

amount = random.randint(0,20) + round (random.randint(0,100)/100,2)
print("Your total is = ",amount)

# ASSUME payment >= amount
# Calculate the total amount of change due
payment = input("Amount that was given: ")
payment = float(payment)


# Initialize variables for counting the number each demonination in the change
change = amount - payment
if (change <= 0):
    print("Your Change is:", round(change,2))
    d = 0  # 1.00
    q = 0  # 0.25
    i = 0  # 0.10
    n = 0  # 0.05

if (change > 0):

# Dollars
    d = int(change)
    change =round(change - d,2)
    
#Quarters
    q = int(change / 0.25)
    change = round(change - (q * 0.25),2)

# Dimes
    i  = int(change / 0.10)
    change = round(change - (i * 0.10),2)

# Nickels
    n  = int(change / 0.05)
    change = round(change - (n * 0.05),2)

    print("Change Owed:", round(change,2))

    
# Display a message indicating the numbers of each denomination in the change
print("you got", int(d), "Dollar(s)", int(q), "Quarter(s)", int(i), "Dime(s)", int(n), "Nickel(s) back in change.")

#END

# Test Values
# Test Value amount = $13.34 , and payment = $20
# We give back Dollars(d) = 6, Quarters(q) = 2, Dimes(i) = 1, Nickels(n) = 1

# Test Values
# Test Value amount = $2.31 , and payment = $5
# We give back Dollars(d) = 2, Quarters(q) = 1, Dimes(i) = 0, Nickels(n) = 1

# Test Values
# Test Value amount = $4.23 , and payment = $5
# We give back Dollars(d) = 0, Quarters(q) = 3, Dimes(i) = 0, Nickels(n) = 0

# Test Values
# Test Value amount = $9.77 , and payment = $10
# We give back Dollars(d) = 0, Quarters(q) = 0, Dimes(i) = 2, Nickels(n) = 0

# Test Values
# Test Value amount = $4.66 , and payment = $10
# We give back Dollars(d) = 5, Quarters(q) = 1, Dimes(i) = 1, Nickels(n) = 0

