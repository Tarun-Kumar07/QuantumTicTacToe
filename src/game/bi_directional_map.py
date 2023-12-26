EMPTY_VALUE = -1


class BiDirectionalMap:
    """
    BiDirectionalMap in which key and value are both positive numbers
    """

    def __init__(self, size) -> None:
        self.size = size
        self.map = [EMPTY_VALUE for _ in range(size)]

    def put(self, key1: int, key2: int) -> None:
        self.__validate_key(key1)
        self.__validate_key(key2)

        self.map[key1] = key2
        self.map[key2] = key1

    def get(self, key) -> None | int:
        self.__validate_key(key)
        val = self.map[key]
        if val is not EMPTY_VALUE:
            return val

    def delete(self, key):
        self.__validate_key(key)
        mapped_key = self.map[key]
        self.map[key] = EMPTY_VALUE
        self.map[mapped_key] = EMPTY_VALUE

    def __validate_key(self, key):
        if key < 0 or key >= self.size:
            raise ValueError(f"{key} is not in [0,{self.size}]")
