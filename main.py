import random
from hangman_art import logo, stages
from hangman_word import word_list



print(logo)
print("########## Guess the word game ##########\n")
n = len(stages)
int(n)

chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.

display = []
for c in chosen_word:
        display += '_'

for i in display:
    print(i, end=" ")
lol = True
lives = 6
while lol:
    guess = input("\nGuess a letter: ").lower()


    for i in range(0, len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    
    if guess in display:
        print(f"\nYou have already used this letter {guess}\n")
    else:
        print(f"\nThe letter {guess} is not in the chosen word")

    if guess not in chosen_word:
        print(stages[lives])
        lives-=1
        print("The letter is not in the word ! ")

    if lives == 0:
         print(stages[0])
         print("\nYou lost\n")
         break
    else:

        if '_' not in display:
            lol = False

        for i in display:
            print(i, end="")

        if not lol:
            print("\nYou win")
