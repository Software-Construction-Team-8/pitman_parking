import pymongo
import pandas as pd
#this is how we connect to the data base, since I am usuing local host "MongoClient is left empty". we can add a link in there later
client = pymongo.MongoClient()
#name of the database
db = client["pitmanParking"]
#name of the table
#right now this table has 2 levels with 3 praking spots each. This is for test purposes only and the actual data will be implemented later.
garage = input("Hello, what is the name of the garage to manage? (enter \"Garage 1\"))\n")
collection = db[garage]


class spot:
    
    def __init__(self, id, occupied, level, number):
        #int. has to be uniqu
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
        #int. represents what level in the garage is this spot in
        self.level = level



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

    
    def setOccupied(self, occupied):
        if (occupied == True):
            self.occupied = True
            self.light = "red"
        elif (occupied == False):
            self.occupied = False
            self.light = "green"
    
        
    
    def printInfo(self):
        print("SpaceId: ", self.getId(), " Space Ocupied: ", self.getOccupied(), " Level Number: ", self.getLevel()," Space Number: ", self.getNumber(), "Light: ", self.getLight())




#this will change the value of true or false of a given spot
class updateSpotCommand:
    def __init__(self, occupied):
        self.occupied = occupied
    
    def execute(self, spotId):
        findSpot = {"SpaceId" : spotId}
        updateSpot = {"$set": {"Space Occupied" : self.occupied}}
        collection.update_one(findSpot, updateSpot)
        print("*****Spot has now been Updated*****\n")

    ## implement undo method after we have a history array




        

#purpose: to hold information of how many parking spots there are and how many floors. show the user the information about the spots in an organized manner
class garage:
    def __init__(self, spots, floors):
        self.spots = spots
        self.floors = floors
        self.floorList = [[] for i in range(self.floors)]



    def getFloors(self):
        return self.floors

    def getSpots(self):
        return self.spots

    def printFloorList(self):
        for floor in self.floorList:
            print("floor ", floor[0].getLevel(), " with ", len(floor), " spots.") 






    #will get information about the database and crate a garage object based on that information
    def populate(self):
        allData = collection.find()
        allRecords = list(allData)
        for row in allRecords:
            newSpot = spot(row['SpaceId'], row['Space Occupied'], row['Level Number'], row['Space Number'])
            self.floorList[row['Level Number'] - 1].append(newSpot)


        #for row in allRecords:
        #    print(row['SpaceId'])
        #df = pd.DataFrame(allRecords)
        #print(df[0])

    def printInfo(self):
        print("Here are all the spots:")
        for floor in self.floorList:
            for spot in floor:
                spot.printInfo()


    def printAvailable(self):
        print("Here are all the spots:")
        for floor in self.floorList:
            for spot in floor:
                if spot.getOccupied() == False:
                    spot.printInfo()


    def updateSpot(self, id, newValue):
        for floor in self.floorList:
            for spot in floor:
                print(spot.getId())
                if spot.getId() == id:
                    spot.setOccupied(newValue)
                    print("Successful")
                    break
        print("UnSuccessful")
        

    


    # #a method to print the information of all the spots
    # def printInfo(self):
    #     print("Welcome, here are all the spots:")
    #     for x in collection.find():
    #         print("********Spot ",x["SpaceId"],"**********\n")
    #         print("Spot Taken: \t",x['Space Occupied'])
    #         print("Spot Number: \t",x['Space Number'])
    #         print("Floor Number: \t",x['Level Number'], "\n")

    # #a method to print all the non taken spots
    # def printAvailable(self):
    #     print("Welcome, here are all the Available spots:")
    #     for x in collection.find({"Space Occupied" : False}):
    #         print("********Spot ID: ",x["SpaceId"],"**********\n")
    #         print("Spot Number: \t",x['Space Number'])
    #         print("Floor Number: \t",x['Level Number'], "\n")
            

        
        





if __name__ == "__main__":


    g = garage(6, 2)
    g.populate()

    action = input("What would you like to do?\nPress \"1\" to view all the spots.\nPress \"2\" to view all the available spots.\nPress \"3\" to update a spot.\nPress \"0\" exit the program.\n")
    while(action != "0"):
        if(action == "1"):
            g.printInfo()
        if(action == "2"):
            g.printAvailable()
        if(action == "3"):
            spaceToUpdate = input("Enter the name of the space to update: \n")
            newValue = input("Enter \"1\" to set the spot as taken.\nEnter \"2\" to set the spot as free.\n")
            if newValue == "1":
                g.updateSpot(int(spaceToUpdate), True)
            elif newValue == "2":
                g.updateSpot(int(spaceToUpdate), False) 
            print("Spot has beem updated!")

        action = input("What would you like to do?\nPress \"1\" to view all the spots.\nPress \"2\" to view all the available spots.\nPress \"3\" to update a spot.\nPress \"0\" exit the program.\n")

    print("Thank you")
        
            







    
    
    
    #g.printInfo()
    

    # x = updateSpotCommand(True)
    # x.execute(1)
    # x.execute(2)
    # x.execute(3)

    # g.printInfo()


















