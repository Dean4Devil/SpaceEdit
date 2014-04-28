import xml.etree.ElementTree as ET
import SectorObjects

class FileEngineer():

    def __init__(self):
        self.ship_list = {}
        self.name_dict = {}
        self.id_list = []
        
    def parse_file(self, filename):
        tree = ET.parse(filename)
        sector = tree.getroot()
        for sector_objects in sector:
            if(sector_objects.tag == "SectorObjects"):
                objects = sector_objects
                break
        sector_objects = []
        for myobject in objects:
            if(myobject.attrib["{http://www.w3.org/2001/XMLSchema-instance}type"] == "MyObjectBuilder_CubeGrid"):    # Make use of SectorObjects.Object class!
                sector_objects.append(myobject)
        
        for sector_object in sector_objects:
            ship_dict = {}
            EID = ""
            for obj in sector_object:
                if(obj.tag == "PositionAndOrientation"):
                    pos_and_or = {}
                    for p_o in obj:
                        pos_and_or.update({p_o.tag: p_o.attrib})
                    ship_dict.update({obj.tag: pos_and_or})
                elif(obj.tag == "EntityId"):
                    EID = obj.text
                    ship_dict.update({obj.tag: obj.text})
                elif(obj.tag == "CubeBlocks"):
                    blocks = []
                    for block in obj:
                        xml_block = SectorObjects.create_block_from_xml(block)
                        blocks.append(xml_block)
                    ship_dict.update({obj.tag: blocks})
                else:
                    ship_dict.update({obj.tag: obj.text})
            self.id_list.append(EID)
            self.ship_list.update({EID: ship_dict})
    
    def return_ship_list(self):
        return self.ship_list
    
    def return_name_dict(self):
        return self.name_dict
    
    def return_id_list(self):
        return self.id_list
