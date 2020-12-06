import operator
import arcpy
from arcpy import env

arcpy.env.workspace = r"C:\PSP\GroupProject\Algonquin\Algonquin\PSPgrp\CampgroundsData.gdb"

def appendtolist(distgate, electricCampsite, boatramp, proxvisit, trailpref, trailerstation):
    PreferenceList = []
    PreferenceList.extend([int(distgate), int(electricCampsite), int(boatramp), int(proxvisit), int(trailpref), int(trailerstation)])
    return PreferenceList

def EastGate(preflist):
    print("East Gate Function")
    # set variable for feature class definition
    sitematch = {}
    featureClasses = arcpy.ListFeatureClasses()
    campgrounds = featureClasses[0]
    fieldName = [f.name for f in arcpy.ListFields("Campgrounds")] 
    
    # sitesdict = {}
    
    with arcpy.da.SearchCursor(campgrounds, fieldName) as cursor:
        for row in cursor:
            sitefields = [row[19], row[21], row[22], row[17], row[12], row[20]]
            sitesdict = {row[6]: sitefields}
            print(sitesdict)
            ranker = 0
            # print(row[6], row[18], row[21], row[22], row[17], row[12], row[20])
            # dictionary order is: KEY=campsite name, distance to West Gate, Distance to East Gate, electric,
            # boat ramp, distance to visitor centre, Trail difficulty, distance to sanitation station, 
            # siteoutputinfo = [row[7], row[8], row[9]]    #These fields not used in site selection but included in output: pet-friendly, wheelchair accessible, reservation URL
            if sitefields == preflist:
                rank = 3
                sitematch.update({row[6]: rank})
            else:
                
                for i in range(len(sitefields)):
                    if sitefields[i] == preflist[i]:
                        ranker += 1
                        rank = ranker-3
                        print(rank)
                        print(row[6])
                        sitematch.update({row[6]: rank})
                                

    sorted_sitematch = dict(sorted(sitematch.items(), key=operator.itemgetter(1),reverse=True))
    sort_match = sorted_sitematch.items()
    top_match = list(sort_match)[:3]
    return top_match


def WestGate(preflist):
    print("West Gate")
    sitematch = []
    featureClasses = arcpy.ListFeatureClasses()
    campgrounds = featureClasses[0]
    fieldName = [f.name for f in arcpy.ListFields("Campgrounds")] 
    with arcpy.da.SearchCursor(campgrounds, fieldName) as cursor:
        for row in cursor:
            sitefields = [row[18], row[21], row[22], row[17], row[12], row[20]]
            sitesdict = {row[6]: sitefields}
            print(sitesdict)
            # print(row[6], row[18], row[21], row[22], row[17], row[12], row[20])
            # dictionary order is: KEY=campsite name, distance to West Gate, Distance to East Gate, electric,
            # boat ramp, distance to visitor centre, Trail difficulty, distance to sanitation station, 
            # siteoutputinfo = [row[7], row[8], row[9]]    #These fields not used in site selection but included in output: pet-friendly, wheelchair accessible, reservation URL
            if sitefields == preflist:
                sitematch.append(row[6])
    return sitematch
          


    # sets field names to scan through later 

# # printing info to help view and construction ------ remove when ready!---------------
# print(campgrounds)
# print(" fields: " + str(fieldName))
# print()
# # ----------------------------------------this can be removed for final, but leaving in in case we want to view it later----------

# # loop through the feature class attribute table and assign evaluation criteria field values to each campsite (key)
# with arcpy.da.SearchCursor(campgrounds, fieldName) as cursor:
#     for row in cursor:
#         # print(row[6], row[18], row[21], row[22], row[17], row[12], row[20])
#         # dictionary order is: KEY=campsite name, distance to West Gate, Distance to East Gate, electric,
#         # boat ramp, distance to visitor centre, Trail difficulty, distance to sanitation station, 
#         siteoutputinfo = [row[7], row[8], row[9]]    #These fields not used in site selection but included in output: pet-friendly, wheelchair accessible, reservation URL
#         sitefields = [row[18], row[19], row[21], row[22], row[17], row[12], row[20]]
#         sitesdict = {row[6]: sitefields}
#         print(sitesdict)     

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
    # just to test if the above line runs properly
    print("done")
    print(indistgate, inelectricCampsite, inboatramp, inproxvisit, intrailpref, intrailerstation)
    userPreference = appendtolist(indistgate, inelectricCampsite, inboatramp, inproxvisit, intrailpref, intrailerstation)
    print(userPreference)



    if startingpoint=="E":
        EastGateResult = EastGate(userPreference)
        print(EastGateResult)
    else:
        WestGateResult = WestGate(userPreference)
        print(WestGateResult)

    # # Top 3 campgrounds selected based on user input and matches stored in a dictionary
    # campgroundSelection = {"Rock Lake": ["Yes", "Yes", "Yes", "Yes", "Booth's Rock Trail", "Difficult", "23.2 km", "49.2 km", "0 km", "11.5 km",
    # "https://reservations.ontarioparks.com/create-booking/results?resourceLocationId=-2147483555&mapId=-2147483264&searchTabGroupId=0&bookingCategoryId=0&startDate=2020-11-13T00:00:00.000Z&endDate=2020-11-14T00:00:00.000Z&nights=1&isReserving=true&equipmentId="], 
    # "Coon Lake": ["No", "No", "Yes", "No", "Centenial Ridges Trail", "Difficult", "20.9 km", "46.9 km", "1.5 km", "9.2 km",
    # "https://reservations.ontarioparks.com/create-booking/results?resourceLocationId=-2147483555&mapId=-2147483264&searchTabGroupId=0&bookingCategoryId=0&startDate=2020-11-13T00:00:00.000Z&endDate=2020-11-14T00:00:00.000Z&nights=1&isReserving=true&equipmentId="]}

    # # Create empty lists to hold individual dictionary items
    # campgroundName = []
    # electricalCampsites = []
    # boatRamp = []
    # dogFriendly = []
    # wheelchairAccessible = []
    # trailName = []
    # trailDifficulty = []
    # eastGateDistance = []
    # westGateDistance = []
    # trailerStationDistance = []
    # visitorCentreDistance = []
    # reservationLink = []

    # # Append individual dictionary items to empty list
    # # Every item appended is associated with the same key (campground name)
    # for akey in campgroundSelection:
    #     campgroundName.append(akey)
    #     electricalCampsites.append(campgroundSelection[akey][0])
    #     boatRamp.append(campgroundSelection[akey][1])
    #     dogFriendly.append(campgroundSelection[akey][2])
    #     wheelchairAccessible.append(campgroundSelection[akey][3])
    #     trailName.append(campgroundSelection[akey][4])
    #     trailDifficulty.append(campgroundSelection[akey][5])
    #     eastGateDistance.append(campgroundSelection[akey][6])
    #     westGateDistance.append(campgroundSelection[akey][7])
    #     trailerStationDistance.append(campgroundSelection[akey][8])
    #     visitorCentreDistance.append(campgroundSelection[akey][9])
    #     reservationLink.append(campgroundSelection[akey][10])

    # # Write output to a new text file
    # # Each row is one campground
    # with open("CampgroundSelection.csv", "w", newline="") as campground_final:
    #     campgroundWriter = csv.writer(campground_final)
    #     campgroundWriter.writerow(["Name of Campground", "Electrical Campsites", "Boat Ramp", "Dog Friendly", "Wheelchair Accessible", "Nearest Trail", "Trail Difficulty", 
    #     "Distance to East Gate", "Distance to West Gate", "Distance to Trailer Sanitation Station", "Distance to Visitor Centre", "Reservation Link"])
    #     for index in range(len(campgroundName)):
    #         row = [campgroundName[index]] + [electricalCampsites[index]] + [boatRamp[index]] + [dogFriendly[index]] + [wheelchairAccessible[index]] + \
    #             [trailName[index]] + [trailDifficulty[index]] + [eastGateDistance[index]] + [westGateDistance[index]]  + [trailerStationDistance[index]] + \
    #                 [visitorCentreDistance[index]] + [reservationLink[index]]
    #         campgroundWriter.writerow(row)
except ValueError:
    print("Enter correct value as requested please")