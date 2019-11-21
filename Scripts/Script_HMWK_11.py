

# 2

arcpy.Exists("hospitals.shp")
from arcpy import env
env.workspace = r"H:\PythonGIS\Bouzeid\HMWK11_11_14_19\Exercise05"

arcpy.Usage("Clip_analysis")
arcpy.Usage("Clip")

arcpy.Usage("Exists")
prjFile = "H:\PythonGIS\Bouzeid\HMWK11_11_14_19\Exercise05\facilities.prj"
spatial_ref = arcpy.SpatialReference(prjFile)
arcpy.DefineProjection_management("hospitals", spatial_ref)

print spatial_ref.XYResolution

# 3 Dissolve Tool on the parks.shp

import arcpy
from arcpy import env
env.workspace = r"H:\PythonGIS\Bouzeid\HMWK11_11_14_19\Exercise05"
env.overwriteOutput = True
arcpy.Dissolve_management("parks.shp", "parks_dissolve1.shp", "PARK_TYPE", "", "SINGLE_PART")

# 4

import arcpy
arcpy.CheckExtension("spatial")
if arcpy.CheckExtension("spatial") == "Available":
    print "Spatial Analyst extension is available"
    arcpy.CheckExtension("3D")
    if arcpy.CheckExtension("3D") == "Available":
        print "3D analyst and Spatial is available"
    else:
        print "3D analyst is not available"
    arcpy.CheckExtension("network")
    if arcpy.CheckExtension("network") == "Available":
        print "Network, 3d, and Spatial analyst is available"
    else:
        print "network analyst not available"
    
else:
    print "the extensions are not available"