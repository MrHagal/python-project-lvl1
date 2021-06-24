import random
from brain_games.scripts.brain_games import main2


def progression():
    name = main2()
    print('What number is missing in the progression?')
    count = 0
    while count != 3:
        random_list = []
        while len(random_list) not in range(5, 10):  # генерируем лист
            random_list = []
            number_1 = random.randint(1, 50)
            number_2 = random.randint(51, 100)
            step = random.randint(1, 20)
            for i in range(number_1, number_2, step):
                random_list.append(i)

        random_point_list = random.randint(0, len(random_list) - 1)  # random index
        result = random_list[random_point_list]  # результат для сверки
        random_list[random_point_list] = '..'  # замена index на '..'

        print('Question:', *random_list)
        answer = input('Your answer: ')

        if str(result) == answer:
            count += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.\n"
                  f"Let's try again, {name}")
            break
        if count == 3:
            print(f'Congratulations, {name}!')
