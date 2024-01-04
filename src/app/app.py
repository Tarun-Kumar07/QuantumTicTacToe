import streamlit as st
from streamlit.delta_generator import DeltaGenerator
from game import Coordinate
from game import QuantumTicTacToe

ENTANGLE_CLICKED = "entangle_clicked"
COLLAPSE_CLICKED = "collapse_clicked"
ENTAINGLE_CELL_CLICKED_FIRST = "entangle_cell_clicked_first"
COLLAPSE_BUTTON_TOOLTIP = (
    "If the chosen qubit is entangled it will collapse both qubits"
)
ENTANGLE_BUTTON_TOOLTIP = "Choose target qubit first then the control qubit"
PLAYER_X = "X"
PLAYER_O = "O"


def on_click_collapse():
    st.session_state.collapse_clicked = True
    reset_entangle_click_flags()


def on_click_entangle():
    st.session_state.entangle_clicked = True
    reset_collapse_click_flags()


def reset_collapse_click_flags():
    st.session_state.collapse_clicked = False


def reset_entangle_click_flags():
    st.session_state.entangle_clicked = False
    st.session_state.entangle_cell_clicked_first = None


def null_safe_get_from_session(key: str):
    if key in st.session_state:
        return st.session_state[key]


def assign_next_player():
    if st.session_state.current_player == PLAYER_X:
        st.session_state.current_player = PLAYER_O
    else:
        st.session_state.current_player = PLAYER_X


def on_click_cell(x, y):
    coordinate = Coordinate(x, y)

    if null_safe_get_from_session(COLLAPSE_CLICKED):
        try:
            st.session_state.game.collapse(coordinate)
            assign_next_player()
        except Exception as e:
            st.error(e)
            reset_collapse_click_flags()
    elif null_safe_get_from_session(ENTANGLE_CLICKED):
        target_cell = null_safe_get_from_session(ENTAINGLE_CELL_CLICKED_FIRST)
        if target_cell:
            control_cell = Coordinate(x, y)
            try:
                st.session_state.game.entangle(control_cell, target_cell)
                assign_next_player()
            except Exception as e:
                st.error(e)
                reset_entangle_click_flags()
        else:
            st.session_state.entangle_cell_clicked_first = Coordinate(x, y)


def cell_tool_tip():
    if null_safe_get_from_session(COLLAPSE_CLICKED):
        return "Click to collapse"
    elif null_safe_get_from_session(ENTAINGLE_CELL_CLICKED_FIRST):
        return "Choose control qubit"
    else:
        return "Choose target qubit"


def display_game(game: DeltaGenerator):
    game.write("Game")
    board = st.session_state.game.get_board()
    for x, row in enumerate(board.get_all()):
        cols = game.columns(len(row))
        for y, col in enumerate(row):
            cols[y].button(
                col,
                key=f"{x}-{y}",
                on_click=on_click_cell,
                args=(x, y),
                help=cell_tool_tip(),
            )


def display_player(player: DeltaGenerator):
    game = st.session_state.game
    if game.is_over():
        if game.get_winner():
            player.write(f"Winner is {game.get_winner()}")
        else:
            player.write("Game is draw")
        player.button("New Game", on_click=lambda: st.session_state.clear())
    else:
        player.write(f"Player {st.session_state.current_player}'s turn")
        player.button(
            "Collapse", on_click=on_click_collapse, help=COLLAPSE_BUTTON_TOOLTIP
        )
        player.button(
            "Entangle", on_click=on_click_entangle, help=ENTANGLE_BUTTON_TOOLTIP
        )


def initialize_session():
    if "game" not in st.session_state:
        st.session_state.game = QuantumTicTacToe()
    if "current_player" not in st.session_state:
        st.session_state.current_player = PLAYER_X


def run_game():
    page_title = "Quantum Tic-Tac-Toe"
    layout = "centered"

    st.set_page_config(page_title=page_title, layout=layout)
    st.write("Quantum tic-tac-toe")

    initialize_session()

    game, player = st.columns([0.7, 0.3])
    display_game(game)
    display_player(player)
