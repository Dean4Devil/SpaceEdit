import xml.etree.ElementTree as ET

def return_sector_objects():
    tree = ET.parse("../SANDBOX_0_0_0_.sbs")
    sector = tree.getroot()
    for child in sector:
        if(child.tag == "SectorObjects"):
            objects = child
    tmp = []
    for obj in objects:
        if(obj.attrib["{http://www.w3.org/2001/XMLSchema-instance}type"] == "MyObjectBuilder_CubeGrid"):
            tmp.append(obj)
    return tmp

sector_objects = return_sector_objects()

print(sector_objects)

sector_ships = []
sector_stations = []

for so in sector_objects:
    for o in so:
        if(o.tag == "IsStatic"):
            if(o.text == "true"):
                sector_stations.append(so)
            else:
                sector_ships.append(so)
                
print(sector_stations, "\n")
print(sector_ships)