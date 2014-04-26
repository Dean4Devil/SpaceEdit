import xml.etree.ElementTree as ET
import SectorObjects

class FileEngineer():

    def __init__(self):
        self.ship_list = []
        
    def parse_file(self, filename):
        tree = ET.parse(filename)
        sector = tree.getroot()
        for sector_objects in sector:
            if(sector_objects.tag == "SectorObjects"):
                objects = sector_objects
                break
        sector_objects = []
        for myobject in objects:
            if(myobject.attrib["{http://www.w3.org/2001/XMLSchema-instance}type"] == "MyObjectBuilder_CubeGrid"):
                sector_objects.append(myobject)

        
        for sector_object in sector_objects:
            ship_dict = {}
            for obj in sector_object:
                if(obj.tag == "PositionAndOrientation"):
                    pos_and_or = {}
                    for p_o in obj:
                        pos_and_or.update({p_o.tag: p_o.attrib})
                    ship_dict.update({obj.tag: pos_and_or})
                elif(obj.tag == "CubeBlocks"):
                    blocks = []
                    for block in obj:
                        blocks.append(SectorObjects.create_block_from_xml(block))
                    ship_dict.update({obj.tag: blocks})
                else:
                    ship_dict.update({obj.tag: obj.text})
            self.ship_list.append(ship_dict)
            
    def return_ship_list(self):
        return self.ship_list   # Makes it easier for multithreading later on
    