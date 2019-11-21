# Scarlett Bouzeid
# Exercise 7 - Manipulating Spatial Data
# 11/22/2019

# printed all the names in the NAME column

##import arcpy
##from arcpy import env
##env.workspace = r"H:\PythonGIS\Bouzeid\HMWK12_11_20_19\Exercise07"
##fc = "airports.shp"
##cursor = arcpy.da.SearchCursor(fc, ["NAME"])
##for row in cursor:
##    print "Airport name = {0}".format(row[0])

# script created a search cursor o the feature class and uses a for loop
# to iterate over all the rows of the attribute table
#............

#Use search cursors with SQL in Python
# prints airports according to the number of passengers

##import arcpy
##from arcpy import env
##env.workspace = r"H:\PythonGIS\Bouzeid\HMWK12_11_20_19\Exercise07"
##fc = "airports.shp"
##cursor = arcpy.da.SearchCursor(fc, ["NAME"], '"TOT_ENP" > 100000')
### Field delimiters for shapefiles consist of double quotation marks
### but there are no quotation marks around the value of 100000 because TOT_ENP is a numeric field.
##for row in cursor:
##    print row[0]
##del row
##del cursor

#Modified SQL expression

##import arcpy
##from arcpy import env
##env.workspace = r"H:\PythonGIS\Bouzeid\HMWK12_11_20_19\Exercise07"
##fc = "airports.shp"
##cursor = arcpy.da.SearchCursor(fc, ["NAME"], '"FEATURE" = \'Seaplane Base\'')
##for row in cursor:
##    print row[0]
##del row
##del cursor

# 6 Modified SQL expression
# selected airpots only in the Anchorage Borough

##import arcpy
##from arcpy import env
##env.workspace = r"H:\PythonGIS\Bouzeid\HMWK12_11_20_19\Exercise07"
##fc = "airports.shp"
##delimitedField = arcpy.AddFieldDelimiters(fc, "COUNTY")
##cursor = arcpy.da.SearchCursor(fc, ["NAME"], delimitedField + " ='Anchorage Borough'")
##for row in cursor:
##        print row[0]
##del row
##del cursor
#....... Select.py


# 9  
import arcpy
from arcpy import env
env.workspace = r"H:\PythonGIS\Bouzeid\HMWK12_11_20_19\Exercise07"
infc = "airports.shp"
outfc = "Results/airports_anchorage.shp"

delimitedfield = arcpy.AddFieldDelimiters(infc, "COUNTY")
arcpy.Select_analysis(infc, outfc, delimitedfield + " = 'Anchorage Borough'")



