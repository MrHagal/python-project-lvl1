#!/usr/bin/env python
from brain_games.games.greatest_divisor_gcd \
    import question_answer, INTRODUCTION_TO_GAME
from brain_games.engine_brain import run_engine


def main():
    run_engine(question_answer, INTRODUCTION_TO_GAME)


if __name__ == '__main__':
    main()
