# AlgCampSites1
# created by James Serendip Dec 2020 for GEOM 67 PSP Final Project


# import arcpy and get connected to our geodatabase
import arcpy
from arcpy import env

arcpy.env.workspace = r"C:\PSP\GroupProject\Algonquin\Algonquin\PSPgrp\CampgroundsData.gdb"

# set variable for feature class definition
featureClasses = arcpy.ListFeatureClasses()
campgrounds = featureClasses[0]
fieldName = [f.name for f in arcpy.ListFields("Campgrounds")]  # sets field names to scan through later 

# printing info to help view and construction ------ remove when ready!---------------
print(campgrounds)
print(" fields: " + str(fieldName))
print()
# ----------------------------------------this can be removed for final, but leaving in in case we want to view it later----------

# create empty dictionary for campsite info and empty string to hold values of fields for each site
sitesdict = {}

# loop through the feature class attribute table and assign evaluation criteria field values to each campsite (key)
with arcpy.da.SearchCursor(campgrounds, fieldName) as cursor:
    for row in cursor:
         # print(row[6], row[18], row[21], row[22], row[17], row[12], row[20])
         # dictionary order is: KEY=campsite name, distance to West Gate, Distance to East Gate, electric,
         # boat ramp, distance to visitor centre, Trail difficulty, distance to sanitation station, 
         siteoutputinfo = [row[7], row[8], row[9]]    #These fields not used in site selection but included in output: pet-friendly, wheelchair accessible, reservation URL
         sitefields = [row[18], row[19], row[21], row[22], row[17], row[12], row[20]]
         sitesdict = {row[6]: sitefields}
         print(sitesdict)      

