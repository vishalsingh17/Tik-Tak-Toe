from game.game.logic import TicTacToe
from game.exception.exception import CustomException
import sys
import logging

logger = logging.getLogger(__name__)


def play(game):
    try:
        print('Welcome to Tic Tac Toe!')

        while True:
            # Reset the board
            game.board = [' '] * 10
            player1_marker, player2_marker = game.player_input()
            turn = game.choose_first()
            print(turn + ' will go first.')

            play_game = input('Are you ready to play? Enter Yes or No.')

            if play_game.lower()[0] == 'y':
                game_on = True
            else:
                game_on = False

            while game_on:
                if turn == 'Player 1':
                    # Player1's turn.

                    game.display_board()
                    position = game.player_choice()
                    game.place_marker(player1_marker, position)

                    if game.win_check(player1_marker):
                        game.display_board()
                        print('Congratulations! You have won the game!')
                        game_on = False
                    else:
                        if game.full_board_check():
                            game.display_board()
                            print('The game is a draw!')
                            break
                        else:
                            turn = 'Player 2'

                else:
                    # Player2's turn.
                    game.display_board()
                    position = game.player_choice()
                    game.place_marker(player2_marker, position)

                    if game.win_check(player2_marker):
                        game.display_board()
                        print('Player 2 has won!')
                        game_on = False
                    else:
                        if game.full_board_check():
                            game.display_board()
                            print('The game is a draw!')
                            break
                        else:
                            turn = 'Player 1'

            if not game.replay():
                break
    except Exception as e:
        logger.error(CustomException(e, sys))
        raise e


if __name__ == "__main__":
    tic_tack_toe = TicTacToe()
    play(tic_tack_toe)
