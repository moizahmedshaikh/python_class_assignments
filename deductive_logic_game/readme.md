# Deductive Logic Game

This is a simple Python-based deductive logic game where the player must guess a secret three-digit number based on hints.

## Game Rules
- The program generates a random three-digit secret number (e.g., "631").
- The player has **10 attempts** to guess the secret number.
- After each guess, the program provides feedback:
  - `👌 (Correct)`: A correct digit in the correct place.
  - `👍 (Ok)`: A correct digit in the wrong place.
  - `❌ (Wrong)`: No correct digits.
- The game ends when the player guesses correctly or exhausts all attempts.

## Example Interaction
```
Welcome to the Guessing Game!

Guess a 3-digit number: 123
❌ 👍 👌 or Wrong Ok Correct

Guess a 3-digit number: 631
👌 👌 👌 or Correct Correct Correct
🎉 Congratulations! You guessed it right: 631
```

## Installation & Running the Game
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/deductive-logic-game.git
   ```
2. Navigate to the project folder:
   ```sh
   cd deductive-logic-game
   ```
3. Run the game:
   ```sh
   python game.py
   ```

## Requirements
- Python 3.x

## Contributing
Feel free to submit issues or pull requests to improve the game.

## License
This project is licensed under the MIT License.