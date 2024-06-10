# exercise 9.1
import arcpy
import os

arcpy.env.workspace = r'C:\Users\lucah\OneDrive\Desktop\exercise_arcpy_1.gdb' #Pfad anpassen

fc_list = arcpy.ListFeatureClasses(feature_type='Point')
fc_list.remove('active_assets')

fc_path_assets = os.path.join(arcpy.env.workspace, 'active_assets')

sql = "status='active'"

icur = arcpy.da.InsertCursor(in_table=fc_path_assets,field_names='*')
for fc in fc_list:
    
    fc_path = os.path.join(arcpy.env.workspace,fc)
    
    scur = arcpy.da.SearchCursor(in_table=fc_path,field_names='*',where_clause=sql)
    for row in scur:
        icur.insertRow(row)
del icur