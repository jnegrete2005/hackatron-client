import sys
import random

from src.types import *


def choose_move(game_state: GameState) -> int:
    """
    This is the main function that you'll have to implement!

    I will show you a very simple example where we choose a
    random move.

    :param game_state: The current state of the game.
    :type game_state: GameState

    :return: The move to make (LEFT, UP, RIGHT, DOWN).
    :rtype: int
    """
    return random.randint(1, 4)


def main():
    """
    This is the main entry point of the program.
    It reads the game state from stdin, parses it as a GameState
    object, and then calls the choose_move function to get the move.
    Finally, it prints the move to stdout.
    """
    try:
        while True:
            # 1. Read the game state from stdin
            data = sys.stdin.readline().strip()  # Important to strip because of newlines
            if not data:
                break  # Server has closed the connection

            # 2. Parse the game state
            game_state = GameState.from_json(data)

            # 3. Choose a move
            move = choose_move(game_state)

            # 4. Send the move to stdout
            print(move, flush=True)  # You must flush to ensure the server receives it!
    except EOFError:
        pass  # End of input
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr, flush=True)


if __name__ == "__main__":
    main()
