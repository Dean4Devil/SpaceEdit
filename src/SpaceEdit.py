from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import *
from FileEngineer import FileEngineer

class SpaceEdit(QWidget):
    version = "1.0.5"
    def __init__(self, parent=None):
        super(SpaceEdit, self).__init__(parent)
        
        self.object_list = QListWidget()
        self.object_list.clicked.connect(self.list_detail)
        
        self.object_detail = QListWidget()
        
        self.file_open_button = QPushButton("&Open")
        self.file_open_button.show()
        self.show_res_button = QPushButton("Resources")
        self.show_res_button.setEnabled(False)
        self.undo_button = QPushButton("&Undo")
        self.undo_button.setEnabled(False)
        self.redo_button = QPushButton("&Redo")
        self.redo_button.setEnabled(False)
        
        self.file_open_button.clicked.connect(self.open_file)
        self.undo_button.clicked.connect(self.undo_action)
        self.redo_button.clicked.connect(self.redo_action)
        self.show_res_button.clicked.connect(self.show_resources)
        
        button_layout1 = QHBoxLayout()
        button_layout1.addWidget(self.file_open_button)
        button_layout1.addWidget(self.undo_button)
        button_layout1.addWidget(self.redo_button)
        button_layout1.addWidget(self.show_res_button)
        
        main_layout = QGridLayout()
        main_layout.addLayout(button_layout1, 0, 0)
        main_layout.addWidget(self.object_list, 1, 0)
        main_layout.addWidget(self.object_detail, 1, 1)
        
        self.setLayout(main_layout)
        self.setWindowTitle("SpaceEdit v%s" % self.version)
        
        self.file_engineer = FileEngineer()
            
    def open_file(self):
        self.object_list.clear()
        self.object_detail.clear()
        file_name = QFileDialog.getOpenFileName(self, caption='Open Save', directory='..', filter='Space Engineers Saves (*.sbs *.sbc)')
        self.file_engineer.parse_file(file_name[0])
        for ship_id in self.file_engineer.return_id_list():
            QListWidgetItem(ship_id, self.object_list)
        self.resources = False
        self.show_res_button.setEnabled(True)
    
    def undo_action(self):
        return ""
    
    def redo_action(self):
        return ""
    
    def list_detail(self, list_item):
        self.object_detail.clear()
        self.resources = False
        for block in self.file_engineer.return_ship_list()[list_item.data()]["CubeBlocks"]:
            try:
                QListWidgetItem(block.identifyer, parent=self.object_detail)
            except:
                print("None Block! :(", block.identifyer)

            
    def show_resources(self):
        self.object_detail.clear()
        if self.resources:
            for block in self.file_engineer.return_ship_list()[self.object_list.currentItem().data(0)]["CubeBlocks"]:
                try:
                    QListWidgetItem(block.identifyer, parent=self.object_detail)
                except:
                    print("None Block! :(", block)
            self.resources = False
        else:
            price = {}
            for block in self.file_engineer.return_ship_list()[self.object_list.currentItem().data(0)]["CubeBlocks"]:
                for part in self.parts[block.identifyer]:
                    try:
                        price[part] += self.parts[block.identifyer][part]
                    except KeyError:
                        price[part] = self.parts[block.identifyer][part]
            self.resources = True
            for p in price:
                QListWidgetItem(p + ": " + str(price[p]), self.object_detail)
            
            
    parts = {"LargeBlockArmorBlock": {"steel_plate": 25},
             "SmallBlockArmorBlock": {"steel_plate": 1},
             "LargeBlockArmorSlope": {"steel_plate": 13},
             "SmallBlockArmorSlope": {"steel_plate": 1},
             "LargeBlockArmorCorner": {"steel_plate": 4},
             "SmallBlockArmorCorner": {"steel_plate": 1},
             "LargeBlockArmorCornerInv": {"steel_plate": 21},
             "SmallBlockArmorCornerInv": {"steel_plate": 1},
             "LargeHeavyBlockArmorBlock": {"steel_plate": 150},
             "SmallHeavyBlockArmorBlock": {"steel_plate": 5},
             "LargeHeavyBlockArmorSlope": {"steel_plate": 75},
             "SmallHeavyBlockArmorSlope": {"steel_plate": 5},
             "LargeHeavyBlockArmorCorner": {"steel_plate": 25},
             "SmallHeavyBlockArmorCorner": {"steel_plate": 5},
             "LargeHeavyBlockArmorCornerInv": {"steel_plate": 125},
             "SmallHeavyBlockArmorCornerInv": {"steel_plate": 5},
             "LargeBlockSmallGenerator": {"steel_plate": 80, "motor": 6, "reactor_comp": 100, "metal_grid": 4, "computer": 25, "construction_comp": 40},
             "SmallBlockSmallGenerator": {"steel_plate": 2, "motor": 1, "reactor_comp": 1, "computer": 10, "construction_comp": 1},
             "LargeBlockLargeGenerator": {"steel_plate": 1000, "motor": 20, "reactor_comp": 2000, "large_tube": 40, "metal_grid": 40, "computer": 75, "construction_comp": 70},
             "SmallBlockLargeGenerator": {"steel_plate": 69, "motor": 5, "reactor_comp": 50, "large_tube": 3, "metal_grid": 9, "computer": 25, "construction_comp": 9},
             "LargeBlockBeacon": {"steel_plate": 80, "small_tube": 60, "large_tube": 40, "computer": 8, "construction_comp": 30, "radio_comp": 40},
             "SmallBlockBeacon": {"steel_plate": 1, "small_tube": 1, "computer": 1, "construction_comp": 1},
             "SmallBlockDrill": {"steel_plate": 22, "motor": 1, "large_tube": 4, "computer": 1, "construction_comp": 8},
             "LargeBlockInteriorWall": {"interior_plate": 22, "construction_comp": 10},
             "LargeBlockGravityGenerator": {"steel_plate": 150, "motor": 6, "gravity_comp": 6, "large_tube": 4, "computer": 40, "construction_comp": 60},
             "LargeRamp": {"small_tube": 50, "interior_plate": 50, "metal_grid": 24, "construction_comp": 16},
             "LargeRotor": {},  # Rotor, the part of the motor that is moving, therefore no cost
             "LargeStator": {"steel_plate": 15, "motor": 4, "large_tube": 4, "computer": 2, "construction_comp": 10},   # Stator is the stationary block, the Rotor "base"
             "LargeBlockDoor": {"steel_plate": 8, "small_tube": 4, "motor": 2, "interior_plate": 10, "metal_grid": 4, "computer": 2, "display": 1, "construction_comp": 10},
             "LargeBlockPassage": {"interior_plate": 74, "metal_grid": 18, "construction_comp": 20},
             "LargeRefinery": {"steel_plate": 1200, "motor": 12, "large_tube": 20, "computer": 20, "construction_comp": 40},
             "LargeAssembler": {"steel_plate": 150, "small_tube": 12, "motor": 8, "computer": 80, "display": 4, "construction_comp": 40},
             "LargeMedicalRoom": {"steel_plate": 20, "interior_plate": 235, "large_tube": 5, "metal_grid": 80, "display": 10, "construction_comp": 80, "medical_comp": 15},
             "LargeBlockSolarPanel": {"steel_plate": 4, "large_tube": 1, "solar_cell": 64, "metal_grid": 5, "computer": 2, "construction_comp": 7},
             "SmallBlockSolarPanel": {"steel_plate": 1, "small_tube": 1, "solar_cell": 16, "metal_grid": 2, "computer": 1, "construction_comp": 2},
             "LargeGatlingTurret": {"steel_plate": 20, "small_tube": 6, "motor": 8, "large_tube": 1, "computer": 10, "construction_comp": 30},
             "SmallGatlingGun": {"steel_plate": 4, "small_tube": 3, "motor": 1, "computer": 1},
             "LargeMissileLauncher": {},
             "SmallMissileLauncher": {"steel_plate": 4, "motor": 1, "large_tube": 4, "computer": 1, "construction_comp": 2},
             "LargeMissileTurret": {"steel_plate": 20, "motor": 16, "large_tube": 6, "computer": 12, "construction_comp": 40},
             "LargeInteriorTurret": {"steel_plate": 10, "small_tube": 2, "motor": 2, "large_tube": 1, "display": 5, "construction_comp": 20},
             "LargeDecoy": {},
             "SmallDecoy": {},
             "LargeWarhead": {"steel_plate": 10, "small_tube": 12, "girder": 25, "explosives": 6, "computer": 2, "bulletproof_glass": 24, "construction_comp": 12},
             "SmallWarhead": {"small_tube": 2, "girder": 1, "explosives": 2, "computer": 1, "construction_comp": 1},
             "LargeBlockConveyor": {"small_tube": 50, "motor": 2, "interior_plate": 50, "computer": 5, "construction_comp": 100},
             "SmallBlockConveyor": {"small_tube": 1, "motor": 1, "interior_plate": 1, "large_tube": 1, "computer": 2, "construction_comp": 2},
             "ConveyorTube": {"steel_plate": 20, "small_tube": 12, "motor": 8, "bulletproof_glass": 30, "construction_comp": 40},
             "ConveyorTubeSmall": {"steel_plate": 7, "small_tube": 2, "motor": 1, "construction_comp": 4},
             "Connector": {"steel_plate": 150, "small_tube": 12, "motor": 8, "computer": 20, "display": 4, "construction_comp": 40},
             "ConnectorSmall": {"steel_plate": 5, "small_tube": 2, "motor": 1, "computer": 4, "display": 1, "construction_comp": 4},
             "Collector": {"steel_plate": 45, "small_tube": 12, "motor": 8, "computer": 10, "display": 4, "construction_comp": 50},
             "CollectorSmall": {"steel_plate": 30, "small_tube": 10, "motor": 6, "computer": 8, "display": 2, "construction_comp": 35},
             "LargeBlockSmallThrust": {"steel_plate": 25, "thruster_component": 80, "large_tube": 8, "computer": 20, "construction_comp": 40},
             "SmallBlockSmallThrust": {"steel_plate": 1, "thruster_component": 1, "large_tube": 1, "construction_comp": 1},
             "LargeBlockLargeThrust": {"steel_plate": 150, "thruster_component": 960, "large_tube": 40, "computer": 60, "construction_comp": 70},
             "SmallBlockLargeThrust": {"steel_plate": 1, "thruster_component": 12, "interior_plate": 4, "large_tube": 5, "construction_comp": 1},
             "LargeBlockGyro": {"steel_plate": 900, "motor": 2, "large_tube": 4, "computer": 20, "construction_comp": 40},
             "SmallBlockGyro": {"steel_plate": 25, "motor": 1, "large_tube": 1, "computer": 3},
             "LargeSteelCatwalk": {"small_tube": 25, "interior_plate": 2, "metal_grid": 25, "construction_comp": 5},
             "LargeInteriorPillar": {"interior_plate": 20, "metal_grid": 6, "construction_comp": 6},
             "LargeStairs": {"small_tube": 82, "metal_grid": 52, "construction_comp": 20},
             "SmallLight": {"construction_comp": 1},
             "LargeBlockLandingGear": {"steel_plate": 150, "motor": 6, "large_tube": 4, "construction_comp": 10},
             "SmallBlockLandingGear": {"steel_plate": 1, "motor": 1, "large_tube": 1, "construction_comp": 1},
             "LargeBlockFrontLight": {"steel_plate": 6, "interior_plate": 20, "large_tube": 2, "bulletproof_glass": 2, "construction_comp": 20},
             "SmallBlockFrontLight": {"steel_plate": 1, "interior_plate": 1, "construction_component": 1},
             "LargeBlockSmallContainer": {"small_tube": 20, "motor": 2, "interior_plate": 40, "computer": 2, "display": 1, "construction_comp": 40},
             "SmallBlockSmallContainer": {"motor": 1, "interior_plate": 1, "computer": 1, "display": 1, "construction_comp": 1},
             "SmallBlockMediumContainer": {"motor": 4, "interior_plate": 10, "computer": 4, "display": 1},
             "LargeBlockLargeContainer": {"small_tube": 60, "motor": 20, "interior_plate": 360, "computer": 8, "display": 1, "construction_comp": 80},
             "SmallBlockLargeContainer": {"motor": 6, "interior_plate": 25, "computer": 6, "display": 1},
             "LargeBlockRadioAntenna": {"steel_plate": 75, "small_tube": 60, "large_tube": 40, "computer": 8, "construction_comp": 30, "radio_comp": 40},
             "SmallBlockRadioAntenna": {"small_tube": 1, "computer": 1, "construction_comp": 1},
             "LargeOreDetector": {"steel_plate": 50, "motor": 5, "detector_comp": 25, "computer": 25, "construction_comp": 20},
             "SmallBlockOreDetector": {"steel_plate": 2, "detector_comp": 1, "computer": 1, "construction_comp": 2},
             "LargeBlockCockpit": {"motor": 2, "interior_plate": 20, "computer": 100, "display": 10, "construction_comp": 20},  # Large ship normal cockpit
             "SmallBlockCockpit": {"motor": 1, "interior_plate": 10, "computer": 15, "display": 5, "construction_comp": 10},    # Small ship closed cockpit
             "LargeBlockCockpitSeat": {"motor": 1, "interior_plate": 30, "computer": 10, "display": 8, "bulletproof_glass": 10, "construction_comp": 20},   # Large ship closed cockpit
             "CockpitOpen": {"motor": 2, "interior_plate": 20, "computer": 100, "display": 4, "construction_comp": 20},    # Large ship open cockpit
             "LargeWindowSquare": {"small_tube": 4, "interior_plate": 12, "construction_comp": 8},   # "Old" Windows
             "LargeWindowEdge": {"interior_plate": 16, "construction_comp": 12},     # "Old" Windows
             "LargeCoverWall": {"steel_plate": 4, "construction_comp": 10},
             "LargeCoverWallHalf": {"steel_plate": 2, "construction_comp": 6},
             "VirtualMassLarge": {},
             "VirtualMassSmall": {},
             "Wheel1x1": {},
             "Wheel3x3": {},
             "Wheel5x5": {},
             "Window1x1Slope": {"girder": 12, "bulletproof_glass": 35},
             "Window1x1Flat": {"girder": 10, "bulletproof_glass": 25},
             "Window1x1FlatInv": {"girder": 10, "bulletproof_glass": 25},
             "Window2x3Flat": {"girder": 25, "bulletproof_glass": 140},
             "Window2x3FlatInv": {"girder": 25, "bulletproof_glass": 140},
             "Window1x2Flat": {},
             "Window1x2FlatInv": {},
             "Window3x3Flat": {"girder": 40, "bulletproof_glass": 200},
             "Window3x3FlatInv": {"girder": 40, "bulletproof_glass": 200},
             "Window1x2Slope": {"girder": 16, "bulletproof_glass": 55},
             "Window1x1Side": {},
             "Window1x2SideLeft": {"girder": 13, "bulletproof_glass": 26},
             "Window1x2SideRight": {"girder": 13, "bulletproof_glass": 26},
             "Window1x1Face": {"girder": 11, "bulletproof_glass": 24},
             "Window1x1Inv": {"girder": 11, "bulletproof_glass": 24},
             "Window1x2Face": {"girder": 15, "bulletproof_glass": 40},
             "Window1x2Inv": {"girder": 15, "bulletproof_glass": 40}}
             
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    screen = SpaceEdit()
    screen.show()
    
    sys.exit(app.exec_())
