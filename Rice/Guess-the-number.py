#!usr/bin/pyton
import random

secret_num = random.randrange(0, 1000)

def ask_to_input():
    guess = float(raw_input('Please guess a number:'))
    return guess

times = 12
print 'I have choice a secret number'
print secret_num
while times > 0:
    print ''
    print 'You have %d times to guess' % times
    guess = ask_to_input()
    if guess < secret_num:
        print 'Higher'
    elif guess > secret_num:
        print 'Lower'
    else:
        print ''
        print 'Correct, You win!'
        break
    times -= 1
else:
    print ''
    print 'Oops! You lose!'
