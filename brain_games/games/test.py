
import random

START_INTERVAL_1 = 1
END_INTERVAL_2 = 50
START_INTERVAL_3 = 51
END_INTERVAL_4 = 100

number_1 = random.randint(START_INTERVAL_1, END_INTERVAL_2)
number_2 = random.randint(START_INTERVAL_3, END_INTERVAL_4)
step = random.randint(1, 20)
random_lists = []

while len(random_lists) not in range(5, 10):
    random_lists = []
    step = random.randint(1, 20)
    i = iter(range(number_1, number_2, step))
    random_lists = list(i)



print(random_lists)