import pymongo


#this is how we connect to the data base, since I am usuing local host "MongoClient is left empty". we can add a link in there later
client = pymongo.MongoClient('mongodb+srv://sc_delaEmi:u2JsEd0nzYssgaMd@cluster0.8qczawe.mongodb.net/test')
#name of the database
db = client["test"]

garage = input("Hello, what is the name of the garage to manage? (enter \"Parking_Spots\"))\n")
collection = db[garage]
allData = collection.find()
allRecords = list(allData)
if(allRecords):
    print("Successfully Connected to the Database")
else:
    exit("There was an Error Connceting to the Database")
    

#This Class keeps all the data locally that will be stored in the database. The purpose is to make it easy for the user to modify the data
class spot:
    def __init__(self, id, occupied, level, number):
        #int. has to be unique
        self.id = id
        #boolean
        self.occupied = occupied
        #int. the number of the spot. has to be unique per floor but may repeat for level
        self.number = number
        #String. either green for available, red for taken
        if (self.occupied == True):
            self.light = "red"
        else:
            self.light = "green"
        #int. represents what level in the garage this spot is in
        self.level = level


    #getters and setters
    def getId(self):
        return self.id
    
    def getOccupied(self):
        return self.occupied

    def getLevel(self):
        return self.level

    def getNumber(self):
        return self.number
    
    def getLight(self):
        return self.light

    
    #this is a method that will locally set a certain spot to a value given by the user
    def setOccupied(self, occupied):
        if (occupied == True):
            self.occupied = True
            self.light = "red"
        elif (occupied == False):
            self.occupied = False
            self.light = "green"
    
        
    
    #this will print all the information of a certain spot
    def printInfo(self):
        print("Space ID: ", self.getId(), " Space Ocupied: ", self.getOccupied(), " Level Number: ", self.getLevel()," Space Number: ", self.getNumber(), "Light: ", self.getLight())



#purpose: to hold information of how many parking spots there are and how many floors. show the user the information about the spots in an organized manner
#it will aslo keep track of all the changed made by the user so that it is easy to update the database later
#after the user is done inputting information, this will use command pattersn to send the info to the database
class garage:
    def __init__(self):
        self.spots = 0
        self.floors = 0
        self.floorList = []
        self.historyOfSpotsUpdated = []
        self.historyOfNewValues = []


    #getters and setters
    def getFloors(self):
        return self.floors

    def getSpots(self):
        return self.spots

    def setSpots(self, spots):
        self.spots = spots

    def setFloors(self, floors):
        self.spots = floors

    def getHistoryOfSpotsUpdated(self):
        return self.historyOfSpotsUpdated

    def getHistoryOfNewValues(self):
        return self.historyOfNewValues


    #prints how many floors with how many spots in each floor 
    def printInfo(self):
        for floor in self.floorList:
            print("floor ", floor[0].getLevel(), " with ", len(floor), " spots.") 


    #will get information about the database and set the garage info to match that
    def populate(self, records):
        self.floors = 0
        for row in records:
            if (row['Level Number'] > self.floors):
                self.floors = row['Level Number']

        for i in range(self.floors):
            self.floorList.append([])

        
        for row in records:
            newSpot = spot(row['Space ID'], row['Space Occupied'], row['Level Number'], row['Space Number'])
            self.floorList[row['Level Number'] - 1].append(newSpot)
            self.spots += 1

    #prints all spots
    def printAll(self):
        print("Here are all the spots:")
        for floor in self.floorList:
            for spot in floor:
                spot.printInfo()

    #prints spots that are set to false(meaning those are available)
    def printAvailable(self):
        print("Here are all the available spots :")
        for floor in self.floorList:
            for spot in floor:
                if spot.getOccupied() == False:
                    spot.printInfo()
        
    def setAllToFree(self):
        for i in range(150):
            self.updateSpot(i+1, False)

    def undoChange(self, previousValue, lastUpdated):
        if len(self.historyOfSpotsUpdated) == 0:
            print("No changes to undo")
            return
        else:
            print(previousValue)
            for floor in self.floorList:
                for spot in floor:
                    if (int(spot.getId()) == int(lastUpdated)):
                        print("succesful")
                        spot.setOccupied(previousValue)
                        self.historyOfSpotsUpdated.pop()
                        self.historyOfNewValues.pop()
                        return
            
            print("could not undo")
            
        



    #this method updates spots locally. to update the database we can use the update spot command methods found beelow. 
    def updateSpot(self, id, newValue):
        for floor in self.floorList:
            for spot in floor:
                if spot.getId() == id:
                    previousValue = spot.getOccupied()
                    spot.setOccupied(newValue)
                    spotUpdated = {"Space ID":id}
                    newInfo = {"$set":{"Space Occupied":newValue}}
                    self.historyOfNewValues.append(newInfo)
                    self.historyOfSpotsUpdated.append(spotUpdated)
                    print("Successful, Spot was Updated!")
                    return previousValue
        print("UnSuccessful, Spot was NOT Updated!")

#This class gets the information form the history queue and uploads all the info to the database
class updateGarageCommand:
    def __init__(self, garage):
        self.garage = garage
    
    def execute(self):
        while (len(self.garage.historyOfSpotsUpdated) > 0):
            findSpot = self.garage.historyOfSpotsUpdated[0]
            updateSpot = self.garage.historyOfNewValues[0]
            self.garage.historyOfSpotsUpdated.pop(0)
            self.garage.historyOfNewValues.pop(0)
            collection.update_one(findSpot, updateSpot)
        print("*****Garage has now been Updated*****")



if __name__ == "__main__":
    #create the garage
    g = garage()
    g.populate(allRecords)
    g.printInfo()
    #user interface
    action = input("What would you like to do?\nPress \"1\" to view all the spots.\nPress \"2\" to view all the available spots.\nPress \"3\" to update a spot.\nPress \"4\" to undo the last change.\nPress \"0\" exit the program.\n")
    previousValue = True
    lastUpdated = 0
    while(action != "0"):
        if(action == "1"):
            g.printAll()
        if(action == "2"):
            g.printAvailable()
        if(action == "3"):
            spaceToUpdate = input("Enter the ID of the space to update: \n")
            newValue = input("Enter \"1\" to set the spot as taken.\nEnter \"2\" to set the spot as free.\n")
            if newValue == "1":
                lastUpdated = spaceToUpdate
                previousValue = g.updateSpot(int(spaceToUpdate), True)
            elif newValue == "2":
                lastUpdated = spaceToUpdate
                previousValue = g.updateSpot(int(spaceToUpdate), False) 
            print("Spot has beem updated!")
        if(action == "4"):
            g.undoChange(previousValue, lastUpdated) 

        action = input("What would you like to do?\nPress \"1\" to view all the spots.\nPress \"2\" to view all the available spots.\nPress \"3\" to update a spot.\nPress \"4\" to undo the last change.\nPress \"0\" exit the program.\n")
    c = updateGarageCommand(g)
    c.execute()
    print("Thank you")

    
    
    # g = garage()
    # g.populate(allRecords)
    # print(g.getFloors(), " floors with ",g.getSpots(), " spots" )
    # g.updateSpot(1, True)
    # g.updateSpot(2, True)
    # print(g.getHistoryOfNewValues())
    # print(g.getHistoryOfSpotsUpdated())
    # c = updateGarageCommand(g)
    # c.execute()
    # print(g.getHistoryOfNewValues())
    # print(g.getHistoryOfSpotsUpdated())