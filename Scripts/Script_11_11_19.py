# Cursor function  and printing different variables from the attribute table
# 11/11/2019

import arcpy
fc = r"H:\PythonGIS\Bouzeid\Lesson1\us_cities.shp" #run before adding any further lines
with arcpy.da.SearchCursor(fc,("NAME")) as cursor: #creating cursor for table fc
    for row in cursor:
        print row[0]

# print more in the att table
import arcpy
fc = r"H:\PythonGIS\Bouzeid\Homework_9\us_major_cities.shp" #run before adding any further lines
where = '"POPULATION" > 950000' # this is the addition of the where_clause
print where

with arcpy.da.SearchCursor(fc,("NAME"),where_clause = where) as cursor: #creating cursor for table fc
    for row in cursor:
        print row[0]

# prints San diago

import arcpy
fc = r"H:\PythonGIS\Bouzeid\Homework_9\us_major_cities.shp" #run before adding any further lines
where = '"POPULATION" > 950000' # this is the addition of the where_clause
where1 = """"NAME" == 'San Diago'""" #prints san diago, """ is a truple
print where

with arcpy.da.SearchCursor(fc,("NAME"),where_clause = where) as cursor: #creating cursor for table fc
    for row in cursor:
        print row[0]

# prints name and population of cities starting with S under 950,000 population

import arcpy
fc = r"H:\PythonGIS\Bouzeid\Homework_9\us_major_cities.shp" #run before adding any further lines
where = '"POPULATION" > 950000' #prints cities under this poplation 
where1 = """"NAME" Like'S%'""" #prints cities with S name
print where 

with arcpy.da.SearchCursor(fc,("NAME", "POPULATION", "SHAPE@X"),where_clause = where) as cursor: #creating cursor for table fc
    for row in cursor:                              # Shape@X prints latitude
        print row[0], row[1], row[2] #row 1 is name, row 2 is population



# Changes state to State Capital in attribute table

import arcpy
fc = r"H:\PythonGIS\Bouzeid\Homework_9\us_major_cities.shp" 
with arcpy.da.UpdateCursor(fc,("CAPITAL"),where) as cursor: # this updates the capital name to State Capital
    for row in cursor: #Loop function
        row [0] = "State Capital"
        cursor.updateRow(row)




