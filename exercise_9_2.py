# import modules
import arcpy
import os

# set workspace (ADD YOUR OWN WORKSPACE HERE!)
arcpy.env.workspace = r'C:\Users\lucah\OneDrive\Desktop\exercise_arcpy_1.gdb' #Pfad anpassen

# Path to active_assets
fc_path_assets = os.path.join(arcpy.env.workspace, 'active_assets')

# Add a helper filed 'Buffer_Distance' for later calculations
arcpy.management.AddField(fc_path_assets, 'Buffer_Distance', 'INTEGER')

# Buffer Dictionary 
buffer_distances = {
    'mast': 300,
    'mobile_antenna': 50,
    'building_antenna': 100
}

# Create UpdateCursor for active_assets
ucur = arcpy.da.UpdateCursor(in_table=fc_path_assets,field_names='*')

# Iterate though active_assets
for row in ucur:

    # Create entry for 'Buffer_Distance' by comparing the current type value with the Dictionary
    row[4] = buffer_distances[row[3]]

    # Update the row
    ucur.updateRow(row)

# Delete the UpdateCursor
del ucur

# Apply the Buffer-Tool: Create output-class 'coverage' and take the new field value 'Buffer_Distance' to choose the Distance for each feature
arcpy.analysis.Buffer(
    in_features="active_assets",
    out_feature_class=r"C:\Users\lucah\OneDrive\Desktop\exercise9\Default.gdb\coverage",
    buffer_distance_or_field="Buffer_Distance"
)
