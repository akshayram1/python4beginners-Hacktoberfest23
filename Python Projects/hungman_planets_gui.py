import random
import tkinter as tk
from tkinter import messagebox

# Dictionary of planet names and hints
planet_data = {
    "earth": "Hint: The only known planet with life.",
    "mars": "Hint: Often called the 'Red Planet'.",
    "venus": "Hint: The hottest planet in our solar system.",
    "jupiter": "Hint: The largest planet with a Great Red Spot.",
    "saturn": "Hint: Known for its beautiful ring system.",
    "uranus": "Hint: It rotates on its side.",
    "neptune": "Hint: The farthest planet from the sun."
}

# Function to choose a random planet from the dictionary


def choose_planet():
    planet = random.choice(list(planet_data.keys()))
    hint = planet_data[planet]
    return planet, hint

# Hangman game class


class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.word_to_guess, self.hint = choose_planet()  # Choose a random planet
        self.guessed_letters = []  # List of guessed letters
        self.attempts = 0  # Number of incorrect attempts
        self.max_attempts = 6  # Maximum allowed attempts
        self.word_length = len(self.word_to_guess)  # Length of the word
        self.remaining_attempts = self.max_attempts  # Remaining attempts

        # Initialize the word display variable
        self.word_display = tk.StringVar()
        self.word_display.set(self.display_word())

        # Create and configure the label for displaying the word
        self.label = tk.Label(
            root, textvariable=self.word_display, font=("Helvetica", 24))
        self.label.pack()

        # Create a label to display the word length
        self.word_length_label = tk.Label(
            root, text=f"Word Length: {self.word_length}")
        self.word_length_label.pack()

        # Create a label to display the remaining attempts
        self.remaining_attempts_label = tk.Label(
            root, text=f"Remaining Attempts: {self.remaining_attempts}")
        self.remaining_attempts_label.pack()

        # Create a label to display the hint
        self.hint_label = tk.Label(root, text=self.hint)
        self.hint_label.pack()

        # Create an input frame
        self.input_frame = tk.Frame(root)
        self.input_frame.pack()

        # Label for instructing the user to guess a letter
        self.input_label = tk.Label(self.input_frame, text="Guess a letter:")
        self.input_label.grid(row=0, column=0)

        # Entry field for user's letter input
        self.guess_entry = tk.Entry(self.input_frame)
        self.guess_entry.grid(row=0, column=1)

        # Button to submit the guess
        self.guess_button = tk.Button(
            self.input_frame, text="Guess", command=self.make_guess)
        self.guess_button.grid(row=0, column=2)

        # Create a "New Game" button
        self.new_game_button = tk.Button(
            self.input_frame, text="New Game", command=self.new_game)
        self.new_game_button.grid(row=0, column=3)

    # Function to display the word with guessed letters
    def display_word(self):
        display = ""
        for letter in self.word_to_guess:
            if letter in self.guessed_letters:
                display += letter
            else:
                display += "_"
        return display

    # Function to process the user's guess
    def make_guess(self):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        # Check if the game is already won or lost
        if set(self.word_to_guess) == set(self.guessed_letters):
            return
        if self.attempts >= self.max_attempts:
            return

        # Check if the guess is a single letter
        if len(guess) != 1 or not guess.isalpha():
            return

        # Check if the letter has already been guessed
        if guess in self.guessed_letters:
            return

        # Add the guess to the list of guessed letters
        self.guessed_letters.append(guess)
        self.word_display.set(self.display_word())

        # Check if the guess is incorrect
        if guess not in self.word_to_guess:
            self.attempts += 1
            self.remaining_attempts = self.max_attempts - self.attempts

        # Update the remaining attempts label
        self.remaining_attempts_label.config(
            text=f"Remaining Attempts: {self.remaining_attempts}")

        # Check for a win or game over
        if set(self.word_to_guess) == set(self.guessed_letters):
            self.word_display.set(
                "You guessed the planet! It was '" + self.word_to_guess + "'. You win!")
            self.guess_entry.config(state="disabled")
            self.guess_button.config(state="disabled")
            messagebox.showinfo(
                "Congratulations!", f"You guessed the planet! It was '{self.word_to_guess}'. You win!")
        elif self.attempts >= self.max_attempts:
            self.word_display.set(
                "You ran out of attempts. The planet was '" + self.word_to_guess + "'. Game over!")
            self.guess_entry.config(state="disabled")
            self.guess_button.config(state="disabled")
            self.hint_label.config(text="Hint: " + self.hint)

    # Function to start a new game
    def new_game(self):
        self.word_to_guess, self.hint = choose_planet()
        self.guessed_letters = []
        self.attempts = 0
        self.remaining_attempts = self.max_attempts
        self.word_display.set(self.display_word())
        self.remaining_attempts_label.config(
            text=f"Remaining Attempts: {self.remaining_attempts}")
        self.hint_label.config(text=self.hint)
        self.guess_entry.config(state="normal")
        self.guess_button.config(state="normal")


if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
