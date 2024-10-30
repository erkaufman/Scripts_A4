# Import packages
import sys, os, arcpy
arcpy.env.overwriteOutput= True

# Set input variables
FeatureClass = arcpy.GetParameterAsText(0) # 'V:\\ENV859_PS4\\Data\\TriCounties.shp'   
Fieldname = arcpy.GetParameterAsText(1) # 'CO_NAME' 

# Create a point object
obsPoint = arcpy.Point()
obsPoint.X = 590000
obsPoint.Y = 230000

# Search cursor for designated feature class
rows = arcpy.da.SearchCursor(FeatureClass, ['Shape@', Fieldname])

# iteraete through features in feature class
for row in rows:
    recShape = row[0]
    # Does point fall within the record's shape?
    if recShape.contains(obsPoint) == True:
        # Attribute value of the field specified by the user
        uservalue = row[1]
        arcpy.AddMessage(f'The point is within {uservalue} county.')