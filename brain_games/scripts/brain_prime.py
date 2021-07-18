#!/usr/bin/env python
from brain_games.games.prime import check_prime, introduction_to_game
from brain_games.engine_brain import run_engine


def main():
    run_engine(check_prime, introduction_to_game)


if __name__ == '__main__':
    main()
