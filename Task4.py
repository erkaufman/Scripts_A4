# Import packages
import sys, os, arcpy
arcpy.env.overwriteOutput= True

# Set input variable 
dataset = arcpy.GetParameterAsText(0)   #'V:/ARGOSTracking/Scratch/ARGOSTrack.shp'

# Create describe object
desc = arcpy.Describe(dataset)

# Message what the catalogPath is
arcpy.AddMessage(f"The CatalogPath is: {desc.catalogPath}")

# Message the extent
arcpy.AddMessage(f"XMin: {round(desc.extent.XMin, 1)}")
arcpy.AddMessage(f"XMax: {round(desc.extent.XMax, 1)}")
arcpy.AddMessage(f"YMin: {round(desc.extent.YMin, 1)}")
arcpy.AddMessage(f"YMax: {round(desc.extent.YMax, 1)}")

# Check dataset type and execute command accordingly
if desc.datasetType == 'FeatureClass':
    arcpy.AddWarning(f"ShapeType: {desc.shapeType}") # arcpy.AddWarning()
elif desc.datasetType == 'RasterDataset':
    arcpy.AddWarning(f"Format: {desc.format}\
          # of rows: {desc.height}\
          # of cols: {desc.width}")
else:
    arcpy.AddError(f"The data set type is: {desc.datasetType}")