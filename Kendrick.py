input_PreferenceList = [] # Create empty user preference list 

# Users input their preferences in the PreferenceList

print()
print("***************************************************************")
print("Question 1)")
print()
try:

while True:
        # Users' preference on their starting point
        startingpoint = str(input("Where would you like your starting point be? E = East Gate and W = West Gate:__  "))
        startingpoint = startingpoint.upper
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
        indistgate = int(input("How far would you want to travel to your campground? Under 20km: enter 1, Between 21 - 40km: enter 2, Over 40km: enter 3:__ "))
        if indistgate not in [1,2,3]:
            print("Invalid entry. Please enter 1, 2 or 3.")
        else:
            break 
print()
print("***************************************************************")
print("Question 3)")
print()
while True:
        # Users' preferences on electric campsites
        inelectricCampsite = int(input("Would you like your campground to have electrical hook-up? Yes: enter 1, No: enter 0:__ "))
    if inelectricCampsite not in [1,0]:
        print("Invalid entry. Please enter 1 (Yes) or 0 (No).")
    else:
        break

print()
print("***************************************************************")
print("Question 4)")
print()
while True:
        # Users' preferences on boat ramp
        inboatramp = int(input("Would you like the lakes at your campground to allow motor boat? Yes: enter 1, No: enter 0:__ "))
        if inboatramp not in [1,0]:    
            print("Invalid entry. Please enter 1 (Yes) or 0 (No).") 
        else:
            break
print()
print("***************************************************************")
print("Question 5)")
print()
while True:  
        # Users' preference on the distance to visitor centre
        inproxvisit = int(input("What is your preferred distance to the Visitor Centre? Under 20km: enter 1, Between 20 - 40km: enter 2, over 40km: enter 3:__ "))
        if inproxvisit not in [1,2,3]:
            print("Invalid entry. Please enter 1 (Yes) or 0 (No).")
        else:
            break
print()
print("***************************************************************")
print("Question 6)")
print()
while True:
        # Users' preference on the trails' difficulty
        intrailpref = int(input("What level of trail difficulty would you like to have in proximity to your campground? Easy: enter 1, Moderate: enter 2, Hard: enter 3:__ "))
        if trailpref not in [1,2,3]:
            print("Invalid entry. Please enter 1 (Easy), 2 (Moderate) or 3 (Hard).")
        else:
            break
print()
print("***************************************************************")
print("Question 7)")
print()
while True:
        # Users' preference on the distance to trailer station
        intrailerstation = int(input("What is your preferred distance to a trailer sanitation station?  Under 10km: enter 1, Between 11 - 20km: enter 2, over 21km: enter 3:__ "))
        if trailerstation not in [1,2,3]:
            print("Invalid entry. Please enter 1, 2 or 3.")
        else:
            break
print()
print("***************************************************************")
print()
# just to test if the above line runs properly
print("done")
print(indistgate, inelectricCampsite, inboatramp, inproxvisit, intrailpref, intrailerstation)
#rrappendtolist(indistgate, inelectricCampsite, inboatramp, inproxvisit, intrailpref, intrailerstation)



