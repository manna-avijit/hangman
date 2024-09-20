import random
from collections import Counter

someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''
someWords = someWords.split(' ')
word = random.choice(someWords)

if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of a fruit')
    guessed_letters = ['_'] * len(word)
    print(' '.join(guessed_letters))
    
    playing = True
    letterGuessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0
    
    try:
        while chances > 0 and flag == 0:
            print(f"\nYou have {chances} chances left.")
            chances -= 1
            try:
                guess = str(input('Enter a letter to guess: ')).lower()
            except:
                print('Enter only a letter!')
                continue

            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue

            letterGuessed += guess
            
            # Update guessed letters if the guess is correct
            if guess in word:
                for i, char in enumerate(word):
                    if char == guess:
                        guessed_letters[i] = guess

            # Display the current state of guessed letters
            print(' '.join(guessed_letters))

            # Check if the whole word is guessed
            if '_' not in guessed_letters:
                print('Congratulations, You won!')
                flag = 1
                break

        if chances <= 0 and '_' in guessed_letters:
            print('You lost! Try again..')
            print(f'The word was {word}')
    
    except KeyboardInterrupt:
        print('\nBye! Try again.')
        exit()