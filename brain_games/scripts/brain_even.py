#!/usr/bin/env python
from brain_games.games.even_odd import check_even, INTRODUCTION_TO_GAME
from brain_games.engine_brain import run_engine


def main():
    run_engine(check_even, INTRODUCTION_TO_GAME)


if __name__ == '__main__':
    main()
