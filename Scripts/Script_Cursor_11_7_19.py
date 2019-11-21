# Prints out Name of city, 1 row

import arcpy
from arcpy import env
env.workspace = r"H:\PythonGIS\Bouzeid\Homework_9"
env.overwriteOutput = True

fc = "us_major_cities.shp"
fieldName = "NAME"
print "worked"

rows = arcpy.SearchCursor(fc) #rows now cursor object
row = rows.next() #next method called from cursor object which retured row object

while row:
    print row.getValue(fieldName) #fieldname is cursor
    row = rows.next()

#Prints out 2 rows

import arcpy
from arcpy import env
env.workspace = r"H:\PythonGIS\Bouzeid\Homework_9"
env.overwriteOutput = True

fc = "us_major_cities.shp"
fieldName0 = "NAME"
fieldName1 = "POPULATION"
print "worked"

rows = arcpy.SearchCursor(fc) #rows now cursor object
# row = rows.next() Dont need

with arcpy.da.SearchCursor(fc, ("NAME", "POPULATION")) as cursor: #called this cursor as cursor, has diff syntex, NAME is data type for tuple
    for row in cursor:#for loop 
        print row[0], row[1] # row 1 is population

#

##for row in rows:
  ##  print row.getValue(fieldName0)
    

##while row:
  ##  print row.getValue(fieldName) #fieldname is cursor

# Calculate average population using arcpy.da.SearchCursor

import arcpy
from arcpy import env
env.workspace = r"H:\PythonGIS\Bouzeid\Homework_9"
env.overwriteOutput = True

fc = "us_major_cities.shp"
# when need to calculate pop, think about variables. First add variable to sum pop and then one to count the rows
total = 0
counts = 0


with arcpy.da.SearchCursor(fc, ("NAME", "POPULATION")) as cursor: #called this cursor as cursor, has diff syntex, NAME is data type for tuple
    for row in cursor:#for loop, defined how many rows. Row is now looking at tuple (name and pop)
        total += row[1] #integer
        counts += 1 #integer. If make 1.0 then answer will have decimal points

print "Average pop is:", total/counts
# can also write as -> print "Average pop is:" + str(total/counts)


#Update Cursor - change neme in attribute table

import arcpy
from arcpy import env
env.workspace = r"H:\PythonGIS\Bouzeid\Homework_9"
env.overwriteOutput = True

fc = "us_major_cities.shp"

with arcpy.da.UpdateCursor(fc, ("CAPITAL")) as cursor: #called this cursor as cursor, has diff syntex, NAME is data type for tuple
    for row in cursor:#for loop, defined how many rows. Row is now looking at tuple (name and pop)
        row[0]
# row[0] = "CAPITAL" would change the entire row into capital when there are only a few that need to be changed


# how to change capital in attribute table

import arcpy
from arcpy import env
env.workspace = r"H:\PythonGIS\Bouzeid\Homework_9"
env.overwriteOutput = True

fc = "us_major_cities.shp"
where = '"CAPITAL' == 'State' #1 = assigns a name and 2 == 
print where 

with arcpy.da.UpdateCursor(fc, ("CAPITAL")) as cursor: #called this cursor as cursor, has diff syntex, NAME is data type for tuple
    for row in cursor:#for loop, defined how many rows. Row is now looking at tuple (name and pop)
        row[0]

# syntex error is usually a type-o






