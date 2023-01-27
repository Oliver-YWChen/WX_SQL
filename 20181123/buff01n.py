#-*- encoding=BIG5
# Name: Buffer.py
# Description: Find areas of suitable vegetation which exclude areas heavily impacted by major roads

# import system modules 
import arcpy
from arcpy import env
env.overwriteOutput = True

# Set environment settings
env.workspace = "E:/Andy/Data"
#env.workspace = "E:/Andy/Data/"

# Buffer areas of impact around major roads
in_fc = "police.shp"
num=300
for i in range(10):
    out_fc = "bufff"+str(num)
    dist = str(num)+" Meters"
    sideType = "FULL"
    endType = "ROUND"
    
    print('distance = ', num)
    arcpy.Buffer_analysis(in_fc, out_fc, dist, sideType, endType)
    num+=300

