import random
from words import words
from hangman_visual import stages
word_list = words  

chosen_word = random.choice(word_list)
print(chosen_word)

lives = 6

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print (display) 

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        

    print(display)

    if guess not in chosen_word:
        lives -= 1
    if lives == 0:
        end_of_game = True
        print ("You lose.")

    if "_" not in display:
        end_of_game = True
        print ("You win.")

    print (stages[lives])
