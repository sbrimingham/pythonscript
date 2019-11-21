import arcpy
from arcpy import env
env.workspace = r"H:\PythonGIS\Bouzeid\data1\USA.gdb\us_cities"

arcpy.CreateFeatureclass_management(env.workspace, "insertPoint2", template = "Fire", spatial_reference = "Fire")

inX = 790000
inY = 325367
fc = "insertPoint2"
colname = "Facility_Zip"
inPoint = arcpy.Point(inX, inY)
rowInsert = arcpy.InsertCursor(fc) # line is ready to create new row
newIncident = rowInserter.newRow() #create row object

newIncident.SHAPE = inPoint
newIncident.setValue(colname, "value Inserted")

rowInserter.insertRow(newincident)

# Will soft code later
# get parameter as text = potential to convert into script tool, 