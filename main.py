import random
from hangman_art import stages, logo
from hangman_words import word_list
from colorama import Fore, Back, Style, init
init(autoreset=True)

lives = 6
print(Fore.CYAN+logo)
print(Fore.CYAN + "=" * 50)
print(Fore.YELLOW + "🎮 Welcome to Hangman!")
print(Fore.WHITE + "Guess the word before the man is hanged.")
print(Fore.CYAN + "=" * 50)
chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guessed_letters=[]

while not game_over:
    print(Fore.YELLOW+"Lives left"+Fore.RED + "❤️ " * lives)
    print("Guessed letters:", " ".join(guessed_letters))
    guess = input("Guess a letter: ").lower()
    if guess not in guessed_letters:
        guessed_letters.append(guess)
    if guess in correct_letters:
        print(Fore.YELLOW+f"Already guessed '{guess}'")
        continue
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
    print(Fore.MAGENTA+stages[lives])
    if lives == 0:
        game_over = True
        print(Fore.RED+"\n💀 GAME OVER 💀")
        print(Fore.RED+f"The word was: {chosen_word.upper()}")   
    if "_" not in display:
        game_over = True
        print(Fore.GREEN+"\n🎉 CONGRATULATIONS! 🎉")
        print(Fore.GREEN+f"You guessed: {chosen_word.upper()}")

    

