import arcpy, sys

# Set workspace
arcpy.env.workspace = "V:\\ENV859_PS4\\Data"

# Enable existing ArcPy outputs to be overwritten
arcpy.env.overwriteOutput = True

# Ensure ArcPy product edition used is ArcInfo, if not, cease processing
if arcpy.CheckProduct("ArcInfo") == 'Available':
    # create a list of all 5 feature classes that start with "BMR"
    BMR_featureclass = arcpy.ListFeatureClasses('BMR*')
    
    # Loop through BMR feature classes 
    for bmr in BMR_featureclass:
        
        # Create folder for outputs in Scratch folder
        folder = f"v:\\ENV859_PS4\\Scratch\\Counties_in_{bmr}_"

        arcpy.CreateFolder_management("v:\\ENV859_PS4\\Scratch", f"Counties_in_{bmr}_")

        # Split feature class by county
        arcpy.Split_analysis(bmr, "TriCounties.shp", "CO_NAME", folder)

else:
    msg = "Proper license is not available"
    print(msg)
    sys.exit(msg)

