#-*- encoding=BIG5
# Name: Buffer.py
# Description: Find areas of suitable vegetation which exclude areas heavily impacted by major roads

# import system modules 
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "E:/Andy/Data/警政署警察局點位資料/Taipei_c"
#env.workspace = "E:/Andy/Data/"

# Buffer areas of impact around major roads
in_fc = "police.shp"
out_fc = "buf1000"
dist = "1000 Meters"
sideType = "FULL"
endType = "ROUND"

arcpy.Buffer_analysis(in_fc, out_fc, dist, sideType, endType)

