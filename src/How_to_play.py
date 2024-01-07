import streamlit as st

st.set_page_config(page_title="Quantum Tic-Tac-Toe", page_icon="🎮")

st.write(
    """
# Quantum Tic Tac Toe 🚀

Welcome to Quantum Tic Tac Toe, a quantum twist to the classic game! This version incorporates principles from quantum mechanics, introducing exciting new moves and strategies.

To get basic understanding of the principles, we recommend watching [Schrödinger's cat experiment](https://youtu.be/z1GCnycbMeA?feature=shared).

## Rules 📜

1. Quantum Tic Tac Toe is a 2-player game. Each player can make one of two legal plays: "Collapse" or "Entanglement."
2. Each tile can be in state
    * "Q" : superposition
    * "✗" : collapsed to X
    * "О" : collapsed to O

#### Collapse Move 💥
- **Description:** Choose a tile and assign it "✗" or "О" with a 50% probability.
- **Legal Tiles:** The chosen tile must be in superposition, i.e state "Q".
- **Restriction:** A tile that has been collapsed cannot be collapsed again.

#### Entanglement Move ⚛️
- **Description:** Apply a quantum entanglement move across two tiles. 
- **Legal Move:** Atleast one of the chosen tiles for entanglement must be "collapsed" tile, i.e. in state "✗" or "О".
- **Restriction:** A tile that has already been entangled cannot be entangled further.

## Strategy and Obstacles 🧠
- Use the "Entanglement" move strategically to present obstacles for your opponent.
- Entangle your chosen tile with your opponent's to render their occupied tile "smeared."

## Winning 🏆
The first player to achieve a complete row, column, or diagonal filled with uninterrupted X’s or O’s wins the game.

## Game Showcase 🎮
See the efficacy of the "Entanglement" move in action by playing a real game.

Enjoy the quantum journey in Tic Tac Toe! May the entangled tiles be ever in your favor. 🌌

## Further Details and Research 📚
For more in-depth details, refer to [this paper](https://physlab.org/wp-content/uploads/2023/05/QuantumTicTacToe_23100002_Fin.pdf).
"""
)
