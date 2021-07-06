#!/usr/bin/env python
from brain_games.games.generation_calc import calc_up, introduction_question
from brain_games.engine_brain import count_algo_check


def main():
    count_algo_check(calc_up, introduction_question)  # передаем аргумент как функцию


if __name__ == '__main__':
    main()
