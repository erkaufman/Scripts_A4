# Import packages
import sys, os, arcpy
arcpy.env.overwriteOutput= True

# Set input variable 
dataset = 'V:/ARGOSTracking/Scratch/ARGOSTrack.shp'   #arcpy.GetParameterAsText(0)

# Create describe object
desc = arcpy.Describe(dataset)

# Message what the catalogPath is
print(f"The CatalogPath is: {desc.catalogPath}") # arcpy.AddMessage()

# Message the extent
print(f"XMin: {round(desc.extent.XMin, 1)}")
print(f"XMax: {round(desc.extent.XMax, 1)}")
print(f"YMin: {round(desc.extent.YMin, 1)}")
print(f"YMax: {round(desc.extent.YMax, 1)}")

# Check dataset type and execute command accordingly
if desc.datasetType == 'FeatureClass':
    print(f"ShapeType: {desc.shapeType}") # arcpy.AddWarning()
if desc.datasetType == 'RasterDataset':
    print(f"Format: {desc.format}\
          # of rows: {desc.height}\
          # of cols: {desc.width}")
else:
    print()