import arcpy
from arcpy import env
env.workspace = r"H:\PythonGIS\youngsang\data\data\geoportal.gdb"
env.overwriteOutput = True
outDir = r"H:\PythonGIS\youngsang\data\data"
#arcpy.CreateFileGDB_management(outDir, "out.gdb")
outDir1 = r"H:\PythonGIS\youngsang\data\data\out.gdb\\"

fcList = arcpy.ListFeatureClasses(feature_type= "Point")
print fcList
clipFc = "polygon"
for item in fcList:
    print outDir1 + item
    arcpy.Clip_analysis(item, clipFc, outDir1 + item + "_clip")
    print item + " is now processing"
