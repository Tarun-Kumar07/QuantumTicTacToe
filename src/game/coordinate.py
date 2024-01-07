from game.constants import LENGTH


class Coordinate(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __str__(self) -> str:
        val_flattened = LENGTH * self.x + self.y + 1
        if val_flattened == 1:
            return "1st"
        elif val_flattened == 2:
            return "2nd"
        else:
            return str(val_flattened) + "th"
