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




# functions for use in program - Kate 

# main function for the entire program?
def main():

# function to append input values to campground preference list 
def appendtolist():
    PreferenceList = []                                                                                 # create empty list to store preferences
    PreferenceList.extend(distgate, electricCampsite, boatramp, proxvisit, trailpref, trailerstation)   # use the extend function to appending individual elements

# I think this function below needs to be simplified to remove the repetitiveness 

def EastGate(): 
    CampgroundEast = []  # do I need this?
    # likely need to refer to dictionary of each campground's values first to have something to compare to
    # need to fill this list with the preferences from user input?
    for i in range len(PreferenceList):                   # is this necessary if I'm using collections.counter?
        # comparison between PreferenceList and index list of campground in dictionary
        # if integer in this index is the same as the integer in this index 
        # use collection.counter() method
        # will need to import collections at the top of the code 
        if collections.Counter(PreferenceList) == collections.Counter(RockLake):
            # the lists are the same and this is a matching campground
        elif collections.Counter(PreferenceList) == collections.Counter(CoonLake):
            # the lists are the same 
        elif collections.Counter(PreferenceList) == collections.Counter(TeaLake):
            # the lists are the same
        elif collections.Counter(PreferenceList) == collections.Counter(CanisbayLake):
            # the lists are the same
        elif collections.Counter(PreferenceList) == collections.Counter(KearneyLake):
            # the lists are the same
        elif collections.Counter(PreferenceList) == collections.Counter(PogLake):
            # the lists are the same
        elif collections.Counter(PreferenceList) == collections.Counter(TwoRivers):
            # the lists are the smae
        elif collections.Counter(PreferenceList) == collections.Counter(MewLake):
            # the lists are the same
        else:
            # the lists are not the same




def WestGate(): 
    CampgroundWest = []
    for i in range len(PreferenceList):
        # comparison between PreferenceList and index list of campground in dictionary


# these are just notes I've made about input to get thinking organized
startgate = input("Which Gate are you going to enter at (W or E)? ")

if startgate = 'E':
    EastGate()
else: 
    WestGate()
# end of notes




    