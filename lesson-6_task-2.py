class Road:
    _length = 0
    _width = 0

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width
        mass = self._length * self._width * 25 * 5 / 1000
        print(f"Масса асфальта: {int(mass)} т")


a = Road(20, 5000)
