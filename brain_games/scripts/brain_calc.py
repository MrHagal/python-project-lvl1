#!/usr/bin/env python
from brain_games.games.calc import run_calc, introduction_to_game
from brain_games.engine_brain import run_engine


def main():
    run_engine(run_calc, introduction_to_game)


if __name__ == '__main__':
    main()
