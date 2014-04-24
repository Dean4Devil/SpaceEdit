class Block():
    x,y,z = 0
    def __init__(self,x,y,z):
        self.x,self.y,self.z = x,y,z
        return ""
    
    def set_position(self,x,y,z):
        self.x,self.y,self.z = x,y,z
    
    def move(self,x=0,y=0,z=0):
        self.x += x
        self.y += y
        self.z += z
           

class SectorObject():
    def __init__(self, blocks=[], station=False):
        self.blocks = blocks
        self.station = station
        return ""
    
    def set_blocks(self, blocks):
        self.blocks = blocks
        
    def move(self,x=0,y=0,z=0):
        for block in self.blocks:
            block.move(x,y,z)
        
    def delete(self):
        
        
    
class SectorShip(SectorObject):
    def __init__(self):
        isStatic = True
        blocks
        SectorObject.__init__(self)
        return ""
        
    
class SectorStation(SectorObject):
    def __init__(self):
        SectorObject.__init__(self)
        return ""