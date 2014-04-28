import SpaceEngineerData

class Block():
    x,y,z = 0,0,0
    name_modifier = ""
    has_name_modifier = False 
    def __init__(self,x,y,z, btype="Armor"):
        self.x,self.y,self.z = x,y,z
        self.type = btype
    
    def set_position(self,x,y,z):
        self.x,self.y,self.z = x,y,z
    
    def set_identifyer(self, ident):
        self.identifyer = ident
    
    def move(self,x=0,y=0,z=0):
        self.x += x
        self.y += y
        self.z += z
           
    def set_entity_id(self, eid):
        if self.type == "Armor":
            return False
        else:
            self.entity_id = eid
            return True

    def return_type(self):
        return "Block"

class Object():
    def __init__(self, sid, blocks=[], station=False):
        self.id = sid
        self.blocks = blocks
        self.station = station
    
    def set_blocks(self, blocks):
        self.blocks = blocks
        
    def move(self,x=0,y=0,z=0):
        for block in self.blocks:
            block.move(x,y,z)
        return True
        
    def delete(self):
        return True
        
    
class Ship(Object):
    def __init__(self, sid, blocks=[]):
        Object.__init__(self, sid, blocks=blocks)
    
        
    
class Station(Object):
    def __init__(self, sid, blocks=[]):
        Object.__init__(self, sid, blocks=blocks, station=True)
        
    def set_blocks(self, blocks):
        Object.set_blocks(self, blocks)


def create_block_from_xml(element):
    block = Block(0,0,0)
    block.set_identifyer("No Identifyer!")
    block.type = "Unknown"
    try:
        if element.attrib["{http://www.w3.org/2001/XMLSchema-instance}type"] == "MyObjectBuilder_GravityGenerator":
            block.identifyer = "LargeBlockGravityGenerator"
            for tag in element:
                if tag.tag == "Min":
                    block.set_position(tag.attrib["x"], tag.attrib["y"], tag.attrib["z"])
                if tag.tag == "EntityId":
                    block.set_entity_id(tag.text)
            return block
        
        elif element.attrib["{http://www.w3.org/2001/XMLSchema-instance}type"] == "MyObjectBuilder_Door":
            block.identifyer = "LargeBlockDoor"
            for tag in element:
                if tag.tag == "Min":
                    block.set_position(tag.attrib["x"], tag.attrib["y"], tag.attrib["z"])
                if tag.tag == "EntityId":
                    block.set_entity_id(tag.text)
            return block
        
        elif element.attrib["{http://www.w3.org/2001/XMLSchema-instance}type"] == "MyObjectBuilder_Passage":
            block.identifyer = "LargeBlockPassage"
            for tag in element:
                if tag.tag == "Min":
                    block.set_position(tag.attrib["x"], tag.attrib["y"], tag.attrib["z"])
                if tag.tag == "EntityId":
                    block.set_entity_id(tag.text)
            return block
                    
        elif element.attrib["{http://www.w3.org/2001/XMLSchema-instance}type"] == "MyObjectBuilder_LargeGatlingTurret":
            block.identifyer = "LargeGatlingTurret"
            for tag in element:
                if tag.tag == "Min":
                    block.set_position(tag.attrib["x"], tag.attrib["y"], tag.attrib["z"])
                elif tag.tag == "EntityId":
                    block.set_entity_id(tag.text) 
            return block 
        
        elif element.attrib["{http://www.w3.org/2001/XMLSchema-instance}type"] == "MyObjectBuilder_SmallGatlingGun":
            block.identifyer = "SmallGatlingGun"
            for tag in element:
                if tag.tag == "Min":
                    block.set_position(tag.attrib["x"], tag.attrib["y"], tag.attrib["z"])
                elif tag.tag == "EntityId":
                    block.set_entity_id(tag.text)  
            return block
        
        elif element.attrib["{http://www.w3.org/2001/XMLSchema-instance}type"] == "MyObjectBuilder_LargeMissileTurret":
            block.identifyer = "LargeMissileTurret"
            for tag in element:
                if tag.tag == "Min":
                    block.set_position(tag.attrib["x"], tag.attrib["y"], tag.attrib["z"])
                elif tag.tag == "EntityId":
                    block.set_entity_id(tag.text)  
            return block
        
        elif element.attrib["{http://www.w3.org/2001/XMLSchema-instance}type"] == "MyObjectBuilder_Beacon":
            for tag in element:
                if tag.tag == "SubtypeName":
                    block.identifyer = tag.text
                elif tag.tag == "Min":
                    block.set_position(tag.attrib["x"], tag.attrib["y"], tag.attrib["z"])
                elif tag.tag == "EntityId":
                    block.set_entity_id(tag.text)
                elif tag.tag == "CustomName":
                    block.name_modifier = tag.text
                    block.has_name_modifier = True 
            return block
                
        else:
            for tag in element:
                if tag.tag == "SubtypeName":
                    print("Setting unknown type block ident to: ", tag.text, tag.attrib)
                    block.set_identifyer(tag.text)
                elif tag.tag == "Min":
                    block.set_position(tag.attrib["x"], tag.attrib["y"], tag.attrib["z"])
                elif tag.tag == "EntityId":
                    block.set_entity_id(tag.text)
            return block
    except:
        if "Armor" in element[0].text:
            block.identifyer = element[0].text
            block.set_position(element[1].attrib["x"], element[1].attrib["y"], element[1].attrib["z"])
            return block
        else:
            print("Except and NOT armor!", element[0].text)
            for tag in element:
                if tag.tag == "SubtypeName":
                    block.set_identifyer(tag.text)
                elif tag.tag == "Min":
                    block.set_position(tag.attrib["x"], tag.attrib["y"], tag.attrib["z"])
            return block
