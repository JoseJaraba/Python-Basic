class Vehicle:
    def __init__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color

    def move(self, how_fast):
        if how_fast == "fast":
            print("Moving around 100 - 120 kilometers")
        elif how_fast == "medium":
            print("Moving around 60 - 80 kilometers")
        elif how_fast == "slow":
            print("Moving around 40 - 60 kilometers")
        else:
            pass

    def step(self):
        print("Stopped")


if __name__ == "__main__":
    pass
