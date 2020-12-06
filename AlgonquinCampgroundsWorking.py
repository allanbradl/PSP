# GEOM 67 Group Project 
# Name of Program: Alongquin Park Campground Selector
# Authors: Kristine Luangkhot, James Serendip, Kathryn Little, Kendrick Lok 
# Date last modified: December 6, 2020
# Program Purpose: to conduct a site suitability analysis for a campground in Algonquin Provincial Park along the highway 60 corridor

# Program Use: This program will be used by people looking to select a campground in Algonquin Park based on specific ranked criteria

# Program Structure: 

# Assumptions made: This program assumes that the user is only looking to book a campground along the Highway 60 corridor of Algonquin
# Provincial Park in Ontario. It also assumes that elevation and ground level are not a factor, given these are established campgrounds
# It also assumes that the user does not want group camping. We are assuming accuracy of data from Ontario Geohub and the Algonquin
# Park main website. 

# Planned for limitations: this program does not work for backcountry campsite selection, only considers campgrounds along the highway
# 60 corridor

# Special cases and known problems: 

# Inputs and outputs: Input data will be user input appended to a list
# the campsites that fit the suitability criteria will be written to a csv file 

# References: Ontario Geohub (URL), Ontario Parks (URL)

# Contribution of team members to implementation: 


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
    #appendtolist(indistgate, inelectricCampsite, inboatramp, inproxvisit, intrailpref, intrailerstation)

except ValueError:
    print("Enter correct value as requested please")

# Main Program: 


# Output Section: 
