##---------------------------------------------------------------------
## Task1b.py
##
## Description: 
##
## Usage: 
##
## Created: Fall 2024
## Author: emma.kaufman@duke.edu (for ENV859)
##---------------------------------------------------------------------
import arcpy

# Set workspace
arcpy.env.workspace = "V:\\ENV859_PS4\\Data"
arcpy.env.overwriteOutput = True

stream_fp = "streams.shp"
buffer = "1000 meters"
buffered_output_fp = "V:\\ENV859_PS4\\Scratch\\StrmBuff1km.shp"

arcpy.Buffer_analysis(stream_fp, buffered_output_fp, buffer, '', '','ALL')
print(arcpy.GetMessages())