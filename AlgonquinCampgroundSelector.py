# Name of Program: Alongquin Park Campground Selector
# Authors: Kristine Luangkhot, James Serendip, Kathryn Little, Kendrick Lok 
# Date last modified: December 8, 2020
# Program Purpose: to conduct a site suitability analysis for a campground in Algonquin Provincial Park along the Highway 60 Corridor

# Program Use: This program will be used by people looking to select a campground in Algonquin Park based on specific ranked criteria

# Program Structure: 
# Input Section: User will be asked for inputs for various criterion involved in selecting a campsite
# Main Program: User inputs are appended to a preference list and are compared to value lists for each campground in either an EastGate
#               Function or WestGate Function depending on the user's preferred entrance gate. 
# Output Section: Up to three matching campgrounds are written to a CSV File with extra information about each campground, including
#                 a link to the Ontario Parks Reservation Website

# Assumptions made: This program assumes that the user is only looking to book a campground along the Highway 60 corridor of Algonquin
#                   Provincial Park in Ontario. It also assumes that elevation and ground level are not a factor, given these are 
#                   established campgrounds. It also assumes that the user does not want group camping. 
#                   We are assuming accuracy of data from Ontario Geohub and the Algonquin Park main website. 

# Planned for limitations: this program does not work for backcountry campsite selection, only considers campgrounds along the Highway
#                          60 corridor

# Special cases and known problems: None

# Input: Input data will be user input appended to a list
# Output: Results will be output as 1) an on-screen output 2) a maximum of three fully or partially campgrounds 
#         matching the preference criteria to a CSV file 

# References: Ontario Geohub (https://geohub.lio.gov.on.ca/), Ontario Parks (https://www.ontarioparks.com/reservations)
#             Algonquin Park Corridor Map (https://www.algonquinpark.on.ca/visit/camping/highway-60-corridor.php)

# Contribution of team members to implementation:  
# Logic Flow: Kendrick
# Inputs: Kendrick, James, Kristine, Kathryn 
# Functions: Kathryn, James, Kristine
# Arcpy: James, Kristine
# Output: Kristine
# Documentation: Kathryn 

import arcpy                # to access campgrounds feature class
from arcpy import env
import csv                  # to write outputs to a text file
import os                   # to set relative path for the application

# Creates a list of all user inputs preferences
# Will be use to calculate a matching score then compared against the dictionary
def AppendToList(distanceGate, electricCampsite, boatRamp, proximityVisit, trailPreference, trailerStation):
    PreferenceList = []
    PreferenceList.extend([int(distanceGate), int(electricCampsite), int(boatRamp), int(proximityVisit), int(trailPreference), int(trailerStation)])
    return PreferenceList

# If user selects to start from the east gate, this is the function that will be used to calculate match scores
# Uses arcpy SearchCursor to read each field per row in the feature class of campgrounds
# Compares each item in each row to the preference list
# Creates a score from 0 to 6 for each campground to indicate how well the preference list matches each campground in the geodatabase
# Only the 3 campgrounds with the highest score will be returned to the main function
# Embedded lists: each item is a list with the score and name of the camgground
def EastGate(userPreferenceList):
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

# If user selects to start from the west gate, this is the function that will be used to calculate match scores
# Uses arcpy SearchCursor to read each field per row in the feature class of campgrounds
# Compares each item in each row to the preference list
# Creates a score from 0 to 6 for each campground to indicate how well the preference list matches each campground in the geodatabase
# Only the 3 campgrounds with the highest score will be returned to the main function
# Embedded lists: each item is a list with the score and name of the camgground
def WestGate(userList):
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

# Creates a dictionary where the keys are the names of all 8 campgrounds and values are a list of attributes for each campground
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

    try:
        # Set the workspace environment to a relative path
        # Will work as long as CampgroundsData.gdb and AlgonquinCampgroundSelector.py are located in the same workspace folder
        cwd = os.getcwd()
        arcpy.env.workspace = cwd + r"\CampgroundsData.gdb"
    
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
        print("In your results, a score of 6 indicates a perfect match. For each unmatched criteria, the score decreases by 1.")
        print()
        print("There are two gates for entry to the park along the Highway 60 corridor; East and West.")
        print()
        print("The East Gate is located near Whitney, ON. The West Gate is located 42.8 km east of Huntsville.")
        # Set answer to Y at the beginning so program will move into inputs immediately
        answer = "Y"

        # Input Section: 
        # Users input their preferences and each preference gets stored in a variable
        # Users must enter an appropriate answer to each question for the application to continue
        # If user input is not in the list of appropriate values for each question the user will be prompted to try again
        while answer == "Y":
            print()
            print("***************************************************************")
            print("Question 1)")
            print()
            while True:
                    # Users' indicate their starting point
                    startingPoint = str(input("Where would you like your starting point be? E = East Gate and W = West Gate:__  "))
                    startingPoint = startingPoint.upper()
                    if startingPoint not in ["E","W"]:
                        print("Invalid entry. Please enter E or W.")
                    else:
                        break
            print()
            print("***************************************************************")
            print("Question 2)")
            print()
            while True:
                    # Users' preferences on their distance from the starting point
                    inputDistanceGate = str(input("How far would you want to travel to your campground? Under 20km: enter 1, Between 21 - 40km: enter 2, Over 40km: enter 3:__ "))
                    if inputDistanceGate not in ["1","2","3"]:
                        print("Invalid entry. Please enter 1, 2 or 3.")
                    else:
                        break 
            print()
            print("***************************************************************")
            print("Question 3)")
            print()
            while True:
                # Users' preferences on electric campsites
                inputElectric = str(input("Would you like your campground to have electrical hook-up? Yes: enter 1, No: enter 0:__ "))
                if inputElectric not in ["1","0"]:
                    print("Invalid entry. Please enter 1 (Yes) or 0 (No).")
                else:
                    break

            print()
            print("***************************************************************")
            print("Question 4)")
            print()
            while True:
                    # Users' preferences on boat ramp
                    inputBoat = str(input("Would you like your campground to have a boat ramp? Yes: enter 1, No: enter 0:__ "))
                    if inputBoat not in ["1","0"]:    
                        print("Invalid entry. Please enter 1 (Yes) or 0 (No).") 
                    else:
                        break
            print()
            print("***************************************************************")
            print("Question 5)")
            print()
            while True:  
                    # Users' preference on the distance to visitor centre
                    inputVisitor = str(input("What is your preferred distance to the Visitor Centre? Under 20km: enter 1, Between 20 - 40km: enter 2, over 40km: enter 3:__ "))
                    if inputVisitor not in ["1","2","3"]:
                        print("Invalid entry. Please enter 1 (Yes) or 0 (No).")
                    else:
                        break
            print()
            print("***************************************************************")
            print("Question 6)")
            print()
            while True:
                    # Users' preference on the trails' difficulty
                    inputDifficulty = str(input("What level of trail difficulty would you like to have in proximity to your campground? Easy: enter 1, Moderate: enter 2, Hard: enter 3:__ "))
                    if inputDifficulty not in ["1","2","3"]:
                        print("Invalid entry. Please enter 1 (Easy), 2 (Moderate) or 3 (Hard).")
                    else:
                        break
            print()
            print("***************************************************************")
            print("Question 7)")
            print()
            while True:
                    # Users' preference on the distance to trailer station
                    inputTrailer = str(input("What is your preferred distance to a trailer sanitation station?  Under 10km: enter 1, Between 11 - 20km: enter 2, over 21km: enter 3:__ "))
                    if inputTrailer not in ["1","2","3"]:
                        print("Invalid entry. Please enter 1, 2 or 3.")
                    else:
                        break
        
            print()
            print("***************************************************************")
            print()

            # User inputs appended to one list by calling the AppendToList function
            userPreference = AppendToList(inputDistanceGate, inputElectric, inputBoat, inputVisitor, inputDifficulty, inputTrailer)

            # If user is starting from the east gate, call the function EastGate to calculate scores for each campground
            # userPreference list passed into the EastGate function
            # Top 3 campgrounds with the highest match score returned from the function are stored as a list in FinalGateResult
            # Top 3 campgrounds with the highest scores will be displayed on screen as a table
            if startingPoint=="E":
                FinalGateResult = EastGate(userPreference)
                print("Your top 3 matches are: ")
                print()
                print("Campground Name\t\t\t\t\tMatch Score")
                for index in range(len(FinalGateResult)):
                    matchName = FinalGateResult[index][1]
                    matchScore = FinalGateResult[index][0]
                    print(f'{matchName:<30}\t\t\t\t{matchScore}')
            # If user is starting from the west gate, call the function WestGate to calculate scores for each campground
            # userPreference list passed into the WestGate function
            # Top 3 campgrounds with the highest match score returned from the function are stored as a list in FinalGateResult
            # Top 3 campgrounds with the highest scores will be displayed on screen as a table
            else:
                FinalGateResult = WestGate(userPreference)
                print("Your top 3 matches are: ")
                print()
                print("Campground Name\t\t\t\t\tMatch Score")
                for index in range(len(FinalGateResult)):
                    matchName = FinalGateResult[index][1]
                    matchScore = FinalGateResult[index][0]
                    print(f'{matchName:<30}\t\t\t\t{matchScore}')
            print()
            print("***************************************************************")
            print()
            # Ask user if they want to run the program again
            answer = input("Do you want to run the campground selector again (Y/N)? ")
            answer = answer.upper()
        
        # Output Section:
        # Create empty lists to hold individual dictionary items
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

        # All eight campgrounds and their associated attributes are stored in one dictionary called allCampgrounds
        # campSelectionName is the name of the campground with the highest score - stored in index position 1 for each embedded list (3 total)
        # If the campground name in FinalGateResult is a key in the allCampgrounds dictionary, add this campground to the result
        # Append individual dictionary items to empty lists
        # Every item appended is associated with the same key (campground name)
        # Each list has 3 items
        allCampgrounds = GateDictionary()
        for index in range(len(FinalGateResult)):
            campSelectionName = FinalGateResult[index][1]
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


        # Write output to a new text (.csv) file
        # Append list items as one row
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
    except KeyError:
        print("Campground does not exist. ")
    except FileNotFoundError:
        print("CampgroundsData.gdb geodatabase not found. Please move geodatabase into the same folder as the application file.")
    except IndexError:
        print("List item not found.")
    except IOError:
        print("Problem with file structure. Please make sure database and application are in the original folder.")
    except ImportError:
        print("Missing library. Please make sure you have arcpy, csv and os libraries available.")
    except RuntimeError:
        print("There has been an error. Please try again.")

if __name__ == "__main__":
    main()