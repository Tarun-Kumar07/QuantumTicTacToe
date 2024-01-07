# QuantumTicTacToe

This is quantum version of traditional tic tac toe. <br>
It is implemented by referring to this 
<a href="https://physlab.org/wp-content/uploads/2023/05/QuantumTicTacToe_23100002_Fin.pdf" target="_blank">paper</a>.
Refer to the <u>rules</u> section in the paper.<br>
You can play the game <a href="https://quantumtictactoe-ekm2cauxbumdelekkkaxqz.streamlit.app/" target="_blank">here</a>.
If the link is not working then run game locally by refering to this [section](#Locally-run-the-game)<br>

### Locally run the game
- Install docker. You can refer to <a href="https://docs.docker.com/engine/install/" target="_blank">official documentation</a>
- Once the docker is up and running paste the commands below in terminal.
- Create docker image <br>
```bash
 docker build -t quantum-tic-tac-toe https://github.com/Tarun-Kumar07/QuantumTicTacToe.git
```
- Run docker image
```bash
 docker run -p 8501:8501 quantum-tic-tac-toe
```
- Play the game by going to the url printed :smile:.
