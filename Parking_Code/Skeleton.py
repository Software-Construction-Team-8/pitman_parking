
class Main:
    def __init__(self):
        pass

class garage:
    def __init__(self,spots,floor):
        self.spots = int(spots)
        self.floor = int(floor)

class command:
    def __init__(self):
        pass

class spot:
    def __init__(self):
        self.light = 'green'
        self.taken = False


class garageSpot:
    def __init__(self,spots,floor,light,taken):
        self.spots = spots
        self.floor = floor
        self.light = light
        self.taken = taken


spotNum = spot()
gfloor1 = garage(10,1)
array = []

for i in range(gfloor1.spots):
    gfloor1Total = garageSpot(gfloor1.spots,gfloor1.floor,spotNum.light,spotNum.taken)
    array.append(gfloor1Total)#write into database when setup.
#For loop just printing out a demo of only a floor 1 in a which is an empty garage
for i in range(gfloor1.spots):
    print("******** spot",i+1," **********")
    print("Spot Taken: \t",array[i].taken)
    array[i].spots = i+1
    print("Spot Number: \t",array[i].spots)
    print("Light Color: \t",array[i].light)
    print("Floor Number: \t",array[i].floor)
    
# print(spotNum.light)
# print(spotNum.taken)
# print(gfloor1.spots)
# print(gfloor1.floor)

