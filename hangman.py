import random
import hangman_words
from hangman_art import logo, stages

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(hangman_words.word_list)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)

# Create an empty List called display.
display = []
#For each letter in the chosen_word, add a "_" to 'display'.
for letter in chosen_word:
    display.append("_")


#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
end_of_game = False

while not end_of_game :
  user_guess = input("Guess a letter: ").lower()

  #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
  if user_guess in display:
     print("You've already guessed " + user_guess)


  #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
  # Loop through each position in the chosen_word;
  #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
  for i in range(0, len(chosen_word)):
    if user_guess == chosen_word[i]:
      display[i] = user_guess
      
  #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
  if user_guess not in chosen_word:
    #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    print(user_guess + " is not in the word")
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You lose.")


  #TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
  #Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
  #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")

  if "_" not in display:
     end_of_game = True
     print("You win.")

  #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
  if lives == 6:
     print(stages[6])
  elif lives == 5:
     print(stages[5])
  elif lives == 4:
     print(stages[4])
  elif lives ==3:
     print(stages[3])
  elif lives == 2:
     print(stages[2])
  elif lives == 1:
     print(stages[1])
  elif lives == 0:
     print(stages[0])
  