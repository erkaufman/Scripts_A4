import arcpy, sys

# Set workspace
arcpy.env.workspace = "V:\\ENV859_PS4\\Data"

# Enable existing ArcPy outputs to be overwritten
arcpy.env.overwriteOutput = True

# Path to Roads.shp
road_path = "Roads.shp"
road_types_string = "0;201;203"

# iterate through road types
for road in road_types_string.split(';'):
    # Set local variables
    where_clause = f'ROAD_TYPE = {road}'
    out_feature_class = f"V:\\ENV859_PS4\\Scratch\\roads_{road}.shp"

    # Execute Select
    arcpy.Select_analysis(road_path, out_feature_class, where_clause)