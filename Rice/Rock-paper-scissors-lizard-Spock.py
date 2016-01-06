#!usr/bin/python
# coding:utf-8
# Rock-paper-scissors-lizard-Spock
# Thanks for the Great Firewall of China, I can't even use the codeskulptor
import random

def name_to_number(name):
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        print 'not correct name.'

def number_to_name(number):
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        print 'not correct number.'

def rpsls(player_choice):
    print ""
    player_number = name_to_number(player_choice)
    comp_number = random.randint(0,4)
    comp_choice = number_to_name(comp_number)
    print 'Player chooses %s' % player_choice
    print 'Computer chooses %s' % comp_choice
    if player_number == comp_number:
        print 'No winner!'
    elif (player_number - comp_number)%5 > 2:
        print 'Computer wins!'
    else:
        print 'Player wins!'

for i in range(5):
    rpsls(number_to_name(i))
    
