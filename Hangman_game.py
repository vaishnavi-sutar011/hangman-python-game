import random

secret_words = {'rose':'flower' ,'india':'country' ,'maharashtra':'state' ,
                'earth': 'planet', 'mango' : 'fruit' ,'elephant':'animal'}
secret_word = random.choice(list(secret_words.keys()))
hint = secret_words[secret_word]
print(f'Hint : {hint}')

chances = 7
guessed_letters = []

print('Welcome to Hangman!')
print(f'You have {chances} lives left.')

for letter in secret_word:
        print('_',end=" ")

hangman_stages = [
        '''
        ---------
         |    |
         |
         |
         |
         |
         |
        ------------''',
        '''
        ---------
         |    |
         |    o
         |
         |
         |
         |
        ------------''',
        '''
        ---------
         |    |
         |    o
         |    |
         |
         |
         |
        ------------''',
        '''
        ---------
         |    |
         |    o
         |   /|
         |
         |
         |
        ------------''',
        '''
        ---------
         |    |
         |    o
         |   /|\\
         |
         |
         |
        ------------''',
        '''
        ---------
         |    |
         |    o
         |   /|\\
         |   / \\
         |
         |
        ------------'''
]


while chances > 0:
        guess = input("\nEnter a letter: ").lower()

        if guess in guessed_letters:
                print('You already guessed that letter!')
                print(f'Used letters : {guessed_letters}')
                continue
        guessed_letters.append(guess)
        
        if guess in secret_word:
                print('Correct guess')
                print(" ".join(letter if letter in guessed_letters else "_" for letter in secret_word))
                if all(letter in guessed_letters for letter in secret_word):
                        print("👏 YOU WON!!!!!!!!!!")
                        break
        else:
                chances = chances - 1
                print('Wrong guess')
                stage_index = 7 - chances - 1
                if stage_index < len(hangman_stages):
                        print(hangman_stages[stage_index])
                print(f'You have {chances} lives left.')

                if chances == 0:
                        print('😢YOU LOST!!')
                        print(f'Correct word is : {secret_word}')
                
print('Game is Over!')
print('Thank You For Playing!!!')


