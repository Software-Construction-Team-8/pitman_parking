import pymongo
#this is how we connect to the data base, since I am usuing local host "MongoClient is left empty". we can add a link in there later
client = pymongo.MongoClient()
#name of the database
db = client["pitmanParking"]
#name of the table
#right now this table has 2 levels with 3 praking spots each. This is for test purposes only and the actual data will be implemented later.
collection = db["Garage 1"]


class spot:
    def __init__(self, id, occupied, number, light, level):
        #int. has to be unique
        self.id = id
        #boolean
        self.occupied = occupied
        #int. the number of the spot. has to be unique per floor but may repeat for level
        self.number = number
        #String. either green for available, red for taken
        self.light = light
        #int. represents what level in the garage is this spot in
        self.level = level




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
    def __init__(self,spots,floor):
        self.spots = spots
        self.floor = floor

    #a method to print the information of all the spots
    def printInfo(self):
        print("Welcome, here are all the spots:")
        for x in collection.find():
            print("********Spot ",x["SpaceId"],"**********\n")
            print("Spot Taken: \t",x['Space Occupied'])
            print("Spot Number: \t",x['Space Number'])
            print("Floor Number: \t",x['Level Number'], "\n")

    #a method to print all the non taken spots
    def printAvailable(self):
        print("Welcome, here are all the Available spots:")
        for x in collection.find({"Space Occupied" : False}):
            print("********Spot ID: ",x["SpaceId"],"**********\n")
            print("Spot Number: \t",x['Space Number'])
            print("Floor Number: \t",x['Level Number'], "\n")
            

        
        





if __name__ == "__main__":

    g = garage(6, 2)
    g.printInfo()

    x = updateSpotCommand(True)
    x.execute(1)
    x.execute(2)
    x.execute(3)

    g.printInfo()














