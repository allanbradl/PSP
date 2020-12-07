import operator
import arcpy
from arcpy import env
import csv
import os

cwd = os.getcwd()
arcpy.env.workspace = cwd + r"\CampgroundsData.gdb"

def appendtolist(distgate, electricCampsite, boatramp, proxvisit, trailpref, trailerstation):
    PreferenceList = []
    PreferenceList.extend([int(distgate), int(electricCampsite), int(boatramp), int(proxvisit), int(trailpref), int(trailerstation)])
    return PreferenceList

def EastGate(userPreferenceList):
    # set variable for feature class definition
    eastGateSiteMatch = {}
    eastGateFeatureClasses = arcpy.ListFeatureClasses()
    eastGateCampgrounds = eastGateFeatureClasses[0]
    eastGateFieldName = [f.name for f in arcpy.ListFields("Campgrounds")] 
    with arcpy.da.SearchCursor(eastGateCampgrounds, eastGateFieldName) as cursor:
        for row in cursor:
            eastGateCodes = [row[19], row[21], row[22], row[17], row[12], row[20]]
            eastScore = 0
            for i in range(len(eastGateCodes)):
                if eastGateCodes[i] == userPreferenceList[i]:
                    eastScore += 1
                    eastGateSiteMatch.update({row[6]: eastScore})
    sorted_EastSiteMatch = dict(sorted(eastGateSiteMatch.items(), key=operator.itemgetter(1),reverse=True))
    topThreeEast = list(sorted_EastSiteMatch.items())[:3]
    return topThreeEast

def EastGateDictionary():
    eastCampgrounds = {}
    eastNames = []
    eastAttributes = []
    eastFeatureClasses = arcpy.ListFeatureClasses()
    eastFeatures = eastFeatureClasses[0]
    eastFieldName = [f.name for f in arcpy.ListFields("Campgrounds")] 
    with arcpy.da.SearchCursor(eastFeatures, eastFieldName) as cursor:
        for row in cursor:
            name = row[6]
            eastNames.append(name)
            attributes = [row[4], row[5], row[7], row[8], row[23], row[24], row[14], row[15], row[16], row[9]]
            eastAttributes.append(attributes)
        for index in range(len(eastNames)):
            eastCampgrounds[eastNames[index]]  = eastAttributes[index]
    return eastCampgrounds

def WestGate(userList):
    # set variable for feature class definition
    westGateSiteMatch = {}
    westGateFeatureClasses = arcpy.ListFeatureClasses()
    westGateCampgrounds = westGateFeatureClasses[0]
    westGateFieldName = [f.name for f in arcpy.ListFields("Campgrounds")] 
    with arcpy.da.SearchCursor(westGateCampgrounds, westGateFieldName) as cursor:
        for row in cursor:
            westGateCodes = [row[18], row[21], row[22], row[17], row[12], row[20]]
            westScore = 0
            for i in range(len(westGateCodes)):
                if westGateCodes[i] == userList[i]:
                    westScore += 1
                    westGateSiteMatch.update({row[6]: westScore})
    sorted_WestSiteMatch = dict(sorted(westGateSiteMatch.items(), key=operator.itemgetter(1),reverse=True))
    topThreeWest = list(sorted_WestSiteMatch.items())[:3]
    return topThreeWest

def WestGateDictionary():
    westCampgrounds = {}
    westNames = []
    westAttributes = []
    westFeatureClasses = arcpy.ListFeatureClasses()
    westFeatures = westFeatureClasses[0]
    westFieldName = [f.name for f in arcpy.ListFields("Campgrounds")] 
    with arcpy.da.SearchCursor(westFeatures, westFieldName) as cursor:
        for row in cursor:
            name = row[6]
            westNames.append(name)
            attributes = [row[4], row[5], row[7], row[8], row[23], row[24], row[13], row[15], row[16], row[9]]
            westAttributes.append(attributes)
        for index in range(len(westNames)):
            westCampgrounds[westNames[index]]  = westAttributes[index]
    return westCampgrounds

# Opening statements about program: 
print("Welcome to the Algonquin Provincial Park Campground Selector.") 
print()
print("Algonquin offers a two different types of camping experiences: backcountry, and drive-in camping in developed campgrounds.")
print() 
print("Along the Highway 60 corridor, there are 9 developed campgrounds containing 1,257 campsites.")
print()
print("In a park so large, it can be difficult to choose a campsite when making a reservation.")
print()
print("This program should help make it a little bit easier by taking your preferences and choosing up to three campgrounds which meet those criterion.")
print()
print("This program assumes the user is only looking for individual camping, therefore the group campground will not be considered.")


# Input Section: 
# Users input their preferences in the PreferenceList

print()
print("***************************************************************")
print("Question 1)")
print()
try:

    while True:
            # Users' preference on their starting point
            startingpoint = str(input("Where would you like your starting point be? E = East Gate and W = West Gate:__  "))
            startingpoint = startingpoint.upper()
            if startingpoint not in ["E","W"]:
                print("Invalid entry. Please enter E or W.")
            else:
                break
    print()
    print("***************************************************************")
    print("Question 2)")
    print()
    while True:
            # Users' preferences on their distance from the starting point
            indistgate = str(input("How far would you want to travel to your campground? Under 20km: enter 1, Between 21 - 40km: enter 2, Over 40km: enter 3:__ "))
            if indistgate not in ["1","2","3"]:
                print("Invalid entry. Please enter 1, 2 or 3.")
            else:
                break 
    print()
    print("***************************************************************")
    print("Question 3)")
    print()
    while True:
        # Users' preferences on electric campsites
        inelectricCampsite = str(input("Would you like your campground to have electrical hook-up? Yes: enter 1, No: enter 0:__ "))
        if inelectricCampsite not in ["1","0"]:
            print("Invalid entry. Please enter 1 (Yes) or 0 (No).")
        else:
            break

    print()
    print("***************************************************************")
    print("Question 4)")
    print()
    while True:
            # Users' preferences on boat ramp
            inboatramp = str(input("Would you like your campground to have a boat ramp? Yes: enter 1, No: enter 0:__ "))
            if inboatramp not in ["1","0"]:    
                print("Invalid entry. Please enter 1 (Yes) or 0 (No).") 
            else:
                break
    print()
    print("***************************************************************")
    print("Question 5)")
    print()
    while True:  
            # Users' preference on the distance to visitor centre
            inproxvisit = str(input("What is your preferred distance to the Visitor Centre? Under 20km: enter 1, Between 20 - 40km: enter 2, over 40km: enter 3:__ "))
            if inproxvisit not in ["1","2","3"]:
                print("Invalid entry. Please enter 1 (Yes) or 0 (No).")
            else:
                break
    print()
    print("***************************************************************")
    print("Question 6)")
    print()
    while True:
            # Users' preference on the trails' difficulty
            intrailpref = str(input("What level of trail difficulty would you like to have in proximity to your campground? Easy: enter 1, Moderate: enter 2, Hard: enter 3:__ "))
            if intrailpref not in ["1","2","3"]:
                print("Invalid entry. Please enter 1 (Easy), 2 (Moderate) or 3 (Hard).")
            else:
                break
    print()
    print("***************************************************************")
    print("Question 7)")
    print()
    while True:
            # Users' preference on the distance to trailer station
            intrailerstation = str(input("What is your preferred distance to a trailer sanitation station?  Under 10km: enter 1, Between 11 - 20km: enter 2, over 21km: enter 3:__ "))
            if intrailerstation not in ["1","2","3"]:
                print("Invalid entry. Please enter 1, 2 or 3.")
            else:
                break
    print()
    print("***************************************************************")
    print()
    userPreference = appendtolist(indistgate, inelectricCampsite, inboatramp, inproxvisit, intrailpref, intrailerstation)

    # Create empty lists to hold individual dictionary items
    campgroundName = []
    electricalCampsites = []
    boatRamp = []
    dogFriendly = []
    wheelchairAccessible = []
    trailName = []
    trailDifficulty = []
    gateDistance = []
    westGateDistance = []
    trailerStationDistance = []
    visitorCentreDistance = []
    reservationLink = []

    if startingpoint=="E":
        EastGateResult = EastGate(userPreference)
        allEastGateCampgrounds = EastGateDictionary()
        for index in range(len(EastGateResult)):
            campName = EastGateResult[index][0]
            # Append individual dictionary items to empty list
            # Every item appended is associated with the same key (campground name)
            if campName in allEastGateCampgrounds:
                campgroundName.append(campName)
                electricalCampsites.append(allEastGateCampgrounds[campName][0])
                boatRamp.append(allEastGateCampgrounds[campName][1])
                dogFriendly.append(allEastGateCampgrounds[campName][2])
                wheelchairAccessible.append(allEastGateCampgrounds[campName][3])
                trailName.append(allEastGateCampgrounds[campName][4])
                trailDifficulty.append(allEastGateCampgrounds[campName][5])
                gateDistance.append(allEastGateCampgrounds[campName][6])
                trailerStationDistance.append(allEastGateCampgrounds[campName][7])
                visitorCentreDistance.append(allEastGateCampgrounds[campName][8])
                reservationLink.append(allEastGateCampgrounds[campName][9])
    else:
        WestGateResult = WestGate(userPreference)
        allWestGateCampgrounds = WestGateDictionary()
        for index in range(len(WestGateResult)):
            campName = WestGateResult[index][0]
            # Append individual dictionary items to empty list
            # Every item appended is associated with the same key (campground name)
            if campName in allWestGateCampgrounds:
                campgroundName.append(campName)
                electricalCampsites.append(allWestGateCampgrounds[campName][0])
                boatRamp.append(allWestGateCampgrounds[campName][1])
                dogFriendly.append(allWestGateCampgrounds[campName][2])
                wheelchairAccessible.append(allWestGateCampgrounds[campName][3])
                trailName.append(allWestGateCampgrounds[campName][4])
                trailDifficulty.append(allWestGateCampgrounds[campName][5])
                gateDistance.append(allWestGateCampgrounds[campName][6])
                trailerStationDistance.append(allWestGateCampgrounds[campName][7])
                visitorCentreDistance.append(allWestGateCampgrounds[campName][8])
                reservationLink.append(allWestGateCampgrounds[campName][9])

    # Write output to a new text file
    # Each row is one campground
    with open("CampgroundSelection.csv", "w", newline="") as campground_final:
        campgroundWriter = csv.writer(campground_final)
        campgroundWriter.writerow(["Name of Campground", "Electrical Campsites", "Boat Ramp", "Dog Friendly", "Wheelchair Accessible", "Nearest Trail", "Trail Difficulty", 
        "Distance to Preferred Gate (km)", "Distance to Trailer Sanitation Station (km)", "Distance to Visitor Centre (km)", "Reservation Link"])
        for index in range(len(campgroundName)):
            row = [campgroundName[index]] + [electricalCampsites[index]] + [boatRamp[index]] + [dogFriendly[index]] + [wheelchairAccessible[index]] + \
                [trailName[index]] + [trailDifficulty[index]] + [gateDistance[index]]  + [trailerStationDistance[index]] + \
                    [visitorCentreDistance[index]] + [reservationLink[index]]
            campgroundWriter.writerow(row)
except ValueError:
    print("Enter correct value as requested please")