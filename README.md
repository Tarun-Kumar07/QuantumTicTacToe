# QuantumTicTacToe

This is quantum version of traditional tic tac toe. It is implemented by referring to this 
<a href="https://physlab.org/wp-content/uploads/2023/05/QuantumTicTacToe_23100002_Fin.pdf" target="_blank">paper</a>.<br>
Refer to the rules section in the paper.

### Run the game
- Install docker. You can refer to <a href="https://docs.docker.com/engine/install/" target="_blank">official documentation</a>
- Once the docker is up and running paste the commands below.
- Create docker image <br>
```bash
    docker build -t quantum-tic-tac-toe https://github.com/Tarun-Kumar07/QuantumTicTacToe.git
```
- Run docker image
```bash
 docker run -p 8501:8501 quantum-tic-tac-toe
```
- Play the game by going to the url printed :).


