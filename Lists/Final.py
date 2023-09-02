import random 

print('What is your name: ')
name = input() 

print(f'Good luck {name}')

names = ["hamza", 'yara', 'hadi', 'nour']
word = random.choice(names)

print('The name is:')
guesses = ''

turns = 12  

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char)
        else:
            print('-')
            failed += 1

    if failed == 0:
        print('You Win!!')
        break

    guess = input('Enter your guess: ')

    guesses += guess

    if guess not in word:
        turns -= 1
        print('Wrong guess')
        print(f'You have a {turns} guess')

    if turns == 0:
        print('You lose!!')