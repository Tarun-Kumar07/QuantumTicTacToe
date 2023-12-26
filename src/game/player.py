from coordinate import Coordinate


class Player(object):
    def __init__(self, name: str) -> None:
        self.name = name

    def get_input(self) -> Coordinate:
        message = f"{self.name}'s turn, enter coordinates : "
        x, y = input(message).split(",")
        return Coordinate(int(x), int(y))

    def get_name(self):
        return self.name
