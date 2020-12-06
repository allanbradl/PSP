import arcpy
from arcpy import env

arcpy.env.workspace = r"C:\Users\kris_\Desktop\PSP\Algonquin\CampgroundsData.gdb"

def appendtolist(distgate, electricCampsite, boatramp, proxvisit, trailpref, trailerstation):
    PreferenceList = []
    PreferenceList.extend([int(distgate), int(electricCampsite), int(boatramp), int(proxvisit), int(trailpref), int(trailerstation)])
    return PreferenceList

def EastGate(preflist):
    print("East Gate Function")
    # set variable for feature class definition
    sitematch = []
    featureClasses = arcpy.ListFeatureClasses()
    campgrounds = featureClasses[0]
    fieldName = [f.name for f in arcpy.ListFields("Campgrounds")] 
    # sitesdict = {}
    with arcpy.da.SearchCursor(campgrounds, fieldName) as cursor:
        for row in cursor:
            sitefields = [row[19], row[21], row[22], row[17], row[12], row[20]]
            sitesdict = {row[6]: sitefields}
            print(sitesdict)
            # print(row[6], row[18], row[21], row[22], row[17], row[12], row[20])
            # dictionary order is: KEY=campsite name, distance to West Gate, Distance to East Gate, electric,
            # boat ramp, distance to visitor centre, Trail difficulty, distance to sanitation station, 
            # siteoutputinfo = [row[7], row[8], row[9]]    #These fields not used in site selection but included in output: pet-friendly, wheelchair accessible, reservation URL
            if sitefields == preflist:
                sitematch.append(row[6])
    return sitematch


# def WestGate():
    # print("West Gate")
    # with arcpy.da.SearchCursor(campgrounds, fieldName) as cursor:
    # for row in cursor:
    #     # print(row[6], row[18], row[21], row[22], row[17], row[12], row[20])
    #     # dictionary order is: KEY=campsite name, distance to West Gate, Distance to East Gate, electric,
    #     # boat ramp, distance to visitor centre, Trail difficulty, distance to sanitation station, 
    #     siteoutputinfo = [row[7], row[8], row[9]]    #These fields not used in site selection but included in output: pet-friendly, wheelchair accessible, reservation URL
    #     sitefields = [row[18], row[21], row[22], row[17], row[12], row[20]]
    #     sitesdict = {row[6]: sitefields}
    #     print(sitesdict)  


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
    # else:
    #     WestGate()

except ValueError:
    print("Enter correct value as requested please")