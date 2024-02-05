import json
from datetime import datetime, timedelta

START_TIME = 0
END_TIME = 0
TEST_TIME = "2024-02-05 15:16:20.000"
def main():

    helper = False
    large_data = []

    with open("paths/ISS.OEM_J2K_EPH.TXT") as file:
        for line in file:
            if "USEABLE_START_TIME" in line:
                vals = line.split()
                START_TIME = vals[2]
            elif "USEABLE_STOP_TIME" in line:
                vals = line.split()
                END_TIME = vals[2]
            if "COMMENT End sequence of events" in line:
                helper = True
                continue
            if helper == True:
                linesplit = line.split()
                valsindict = {"UTC": linesplit[0], "posx": linesplit[1], "posy":linesplit[2], "posz":linesplit[3]}
                large_data.append(valsindict) 
    
    with open("paths/data.json", "w") as file:
        json.dump(large_data, file, indent=4)
        file.write("")
                        
main()