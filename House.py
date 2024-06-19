class House:
    def  __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(f'Number of floors: {self.numberOfFloors}')



house = House()

print(f'Updated number of floors: {house.numberOfFloors}')
house.setNewNumberOfFloors(7)
print(f'Updated number of floors: {house.numberOfFloors}')
