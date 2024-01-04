from game.bi_directional_map import BiDirectionalMap
from game.board import Board
from game.coordinate import Coordinate
from game.constants import Q, O, X, LENGTH, NUM_QUBITS
from qiskit import QuantumCircuit, execute, Aer


def is_collapsed(cell: str) -> bool:
    return cell == O or cell == X


def get_qubit(coordinate: Coordinate) -> int:
    return LENGTH * coordinate.get_x() + coordinate.get_y()


def get_coordinate(qubit: int) -> Coordinate:
    return Coordinate(qubit // LENGTH, qubit % LENGTH)


def qc_with_all_qubits_in_superposition():
    qc = QuantumCircuit(NUM_QUBITS, NUM_QUBITS)
    for i in range(NUM_QUBITS):
        qc.h(i)
    return qc


class QuantumTicTacToe(object):
    def __init__(self) -> None:
        self.board = Board()
        self.qc = qc_with_all_qubits_in_superposition()
        self.entangled_qubits = BiDirectionalMap(NUM_QUBITS)
        self.winner = None

    def collapse(self, coordinate: Coordinate):
        cell = self.board.get(coordinate)
        if is_collapsed(cell):
            raise ValueError(
                f"{coordinate} is already collapsed. Choose your move again !!"
            )

        coordinates_to_collapse = [coordinate]

        entangled_coordinate = self.__entangled_coordinate(coordinate)
        if entangled_coordinate:
            coordinates_to_collapse.append(entangled_coordinate)

        collapsed_values = self.__collapse_coordinates(coordinates_to_collapse)
        for c, v in collapsed_values.items():
            self.board.set(c, v)

    def __entangled_coordinate(self, coordinate):
        qubit = get_qubit(coordinate)
        entangled_qubit = self.entangled_qubits.get(qubit)

        if entangled_qubit is not None:
            self.entangled_qubits.delete(qubit)
            return get_coordinate(entangled_qubit)

    def entangle(self, control: Coordinate, target: Coordinate):
        target_qubit = get_qubit(target)
        control_qubit = get_qubit(control)

        target_cell = self.board.get(target)
        if not is_collapsed(target_cell):
            raise ValueError(
                f"Target must be collapsed. {target} is not collapsed. Choose your move again !!"
            )

        self.qc.cx(control_qubit, target_qubit)

        self.entangled_qubits.put(control_qubit, target_qubit)
        self.board.set(control, Q)
        self.board.set(target, Q)

    def get_winner(self):
        return self.winner

    def is_over(self):
        self.winner = self.board.get_winner()
        return self.winner is not None or self.board.all_cells_collapsed()

    def __collapse_coordinates(self, coordinates):
        qubits = [get_qubit(c) for c in coordinates]
        result = self.__measure(qubits)
        collapsed_value = {}

        for to_measure in qubits:
            self.__delete_all_gates_for_qubit(to_measure)
            measured_value = self.__get_measured_value_and_initialize(
                to_measure, result
            )
            collapsed_value[get_coordinate(to_measure)] = measured_value

        return collapsed_value

    def __measure(self, qubits):
        for q in qubits:
            self.qc.measure(q, q)

        backend = Aer.get_backend("aer_simulator")
        job_result = execute(self.qc, backend, shots=1).result()
        counts = job_result.get_counts()

        return next(iter(counts))

    def __delete_all_gates_for_qubit(self, qubit):
        for index, instruction in enumerate(self.qc.data):
            for q in instruction.qubits:
                if self.qc.find_bit(q).index == qubit:
                    del self.qc.data[index]

    def __get_measured_value_and_initialize(self, to_measure, result):
        state = result[-to_measure - 1]
        if state == "0":
            self.qc.reset(to_measure)
            return O
        else:
            self.qc.reset(to_measure)
            self.qc.x(to_measure)
            return X

    def get_board(self) -> Board:
        return self.board

    def __str__(self) -> str:
        return str(self.board)
