"""
Write a Python program that implements a deductive logic game where the player must guess a secret three-digit number based on hints.
"""

import random

def get_feedback(guess,secret_number):
    feedback_imojis = []
    feedback_message = []

    for i in range(3):
        if guess[i] == secret_number[i]:
            feedback_imojis.append("👌")
            feedback_message.append("Correct")
            
        elif guess[i] in secret_number:
            feedback_imojis.append("👍")
            feedback_message.append("Ok")

        else: 
            feedback_imojis.append("❌")
            feedback_message.append("Wrong")

    return feedback_imojis, feedback_message


def main():
    attempts = 10
    while attempts > 0:
        
        random_number = str(random.randrange(100,999))
        guess = input("Guess a 3-digit number: ")

        if len(guess) != 3 or not guess.isdigit():
            print("Invalid input! Please enter a 3-digit number.")
            continue

        if guess == random_number:
            print(f"🎉 Congratulations! You guessed it right: {random_number}")
            break

        else: 
            feedback_imojis, feedback_message  = get_feedback(guess,random_number)
            print(" ".join(feedback_imojis) , "or" , " ".join(feedback_message))

        attempts -= 1
        if attempts == 0:
            print(f"Game Over! The secret number was {random_number}.")
            break

if __name__ == "__main__":
    main()








