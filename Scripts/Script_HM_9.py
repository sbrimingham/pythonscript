import arcpy
featureClass = r"H:\PythonGIS\Bouzeid\Homework_9\us_major_cities"
desc = arcpy.Describe(featureClass)
spatialRef = desc.SpatialReference #how to access feature class
print spatialRef.name

import arcpy
featureClass = r"H:\PythonGIS\Bouzeid\Homework_9\us_major_cities"
fieldList = arcy.ListFields(featureClass)

for field in fieldList: #loops through each field in the list
    print field.name 

#Cursor function

import arcpy
featureClass = r"H:\PythonGIS\Bouzeid\Homework_9\us_major_cities"
rows = arcpy.SearchCursor(featureClass) #create the search cursor
row = rows.next()

while row:
    print row.AREANAME
    row = rows.next() #moves on to the next rows until no more rows

#find the average population


import arcpy
featureClass = r"H:\PythonGIS\Bouzeid\Homework_9\us_major_cities" # I could not find the shapefile for counties
rows = arcpy.SearchCursor(featureClass) #create the search cursor
row = rows.next()

average = 0
totalPopulation = 0
recordsCounted = 0

#loop through each row and keep running

while row:
    totalPopulation += row.POP_98
    recordsCounted += 1
    row = rows.next()

average = totalPopulation / recordsCounted
print "Average population for a county is " + str(average)

# find the average using a similar method

import arcpy
featureClass = r"H:\PythonGIS\Bouzeid\Homework_9\us_major_cities"
populationField = "POP_98"

rows = arcpy.SearchCursor(featureClass) #create the search cursor
row = rows.next()

average = 0
totalPopulation = 0
recordsCounted = 0

while row:
    totalPopulation += row.getValue(populationField)
    recordsCounted += 1
    row = rows.next()

average = totalPopulation / recordsCounted
print "Average population for a county is " + str(average)

#finds the average population in a county

import arcpy
featureClass = arcpy.GetParameterAsText(0)
populationField = arcpy.GetParameterAsText(1)

rows = arcpy.SearchCursor(featureClass) #create the search cursor
row = rows.next()

average = 0
totalPopulation = 0
recordsCounted = 0

while row:
    totalPopulation += row.getValue(populationField)
    recordsCounted += 1
    row = rows.next()

average = totalPopulation / recordsCounted
print "Average population for a county is " + str(average)



#Use a loop with a cursor
# find the average population

import arcpy
featureClass = r"H:\PythonGIS\Bouzeid\Homework_9\us_major_cities"
populationField = "POP_98"
rows = arcpy.SearchCursor(featureClass)

average = 0
totalPopulation = 0
recordsCounted = 0

for rows in row:
    totalPopulation += row.getValue(populationField)
    recordscounted += 1

averge = totalPopulation / recordsCounted
print "Average population for a county is " + str(average)


import arcpy
featureClass = "C:\\Data\\UnitedStates.gdb\\PACities"
populationField = "POP_98"

average = 0
totalPopulation = 0
recordsCounted = 0

with arcpy.da.SearchCursor(featureClass,((populationField,)) as cursor:
    for row in cursor:
        totalPopulation += row[0]
        recordsCounted += 1

average = totalPopulation / recordsCounted
print "Average population for a county is " + str(average)

# Modify field values using existing records


import arcpy
fc = arcpy.GetParameterAsText(0)
affectedField = arcpy.GetParameterAsText(1)
oldValue = arcpy.GetParameterAsText(2)
newValue = arcpy.GetParameterAsText(3)

queryString = '"' + affectedField + '" = ' + "'" + oldValue + "'"

# Create the update cursor and advance the cursor to the first row

rows = arcpy.UpdateCursor(fc, queryString)
row = rows.next()

# Perform the update and move to the next row as long as there are rows left

while row:
row.setValue(affectedField, newValue)
rows.updateRow(row)
row = rows.next()

# Delete the cursors to remove any data locks

del row, rows

#Updating records using arcpy

import arcpy

# Retrieve input parameters: the feature class, the field

fc = arcpy.GetParameterAsText(0)
affectedField = arcpy.GetParameterAsText(1)
oldValue = arcpy.GetParameterAsText(2)
newValue = arcpy.GetParameterAsText(3)

queryString = '"' + affectedField + '" = ' + "'" + oldValue + "'"

# Create the update cursor and update each row returned by the SQL expression

with arcpy.da.UpdateCursor(fc, (affectedField,),
queryString) as cursor:
 for row in cursor:
 row[0] = newValue
 cursor.updateRow(row)

#Importing new records

import arcpy

inX = arcpy.GetParameterAsText(0)
inY = arcpy.GetParameterAsText(1)
inDescription = arcpy.GetParameterAsText(2)

incidentsFC = "C:/Data/Incidents.shp"
descriptionField = "DESCR"

inPoint = arcpy.Point(inX, inY)

rowInserter = arcpy.InsertCursor(incidentsFC)
newIncident = rowInserter.newRow()

newIncident.SHAPE = inPoint
newIncident.setValue(descriptionField, inDescription)

rowInserter.insertRow(newIncident)

del rowInserter


