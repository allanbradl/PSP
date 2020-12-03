# GEOM 67 Group Project 
# Name of Program: Alongquin Park Campground Selector
# Authors: Kristine Luangkhot, James Serendip, Kathryn Little, Kendrick Lok 
# Date last modified: 
# Program Purpose: to conduct a site suitability analysis for a campground in Algonquin Provincial Park along the highway 60 corridor

# Program Use: This program will be used by people looking to select a campground in Algonquin Park based on specific ranked criteria

# Program Structure: 

# Assumptions made: This program assumes that the user is only looking to book a campground along the Highway 60 corridor of Algonquin
# Provincial Park in Ontario. It also assumes that elevation and ground level are not a factor, given these are established campgrounds
# It also assumes that the user does not want group camping. We are assuming accuracy of data from Ontario Geohub and the Algonquin
# Park main website. 

# Planned for limitations: 

# Inputs and outputs: Input data will be _____, the campsites that fit the suitability criteria will be written to a csv file 

# References: Ontario Geohub (URL), Ontario Parks (URL)

# Contribution of team members to implementation: 

import csv

# Top 3 campgrounds selected based on user input and matches stored in a dictionary
campgroundSelection = {"Rock Lake": ["Yes", "Yes", "Yes", "Yes", "Booth's Rock Trail", "Difficult", "23.2 km", "49.2 km", "0 km", "11.5 km",
"https://reservations.ontarioparks.com/create-booking/results?resourceLocationId=-2147483555&mapId=-2147483264&searchTabGroupId=0&bookingCategoryId=0&startDate=2020-11-13T00:00:00.000Z&endDate=2020-11-14T00:00:00.000Z&nights=1&isReserving=true&equipmentId="], 
"Coon Lake": ["No", "No", "Yes", "No", "Centenial Ridges Trail", "Difficult", "20.9 km", "46.9 km", "1.5 km", "9.2 km",
"https://reservations.ontarioparks.com/create-booking/results?resourceLocationId=-2147483555&mapId=-2147483264&searchTabGroupId=0&bookingCategoryId=0&startDate=2020-11-13T00:00:00.000Z&endDate=2020-11-14T00:00:00.000Z&nights=1&isReserving=true&equipmentId="]}

# Create empty lists to hold individual dictionary items
campgroundName = []
electricalCampsites = []
boatRamp = []
dogFriendly = []
wheelchairAccessible = []
trailName = []
trailDifficulty = []
eastGateDistance = []
westGateDistance = []
trailerStationDistance = []
visitorCentreDistance = []
reservationLink = []

# Append individual dictionary items to empty list
# Every item appended is associated with the same key (campground name)
for akey in campgroundSelection:
    campgroundName.append(akey)
    electricalCampsites.append(campgroundSelection[akey][0])
    boatRamp.append(campgroundSelection[akey][1])
    dogFriendly.append(campgroundSelection[akey][2])
    wheelchairAccessible.append(campgroundSelection[akey][3])
    trailName.append(campgroundSelection[akey][4])
    trailDifficulty.append(campgroundSelection[akey][5])
    eastGateDistance.append(campgroundSelection[akey][6])
    westGateDistance.append(campgroundSelection[akey][7])
    trailerStationDistance.append(campgroundSelection[akey][8])
    visitorCentreDistance.append(campgroundSelection[akey][9])
    reservationLink.append(campgroundSelection[akey][10])

# Write output to a new text file
# Each row is one campground
with open("CampgroundSelection.csv", "w", newline="") as campground_final:
    campgroundWriter = csv.writer(campground_final)
    campgroundWriter.writerow(["Name of Campground", "Electrical Campsites", "Boat Ramp", "Dog Friendly", "Wheelchair Accessible", "Nearest Trail", "Trail Difficulty", 
    "Distance to East Gate", "Distance to West Gate", "Distance to Trailer Sanitation Station", "Distance to Visitor Centre", "Reservation Link"])
    for index in range(len(campgroundName)):
        row = [campgroundName[index]] + [electricalCampsites[index]] + [boatRamp[index]] + [dogFriendly[index]] + [wheelchairAccessible[index]] + \
             [trailName[index]] + [trailDifficulty[index]] + [eastGateDistance[index]] + [westGateDistance[index]]  + [trailerStationDistance[index]] + \
                 [visitorCentreDistance[index]] + [reservationLink[index]]
        campgroundWriter.writerow(row)
