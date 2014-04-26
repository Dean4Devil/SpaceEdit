from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import *
from FileEngineer import FileEngineer

class SpaceEdit(QWidget):
    version = "0.0.3"
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
            QListWidgetItem(block.identifyer, parent=self.object_detail)

            
    def show_resources(self):
        self.object_detail.clear()
        if self.resources:
            for block in self.file_engineer.return_ship_list()[self.object_list.currentItem().data(0)]["CubeBlocks"]:
                QListWidgetItem(block.identifyer, self.object_detail)
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
             "LargeBlockSmallGenerator": {"steel_plate": 80, "motor": 6, "reactor_comp": 100, "metal_grid": 4, "computer": 25, "construction_comp": 40},
             "SmallBLockSmallGenerator": {"steel_plate": 2, "motor": 1, "reactor_comp": 1, "computer": 10, "construction_comp": 1},
             "LargeBlockBeacon": {"steel_plate": 80, "small_tube": 60, "large_tube": 40, "computer": 8, "construction_comp": 30, "radio_comp": 40},
             "SmallBlockBeacon": {"steel_plate": 1, "small_tube": 1, "computer": 1, "construction_comp": 1}
             }
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    screen = SpaceEdit()
    screen.show()
    
    sys.exit(app.exec_())
    