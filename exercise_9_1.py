# exercise 9.1

# import modules
import arcpy
import os


# set workspace (SET YOUR OWN WORKING DIRECTORY)
arcpy.env.workspace = r'C:\Users\lucah\OneDrive\Desktop\exercise_arcpy_1.gdb' 

# Access all feature classes
fc_list = arcpy.ListFeatureClasses(feature_type='Point')

# Remove active_assets from the list, because we dont want to iterate through this feature class
fc_list.remove('active_assets')

# create path to active_assets
fc_path_assets = os.path.join(arcpy.env.workspace, 'active_assets')

# sql filter statement
sql = "status='active'"

# create InsertCursor for active_assets
icur = arcpy.da.InsertCursor(in_table=fc_path_assets,field_names='*')

# iterate through feature classes
for fc in fc_list:

    # set path for current feature class
    fc_path = os.path.join(arcpy.env.workspace,fc)

    # searchCursor for current feature class with defined sql filter
    scur = arcpy.da.SearchCursor(in_table=fc_path,field_names='*',where_clause=sql)
    for row in scur:
        # insert row into active_assets
        icur.insertRow(row)
# delete InsertCursor
del icur
