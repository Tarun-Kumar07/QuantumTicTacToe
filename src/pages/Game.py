import streamlit as st
from streamlit.delta_generator import DeltaGenerator
from game import Coordinate
from game import QuantumTicTacToe
from game.constants import O, X

ENTANGLE_CLICKED = "entangle_clicked"
COLLAPSE_CLICKED = "collapse_clicked"
ENTAINGLE_CELL_CLICKED_FIRST = "entangle_cell_clicked_first"
COLLAPSE_BUTTON_TOOLTIP = "If the chosen tile is entangled it will collapse both tiles"
ENTANGLE_BUTTON_TOOLTIP = "Choose tiles to entangle"
PLAYER_X = "❌"
PLAYER_O = "⭕"


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
            st.error(e, icon="⚠️")
        finally:
            reset_collapse_click_flags()
    elif null_safe_get_from_session(ENTANGLE_CLICKED):
        target_cell = null_safe_get_from_session(ENTAINGLE_CELL_CLICKED_FIRST)
        if target_cell:
            control_cell = Coordinate(x, y)
            try:
                st.session_state.game.entangle(control_cell, target_cell)
                assign_next_player()
            except Exception as e:
                st.error(e, icon="⚠️")
            finally:
                reset_entangle_click_flags()
        else:
            st.session_state.entangle_cell_clicked_first = Coordinate(x, y)


def cell_tool_tip():
    if null_safe_get_from_session(COLLAPSE_CLICKED):
        return "Click to collapse"
    elif null_safe_get_from_session(ENTAINGLE_CELL_CLICKED_FIRST):
        return "Choose control qubit"
    elif null_safe_get_from_session(ENTANGLE_CLICKED):
        return "Choose target qubit"
    elif st.session_state.game.is_over():
        return "Start new game"
    else:
        return "Choose move first"


def cell_display_value(cell: str):
    if cell is X:
        return "✗"
    elif cell is O:
        return "О"
    else:
        return "Q"


def player_display_value(winner: str):
    if winner is X:
        return PLAYER_X
    elif winner is O:
        return PLAYER_O


def display_game(game: DeltaGenerator):
    board = st.session_state.game.get_board()
    for x, row in enumerate(board.get_all()):
        cols = game.columns(len(row))
        for y, col in enumerate(row):
            cols[y].button(
                cell_display_value(col),
                key=f"{x}-{y}",
                on_click=on_click_cell,
                args=(x, y),
                help=cell_tool_tip(),
            )


def display_player(player: DeltaGenerator):
    game = st.session_state.game
    if game.is_over():
        winner = game.get_winner()
        if winner:
            st.success(f"{player_display_value(winner)} won !!", icon="🎉")
        else:
            st.info("It's a tie !!", icon="🤝")
        player.button("New Game", on_click=lambda: st.session_state.clear())
    else:
        player.markdown(f"### {st.session_state.current_player}'s turn")
        player.button(
            "Collapse 💥", on_click=on_click_collapse, help=COLLAPSE_BUTTON_TOOLTIP
        )
        player.button(
            "Entangle ⚛️ ", on_click=on_click_entangle, help=ENTANGLE_BUTTON_TOOLTIP
        )


def initialize_session():
    if "game" not in st.session_state:
        st.session_state.game = QuantumTicTacToe()
    if "current_player" not in st.session_state:
        st.session_state.current_player = PLAYER_X


def run_game():
    page_title = "Quantum Tic-Tac-Toe"
    page_icon = "🎮"
    layout = "centered"

    st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
    st.markdown("### Quantum tic-tac-toe")

    initialize_session()

    game, player = st.columns([0.7, 0.3])
    display_game(game)
    display_player(player)


if __name__ == "__main__":
    run_game()
