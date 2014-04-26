from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import *
from FileEngineer import FileEngineer

class SpaceEdit(QWidget):
    version = "0.0.1"
    def __init__(self, parent=None):
        super(SpaceEdit, self).__init__(parent)
        
        self.object_list = QTextEdit()
        self.object_list.setReadOnly(True)
        
        self.object_detail = QTextEdit()
        self.object_detail.setReadOnly(True)
        
        self.file_open_button = QPushButton("&Open")
        self.file_open_button.show()
        self.file_close_button = QPushButton("&Close")
        self.file_close_button.setEnabled(False)
        self.undo_button = QPushButton("&Undo")
        self.undo_button.setEnabled(False)
        self.redo_button = QPushButton("&Redo")
        self.redo_button.setEnabled(False)
        
        self.file_open_button.clicked.connect(self.open_file)
        self.file_close_button.clicked.connect(self.close_file)
        self.undo_button.clicked.connect(self.undo_action)
        self.redo_button.clicked.connect(self.redo_action)
        
        button_layout1 = QHBoxLayout()
        button_layout1.addWidget(self.file_open_button)
        button_layout1.addWidget(self.file_close_button)
        button_layout1.addWidget(self.undo_button)
        button_layout1.addWidget(self.redo_button)
        
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
        object_ids = ""
        for ship in self.file_engineer.return_ship_list():
            object_ids += ship["EntityId"] + "\n"
        self.object_list.setText(object_ids)
        return ""
        
    def close_file(self):
        return ""
    
    def undo_action(self):
        return ""
    
    def redo_action(self):
        return ""
            
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    screen = SpaceEdit()
    screen.show()
    
    sys.exit(app.exec_())