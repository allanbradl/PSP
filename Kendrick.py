input_PreferenceList = [] # Create empty user preference list 

# Users input their preferences in the PreferenceList


while True:
    try:
        # Users' preference on their starting point
        startingpoint = str(input("Where would you like your starting point be? \
                           E = East Gate and W West Gate"))
    except:
        continue
    if startingpoint not in ["E","e","W","w"]:Ellipsis
        startingpoint = str(input("Where would you like your starting point be? \
                           E = East Gate and W West Gate"))
    else:
        break


while True:
    try:
        # Users' preferences on their distance from the starting point
        distgate = int(input("How far would you want to travel to your camp ground? Under 20km: enter 1, \
                              Between 21 - 40km: enter 2, Over 40km: enter 3 "))
    except ValueError:
        print("Please enter your preference: 1, 2 or 3.")
        continue
    if distgate not in [1,2,3]:
        distgate = int(input("How far would you want to travel to your camp ground? Under 20km: enter 1, \
                              Between 21 - 40km: enter 2, Over 40km: enter 3 "))
    else:
        break 


while True:
    try:
        # Users' preferences on electric campsites
        electricCampsite = int(input("Would you want your camp ground that has electric camp sites? \
                                      Yes: enter 1, No: enter 0 "))
    except ValueError:
        print("Please enter your preference: 1 or 0.")
        continue
    if electricCampsite not in [1,0]:
        electricCampsite = int(input("Would you want your camp ground that has electric camp sites? \
                                      Yes: enter 1, No: enter 0 "))
    else:
        break


while True:
    try:
        # Users' preferences on boat ramp
        boatramp = int(input("Would you want the lakes in your camp ground that allows motor boat? \
                              Yes: enter 1, No: enter 0 "))
    except ValueError:
        print("Please enter your preference: 1 or 0.")
        continue   
    if boatramp not in [1,0]:
        boatramp = int(input("Would you want the lakes in your camp ground that allows motor boat? \
                              Yes: enter 1, No: enter 0 "))
    else:
        break


while True:
    try:    
        # Users' preference on the distance to visitor centre
        proxvisit = int(input("How far would you like to have the Visitor Centre nearby? \
                               Under 20km: enter 1, Between 20 - 40km: enter 2, over 40km: enter 3 "))
    except ValueError:
        print("Please enter your preference: 1, 2 or 3.")
        continue                      
    if proxvisit not in [1,2,3]:
        proxvisit = int(input("How far would you like to have the Visitor Centre nearby? \
                               Under 20km: enter 1, Between 20 - 40km: enter 2, over 40km: enter 3 "))
    else:
        break


while True:
    try:
        # Users' preference on the trails' difficulty
        trailpref = int(input("What trail difficulty would you like to have in your camp ground? \
                               Easy: enter 1, Moderate: enter 2, Hard: enter 3 "))
    except ValueError:
        print("Please enter your preference: 1, 2 or 3.")
        continue
    if trailpref not in [1,2,3]:
        trailpref = int(input("What trail difficulty would you like to have in your camp ground? \
                               Easy: enter 1, Moderate: enter 2, Hard: enter 3 "))
    else:
        break

while True:
    try:
        # Users' preference on the distance to trailer station
        trailerstation = int(input("how far would you want a trailer station near your camp ground? \
                                    Under 10km: enter 1, Between 11 - 20km: enter 2, over 21km: enter 3"))
    except ValueError:
        print("Please enter your preference: 1, 2 or 3.")
        continue
    if trailerstation not in [1,2,3]:
        trailerstation = int(input("how far would you want a trailer station near your camp ground? \
                                    Under 10km: enter 1, Between 11 - 20km: enter 2, over 21km: enter 3"))
    else:
        break

# just to test if the above line runs properly
print("done")


