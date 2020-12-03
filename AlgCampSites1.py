# AlgCampSites1

# get connected to our geodatabase
import arcpy
from arcpy import env

env.workspace = r"C:\PSP\GroupProject\Algonquin\Algonquin\PSPgrp\CampgroundsData.gdb"


fieldList = arcpy.ListFields("Campgrounds")
for field in fieldList:

     print(field.name)  
print()
