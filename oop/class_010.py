class Coordinate:
    def __init__(self, x, y):  # Constructor Method
        self.x = x
        self.y = y

    def distance(self, other_coordinate):
        x_diff = (self.x - other_coordinate.x) ** 2
        y_diff = (self.y - other_coordinate.y) ** 2

        return "%.2f" % (x_diff + y_diff) ** 0.5


if __name__ == "__main__":
    coordinate_one = Coordinate(3, 5)
    coordinate_two = Coordinate(4, 8)

    print(coordinate_one.distance(coordinate_two))
