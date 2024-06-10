import arcpy
import os

arcpy.env.workspace = r'C:\Users\lucah\OneDrive\Desktop\exercise_arcpy_1.gdb' #Pfad anpassen

fc_path_assets = os.path.join(arcpy.env.workspace, 'active_assets')

arcpy.management.AddField(fc_path_assets, 'Buffer_Distance', 'INTEGER')

buffer_distances = {
    'mast': 300,
    'mobile_antenna': 50,
    'building_antenna': 100
}


ucur = arcpy.da.UpdateCursor(in_table=fc_path_assets,field_names='*')
for row in ucur:
    
    row[4] = buffer_distances[row[3]]
    ucur.updateRow(row)
del ucur

arcpy.analysis.Buffer(
    in_features="active_assets",
    out_feature_class=r"C:\Users\lucah\OneDrive\Desktop\exercise9\Default.gdb\coverage",
    buffer_distance_or_field="Buffer_Distance"
)
