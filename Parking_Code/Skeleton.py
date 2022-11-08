class Main:
    def __init__(self):
        pass

class garage:
    def __init__(self,spots,floors):
        self.spots = spots
        self.floors = floors

class command:
    def __init__(self):
        pass

class spot:
    def __init__(self,light,taken):
        self.light = light
        self.taken = taken
        #


spotNum = spot("red",True)

print(spotNum.light)
print(spotNum.taken)
