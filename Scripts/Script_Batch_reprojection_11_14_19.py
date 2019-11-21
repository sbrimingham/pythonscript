import arcpy
fc = r"H:\PythonGIS\Bouzeid\data\Lesson1\geoportal.gdb\Fire" #old projection
target_prj = r"H:\PythonGIS\Bouzeid\data1\USA.gdb\TNoutline" #new projection
arcpy.Project_management(fc, r"H:\PythonGIS\Bouzeid\data\Lesson1\geoportal.gdb\Fire", target_prj)


