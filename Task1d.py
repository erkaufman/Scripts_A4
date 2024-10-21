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
import arcpy, sys

# Set workspace
arcpy.env.workspace = "V:\\ENV859_PS4\\Data"
arcpy.env.overwriteOutput = True

# Streams file
stream_fp = "streams.shp"

# User input for buffer distance
buffer_input = sys.argv[1]

# Put in corrent format for buffer analysis function
buffer = f"{buffer_input} meters"

# user input for output
buffered_output_fp = f"V:\\ENV859_PS4\\Scratch\\buff_{buffer_input}m.shp"

arcpy.Buffer_analysis(stream_fp, buffered_output_fp, buffer, '', '','ALL')
print(arcpy.GetMessages())