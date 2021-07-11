#!/usr/bin/env python
import prompt


def hello_player():
    print('Welcome to the Brain Games!')
    name_player = prompt.string('May I have your name? ')
    print(f'Hello, {name_player}!')
    return name_player
