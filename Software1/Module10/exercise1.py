class Elevator:
    def __init__(self, bottom, top):
        self.bottom_floor = bottom
        self.top_floor = top
        self.current_floor = bottom
    def go_to_floor(self, floor):
        if floor < self.bottom_floor or floor > self.top_floor:
            print("Invalid floor")

        while self.current_floor < floor:
                self.floor_up()

        while self.current_floor > floor:
                self.floor_down()
    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now on floor {self.current_floor}")


    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now on floor {self.current_floor}")


h = Elevator(1, 10)
print("Basic elevator test:")
h.go_to_floor(5)
h.go_to_floor(1)