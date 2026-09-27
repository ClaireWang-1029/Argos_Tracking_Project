#-------------------------------------------------------------
# ArgosSelectionTool.py
#
# Description: Reads in an Argos tracking data file and allows
#   the user to identify the tracked sitings found within a 
#   specified bounding box.
#
# Author:Ziyan Wang(zw284@duke.edu) 
# Date:   Fall 2026
#--------------------------------------------------------------
  
# Create the geographic selection box
the_box = {
    'x_min' : 34.00,
    'y_min' : -76.00,
    'x_max' : 34.50,
    'y_max' : -75.00
}

# Copy and paste a line of data as the lineString variable value
file_name= 'data/raw/Satellite tracking of black-capped petrels 2019-argos.csv'
#Create a file object pointing to file name
with open(file_name,"r") as f:
    line_list=f.readlines()
for lineString in line_list[1:]:
   
    # Use the split command to parse the items in lineString into a list object
    line_data = lineString.split(',')
       
    # Assign variables to specfic items in the list
    event_id = line_data[0]   # Argos tracking event ID ("event-id")
    timestamp = line_data[2]  # Observation date ("timestamp")
    lc  = line_data[14]
    if lc not in ('"1"','"2"','"3"'):
            continue
    
    lat = float(line_data[3])        # Observation latitude  ("location-lat")
    lon = float(line_data[4])        # Observation longitude ("location-lon")
    tag_id = line_data[-3]     # Tag identifier ("tag-local-identifier")
       
    #Evaluate latitude and longitude conditions
    lat_condition = the_box['y_min'] < lat < the_box['y_max']
    lon_condition = the_box['x_min'] < lon < the_box['x_max']
   
    #Report the status of the points
    if lat_condition & lon_condition:
        print(f'Record {event_id}: {tag_id} was IN the box at {timestamp}')
    else:
        print(f'Record {event_id}: {tag_id} was NOT IN the box at {timestamp}')