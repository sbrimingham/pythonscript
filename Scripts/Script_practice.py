import arcpy
from arcpy import env
env.workspace = "H:\PythonGIS\Bouzeid\HMWK11_11_14_19\Exercise06"
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    fcdescribe = arcpy.Describe(fc)
    print "Name: " + fcdescribe.name
    print "Data type: " + fcdescribe.dataType


    