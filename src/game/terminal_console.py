from game.player import Player
from game.quantum_tic_tac_toe import QuantumTicTacToe

player1 = Player("One")
player2 = Player("Two")


def collapse_move(game: QuantumTicTacToe, current_player: Player):
    coordinate = current_player.get_input()
    game.collapse(coordinate)


def entanglement_move(game: QuantumTicTacToe, current_player: Player):
    print("Enter control qubit")
    control = current_player.get_input()
    print("Enter target qubit")
    target = current_player.get_input()
    game.entangle(control, target)


def execute_till_no_error(func):
    is_error = True
    while is_error:
        try:
            func()
            is_error = False
        except Exception as err:
            print(err)


def main():
    game = QuantumTicTacToe()
    current_player = player1
    while not game.is_over():
        print(game)
        print(f"{current_player.get_name()}'s turn")
        print("Choose\n 1. Classical move\n 2. Entanglement move")
        choice = int(input("Choice : "))
        match choice:
            case 1:
                execute_till_no_error(lambda: collapse_move(game, current_player))
            case 2:
                execute_till_no_error(lambda: entanglement_move(game, current_player))
            case _:
                print("Invalid choice")
                continue

        current_player = player2 if current_player == player1 else player1

    print(game)
    winner = game.get_winner()
    if winner is not None:
        print(f"{winner} won the game !!")
    else:
        print("Game is draw")


if __name__ == "__main__":
    main()
