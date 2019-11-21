# SCARLETT BOUZEID
# HOMEWORK 8 - BATCH REPROJECTION TOOL
# 11/08/2019

import arcpy
import os

# I know that this should be softcoded but I could not find anything on that
targetFC = r"H:\PythonGIS\Bouzeid\data1\USA.gdb"
MainFolder = r"H:\PythonGIS\Bouzeid\data1\USA.gdb"

DescribeTarget = arcpy.Describe(targetFC)
SpatialRefTarget = DescribeTarget.SpatialReference
SpatialRefNameTarget = SpatialRefTarget.Name


arcpy.env.workspace = MainFolder
FClist = arcpy.ListFeatureClasses()
print FClist

for FCcurrent in FClist:
    DescribeCurrentFC = arcpy.Describe(FCcurrent)
    FCSpatialRefcurrent = DescribeCurrentFC.SpatialReference
    FCSpatialRefNameCurrent = FCSpatialRefcurrent.Name

    if FCSpatialRefcurrent != SpatialRefNameTarget:
        print "Spatial references do NOT match."
    else:
        print "Spatial references do match."

    if FCSpatialRefNameCurrent == SpatialRefNameTarget:
        continue
    else:
        
        outCS = os.path.splitext(FCcurrent)[0] +"_projected.shp" 
        arcpy.Project_management(FCcurrent, outCS, SpatialRefTarget)
        print outCS
# I could not get the script to run. I did try several different ways to achieve batch re-projection
# but could not figure it out.

# Write Up
# This assignment was difficult. I learned that I batch projection is challenging and that
# more research needs to be done in order to understand how to softcode and hardcoding.
# I plan on showing up early on tuesday to class in order to try and get some answers about
# this assignment. 