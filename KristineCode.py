# # GEOM 67 Group Project 
# # Name of Program: Alongquin Park Campground Selector
# # Authors: Kristine Luangkhot, James Serendip, Kathryn Little, Kendrick Lok 
# # Date last modified: 
# # Program Purpose: to conduct a site suitability analysis for a campground in Algonquin Provincial Park along the highway 60 corridor

# # Program Use: This program will be used by people looking to select a campground in Algonquin Park based on specific ranked criteria

# # Program Structure: 

# # Assumptions made: This program assumes that the user is only looking to book a campground along the Highway 60 corridor of Algonquin
# # Provincial Park in Ontario. It also assumes that elevation and ground level are not a factor, given these are established campgrounds
# # It also assumes that the user does not want group camping. We are assuming accuracy of data from Ontario Geohub and the Algonquin
# # Park main website. 

# # Planned for limitations: 

# # Inputs and outputs: Input data will be _____, the campsites that fit the suitability criteria will be written to a csv file 

# # References: Ontario Geohub (URL), Ontario Parks (URL)

# # Contribution of team members to implementation: 

# import csv

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
#              [trailName[index]] + [trailDifficulty[index]] + [eastGateDistance[index]] + [westGateDistance[index]]  + [trailerStationDistance[index]] + \
#                  [visitorCentreDistance[index]] + [reservationLink[index]]
#         campgroundWriter.writerow(row)

# input_PreferenceList = [] # Create empty user preference list 

# # Users input their preferences in the PreferenceList

# def appendtolist():
#     PreferenceList = []                                                                                 # create empty list to store preferences
#     PreferenceList.extend(distncegate, electricCampsites, boatramps, proximityvisit, trailpreference, trailerstations)   # use the extend function to appending individual elements
#     return PreferenceList

try:
    # # import arcpy and get connected to our geodatabase
    # import arcpy
    # from arcpy import env

    # arcpy.env.workspace = r"C:\Users\kris_\Desktop\PSP\Algonquin\CampgroundsData.gdb"

    # # set variable for feature class definition
    # featureClasses = arcpy.ListFeatureClasses()
    # campgrounds = featureClasses[0]
    # fieldName = [f.name for f in arcpy.ListFields("Campgrounds")]  # sets field names to scan through later 

    # # printing info to help view and construction ------ remove when ready!---------------
    # print(campgrounds)
    # print(" fields: " + str(fieldName))
    # print()
    # # ----------------------------------------this can be removed for final, but leaving in in case we want to view it later----------

    # # create empty dictionary for campsite info and empty string to hold values of fields for each site
    # sitesdict = {}

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

    while True:
        # Users' preference on their starting point
        startingpoint = str(input("Where would you like your starting point be? E = East Gate and W West Gate: "))
        startingpoint = startingpoint.upper()
        if startingpoint not in ["E", "W"]:
            print("Invalid entry. Please enter E or W.")
        else:
            break


    while True:
        # Users' preferences on their distance from the starting point
        distgate = str(input("How far would you want to travel to your camp ground? Under 20km: enter 1, Between 21 - 40km: enter 2, Over 40km: enter 3 "))
        if distgate not in ["1","2","3"]:
            print("Invalid entry. Please enter 1, 2 or 3.")
        else:
            break 


    while True:
        # Users' preferences on electric campsites
        electricCampsite = int(input("Would you want your camp ground that has electric camp sites? Yes: enter 1, No: enter 0 "))
        if electricCampsite not in [1,0]:
            print("Invalid entry. Please enter 1 (Yes) or 0 (No).")
        else:
            break


    while True:
        # Users' preferences on boat ramp
        boatramp = int(input("Would you want the lakes in your camp ground that allows motor boat? Yes: enter 1, No: enter 0 "))
        if boatramp not in [1,0]:
            print("Invalid entry. Please enter 1 (Yes) or 0 (No).")
        else:
            break


    while True:   
        # Users' preference on the distance to visitor centre
        proxvisit = int(input("How far would you like to have the Visitor Centre nearby? Under 20km: enter 1, Between 20 - 40km: enter 2, over 40km: enter 3 "))                   
        if proxvisit not in [1,2,3]:
            print("Invalid entry. Please enter 1 (Yes) or 0 (No).")
        else:
            break


    while True:
        trailpref = int(input("What trail difficulty would you like to have in your camp ground? Easy: enter 1, Moderate: enter 2, Hard: enter 3 "))
        if trailpref not in [1,2,3]:
            print("Invalid entry. Please enter 1 (Easy), 2 (Moderate) or 3 (Hard).")
        else:
            break

    while True:
        # Users' preference on the distance to trailer station
        trailerstation = int(input("how far would you want a trailer station near your camp ground? Under 10km: enter 1, Between 11 - 20km: enter 2, over 21km: enter 3"))
        if trailerstation not in [1,2,3]:
            print("Invalid entry. Please enter 1, 2 or 3.")
        else:
            break

    # just to test if the above line runs properly
    print("done")

except ValueError:
    print("Please enter your preference: 1 or 0.")