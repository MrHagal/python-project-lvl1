#!/usr/bin/env python
from brain_games.games.prime\
    import generate_question_and_answer, INTRODUCTION_TO_GAME
from brain_games.engine_brain import run_engine


def main():
    run_engine(generate_question_and_answer, INTRODUCTION_TO_GAME)


if __name__ == '__main__':
    main()
