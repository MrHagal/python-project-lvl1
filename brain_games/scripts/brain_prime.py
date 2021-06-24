import random
import math
from brain_games.scripts.brain_games import main2


def prime():
    name = main2()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    while count != 3:
        number_1 = random.randint(2, 100)
        print(f'Question: {number_1}')
        answer = input('Your answer: ')

        # проверка на прсото число
        if (math.factorial(number_1 - 1) + 1) % number_1 != 0:
            result = 'no'
        else:
            result = 'yes'

        if str(result) == answer:
            count += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{result}'.\n Let's try again, {name}!")
            break
        if count == 3:
            print(f'Congratulations, {name}!')
