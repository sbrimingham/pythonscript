# Scarlett Bouzeid
# Homework 11 - exercise 6
# 11/15/19

# Challenge Question 1

##import arcpy
##from arcpy import env
##env.workspace = "H:\PythonGIS\Bouzeid\HMWK11_11_14_19\Exercise06"
##fclist = arcpy.ListFeatureClasses()
##for fc in fclist:
##    fcdescribe = arcpy.Describe(fc)
##    print "Name: " + fcdescribe.name
##    print "Data type: " + fcdescribe.dataType
##
##Name: amtrak_stations.shp
##Data type: ShapeFile
##Name: cities.shp
##Data type: ShapeFile
##Name: counties.shp
##Data type: ShapeFile
##Name: new_mexico.shp
##Data type: ShapeFile
##Name: railroads.shp
##Data type: ShapeFile

# Challenge Question 2

import arcpy
from arcpy import env
env.workspace = r"H:\PythonGIS\Bouzeid\HMWK11_11_14_19\Exercise06"
fcClasses = arcpy.ListFeatureClasses("Polygon")
arcpy.CreateFileGDB_management(r"H:\PythonGIS\Bouzeid\HMWK11_11_14_19\Exercise06\Results", "CopyPoly1.gdb")
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    fcdesc = arcpy.Describe(fc)
    arcpy.CopyFeatures_management(fc, r"H:/PythonGIS/Bouzeid/HMWK11_11_14_19/Exercise06/Results/CopyPoly1.gdb/" + fcdesc.basename) 

