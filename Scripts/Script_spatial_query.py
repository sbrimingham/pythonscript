import arcpy
# different queries - attribute and location in arcMAP
# r" must use when using \ in file location
# if you don't use r".... then use double \\  or single /

# feature layer and feature class are different
# f layer = saves source file location and into your memory
# f class =

import arcpy
fc = r"H:\PythonGIS\Bouzeid\data1\USA.gdb\us_states"
arcpy.MakeFeatureLayer_management(fc,"all") #fc = in, all = out