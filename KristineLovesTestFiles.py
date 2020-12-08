# import operator # this version doesn't use a dictionary for the scores, but a list
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
    eastGateSiteMatch = []
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
            eastGateSiteMatch.append([eastScore, row[6]])
    eastGateSiteMatch.sort(reverse=True)
    eastGateSiteMatch = eastGateSiteMatch[:3]
    return eastGateSiteMatch

def WestGate(userList):
    # set variable for feature class definition
    westGateSiteMatch = []
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
            westGateSiteMatch.append([westScore, row[6]])
    westGateSiteMatch.sort(reverse=True)
    westGateSiteMatch = westGateSiteMatch[:3]
    return westGateSiteMatch

def GateDictionary():
    campgrounds = {}
    campNames = []
    campAttributes = []
    campFeatureClasses = arcpy.ListFeatureClasses()
    campFeatures = campFeatureClasses[0]
    campFieldName = [f.name for f in arcpy.ListFields("Campgrounds")] 
    with arcpy.da.SearchCursor(campFeatures, campFieldName) as cursor:
        for row in cursor:
            name = row[6]
            campNames.append(name)
            attributes = [row[4], row[5], row[7], row[8], row[23], row[24], row[13], row[14], row[15], row[16], row[9]]
            campAttributes.append(attributes)
        for index in range(len(campNames)):
            campgrounds[campNames[index]]  = campAttributes[index]
    return campgrounds

def main():

    # Input Section: 
    # Users input their preferences in the PreferenceList
    try:
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
        print()
        answer = str(input("Enter 'y' to start the application: "))
        answer = answer.upper()
        while answer == "Y":
            print()
            print("***************************************************************")
            print("Question 1)")
            print()
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

            if startingpoint=="E":
                FinalGateResult = EastGate(userPreference)
                print("Your top 3 matches are: ")
                print()
                print("Campground Name\t\t\tMatch Score")
                for index in range(len(FinalGateResult)):
                    matchName = FinalGateResult[index][1]
                    matchScore = FinalGateResult[index][0]
                    print(matchName, '\t\t', matchScore)
            else:
                FinalGateResult = WestGate(userPreference)
                print("Your top 3 matches are: ")
                print()
                print("Campground Name\t\t\tMatch Score")
                for index in range(len(FinalGateResult)):
                    matchName = FinalGateResult[index][1]
                    matchScore = FinalGateResult[index][0]
                    print(matchName, '\t\t', matchScore)
            print()
            print("***************************************************************")
            print()
            answer = input("Do you want to run the campground selector again (Y/N)? ")
            answer = answer.upper()
        
        # # Output Section 
        # Create empty lists to hold individual dictionary items
        # simplified version of the code that uses one dictionary and has all information regardless of chosen gate
        # dictionary has both east gate and west gate distances
        campgroundName = []
        electricalCampsites = []
        boatRamp = []
        dogFriendly = []
        wheelchairAccessible = []
        trailName = []
        trailDifficulty = []
        westGateDistance = []
        eastGateDistance = []
        trailerStationDistance = []
        visitorCentreDistance = []
        reservationLink = []

        allCampgrounds = GateDictionary()
        for index in range(len(FinalGateResult)):
            campSelectionName = FinalGateResult[index][1]
            # Append individual dictionary items to empty list
            # Every item appended is associated with the same key (campground name)
            if campSelectionName in allCampgrounds:
                campgroundName.append(campSelectionName)
                electricalCampsites.append(allCampgrounds[campSelectionName][0])
                boatRamp.append(allCampgrounds[campSelectionName][1])
                dogFriendly.append(allCampgrounds[campSelectionName][2])
                wheelchairAccessible.append(allCampgrounds[campSelectionName][3])
                trailName.append(allCampgrounds[campSelectionName][4])
                trailDifficulty.append(allCampgrounds[campSelectionName][5])
                westGateDistance.append(allCampgrounds[campSelectionName][6])
                eastGateDistance.append(allCampgrounds[campSelectionName][7])
                trailerStationDistance.append(allCampgrounds[campSelectionName][8])
                visitorCentreDistance.append(allCampgrounds[campSelectionName][9])
                reservationLink.append(allCampgrounds[campSelectionName][10])


        # Write output to a new text file
        # Each row is one campground
        with open("CampgroundSelection.csv", "w", newline="") as campground_final:
            campgroundWriter = csv.writer(campground_final)
            campgroundWriter.writerow(["Name of Campground", "Electrical Campsites", "Boat Ramp", "Dog Friendly", "Wheelchair Accessible", "Nearest Trail", "Trail Difficulty", 
            "Distance to West Gate (km)", "Distance to East Gate (km)", "Distance to Trailer Sanitation Station (km)", "Distance to Visitor Centre (km)", "Reservation Link"])
            for index in range(len(campgroundName)):
                row = [campgroundName[index]] + [electricalCampsites[index]] + [boatRamp[index]] + [dogFriendly[index]] + [wheelchairAccessible[index]] + \
                    [trailName[index]] + [trailDifficulty[index]] + [westGateDistance[index]]  + [eastGateDistance[index]] + [trailerStationDistance[index]] + \
                        [visitorCentreDistance[index]] + [reservationLink[index]]
                campgroundWriter.writerow(row)
        print()
        print("A .csv file with more details about your top 3 campgrounds is available in the workspace folder. Happy camping!")
    except ValueError:
        print("Enter correct value as requested please")

if __name__ == "__main__":
    main()