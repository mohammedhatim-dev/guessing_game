import random

print("--- Welcome to the Number Guessing Game! ---")
print("I am thinking of a number between 1 and 20.")

# توليد رقم عشوائي بين 1 و 20
secret_number = random.randint(1, 20)
attempts = 0

while True:
    try:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break # الخروج من الحلقة عند الإجابة الصحيحة
            
    except ValueError:
        print("Invalid input. Please enter a whole number.")