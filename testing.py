class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor=bottom_floor
        self.top_floor=top_floor
        self.current_floor=bottom_floor
    def floor_up(self):
        if  self.current_floor!=self.top_floor:
            self.current_floor+=1
            print(self.current_floor)
    def floor_down(self):
        if  self.current_floor!=self.bottom_floor:
            self.current_floor-=1
            print(self.current_floor)

    def go_to_floor(self,floor):
        while self.current_floor<floor:
            self.floor_up()
        while self.current_floor>floor:
            self.floor_down()
class Building:
    
    def __init__(self, bottom_floor, top_floor, elevator):
        super().__init__(bottom_floor, top_floor)
        self.elevators=[]
        for i in range(elevator):
            self.elevators.append(Elevator(bottom_floor,top_floor))
        
    def run_elevator(self,elevator,destination_floor):
        print(f"Running elevator {elevator} to floor {destination_floor}")
        self.elevators[elevator].go_to_floor(destination_floor)
    
    def fire_alarm(self):
        self.go_to_floor(1)

building = Building(1, 10, 3)
building.run_elevator(0, 5)
building.run_elevator(1, 8)
building.run_elevator(2, 3)
building.fire_alarm()