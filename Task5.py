# Import packages
import sys, os, arcpy
arcpy.env.overwriteOutput= True

# Set input variables
FeatureClass = 'V:/ARGOSTracking/Scratch/ARGOSTrack.shp'   #arcpy.GetParameterAsText(0)
Fieldname = '' #arcpy.GetParameterAsText(1) 

# Create a point object
# Construct a point object from the feature class
obsPoint = arcpy.Point()
obsPoint.X = 590000
obsPoint.Y = 230000