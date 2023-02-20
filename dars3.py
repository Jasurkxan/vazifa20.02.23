from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QPushButton, QListWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit

class ADD(QWidget):
    def __init__(self):
        super().__init__()



        self.hBtnEditLay = QHBoxLayout()
        self.vEditLay = QVBoxLayout()
        self.vMainLay = QVBoxLayout()

        self.engEdit = QLineEdit()
        self.engEdit.setPlaceholderText("Eng...")

        self.uzEdit = QLineEdit()
        self.uzEdit.setPlaceholderText("Uzb...")

        self.okBtn = QPushButton("OK")
        self.okBtn.clicked.connect(self.ok)

        self.natijaLbl = QLabel("")

        self.menuBtn = QPushButton("MENU")
        self.menuBtn.clicked.connect(self.menu)

        self.vEditLay.addWidget(self.engEdit)
        self.vEditLay.addWidget(self.uzEdit)

        self.hBtnEditLay.addLayout(self.vEditLay)
        self.hBtnEditLay.addWidget(self.okBtn)

        self.vMainLay.addLayout(self.hBtnEditLay)
        self.vMainLay.addWidget(self.natijaLbl)
        self.vMainLay.addWidget(self.menuBtn)

        self.setLayout(self.vMainLay)

    def ok(self):
        self.sanoq=0
        with open("lugat.txt","a+") as a:
            for i in a.read().split('\n'):
                i=i.split(" ")
                if i[0]==self.engEdit.text():
                    self.sanoq+=1
                print(self.sanoq)

            if self.engEdit.text()!="" and self.uzEdit.text()!="":
              a.write(f"{self.engEdit.text()} {self.uzEdit.text()}\n")
              self.engEdit.clear()
              self.uzEdit.clear()

            else:
                self.natijaLbl.setText("Malumot yetarli emas! ")
                self.natijaLbl.setStyleSheet("color:red;font-size:15px")


    def menu(self):
        self.engEdit.clear() 
        self.uzEdit.clear()
        self.close()

class SEARCH(QWidget):
    def __init__(self):
        super().__init__()

        self.hRadioLay = QHBoxLayout()
        self.hEditBtnLay = QHBoxLayout()
        self.vMainLay = QVBoxLayout()

        self.EngRadio = QRadioButton("Englsh")
        self.UzRadio = QRadioButton('Uzbek')

        self.Edit = QLineEdit()

        self.searchBtn = QPushButton("search")
        self.searchBtn.clicked.connect(self.search)

        self.lbl = QLabel("")

        self.menuBtn = QPushButton("MENU")
        self.menuBtn.clicked.connect(self.menu)

        self.hRadioLay.addWidget(self.EngRadio)
        self.hRadioLay.addWidget(self.UzRadio)

        self.hEditBtnLay.addWidget(self.Edit)
        self.hEditBtnLay.addWidget(self.searchBtn)

        self.vMainLay.addLayout(self.hRadioLay)
        self.vMainLay.addLayout(self.hEditBtnLay)
        self.vMainLay.addWidget(self.lbl)
        self.vMainLay.addWidget(self.menuBtn)

        self.setLayout(self.vMainLay)

    def search(self):
        with open("lugat.txt","r") as b:
         if self.EngRadio.isChecked():
            for i in b.read().split('\n'):
                i=i.split(" ")
                if i[0]==self.Edit.text():
                    self.lbl.setText(i[-1])
                    self.lbl.setStyleSheet("color:green;font-size:18px")
                    break
                else:
                     self.lbl.setText("Not found")
                     self.lbl.setStyleSheet("color:red;font-size:18px")
                     



         elif self.UzRadio.isChecked():
            for i in b.read().split('\n'):
                i=i.split(" ")
                if i[-1]==self.Edit.text():
                    self.lbl.setText(i[0])
                    self.lbl.setStyleSheet("color:green;font-size:18px")
                    break
                else:
                    self.lbl.setText("Not found")
                    self.lbl.setStyleSheet("color:red;font-size:18px")


    def menu(self):
        self.Edit.clear()
        self.close()

class LIST(QWidget):
    def __init__(self):
        super().__init__()
        self.navbat=1

        self.hLblLay = QHBoxLayout()
        self.hListWidgLay = QHBoxLayout()
        self.vMainLay = QVBoxLayout()

        self.engLbl = QLabel("English")
        self.uzLbl = QLabel("Uzbek")

        self.engListWdg = QListWidget()
        self.uzListWdg = QListWidget()
        with open("lugat.txt","r") as b:
            for i in b.read().split('\n'):
                i=i.split(" ")
                self.engListWdg.addItem(f"{self.navbat}.{i[0]}")
                self.uzListWdg.addItem(f"{self.navbat}.{i[-1]}")
                self.navbat+=1
                                        


        self.menuBtn = QPushButton("MENU")
        self.menuBtn.clicked.connect(self.menu)

        self.hLblLay.addWidget(self.engLbl)
        self.hLblLay.addWidget(self.uzLbl)

        self.hListWidgLay.addWidget(self.engListWdg)
        self.hListWidgLay.addWidget(self.uzListWdg)

        self.vMainLay.addLayout(self.hLblLay)
        self.vMainLay.addLayout(self.hListWidgLay)
        self.vMainLay.addWidget(self.menuBtn)

        self.setLayout(self.vMainLay)
        
    def menu(self):
        self.engListWdg.clear()
        self.uzListWdg.clear()
        self.close()

class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.addWindow = ADD()
        self.searchWindow = SEARCH()
        self.listWindow = LIST()

        self.vBtnLay = QVBoxLayout()
        self.hMainLay = QHBoxLayout()

        self.addBtn = QPushButton("ADD")
        self.addBtn.clicked.connect(lambda: self.addWindow.show())

        self.searchBtn = QPushButton("SEARCH")
        self.searchBtn.clicked.connect(self.searchWindow.show)
        
        self.listBtn = QPushButton("LIST")
        self.listBtn.clicked.connect(self.listWindow.show)

        self.exitBtn = QPushButton("EXIT")
        self.exitBtn.clicked.connect(self.close)

        self.vBtnLay.addWidget(self.addBtn)
        self.vBtnLay.addWidget(self.searchBtn)
        self.vBtnLay.addWidget(self.listBtn)
        self.vBtnLay.addWidget(self.exitBtn)

        self.hMainLay.addStretch()
        self.hMainLay.addLayout(self.vBtnLay)
        self.hMainLay.addStretch()

        self.setLayout(self.hMainLay)

app = QApplication([])
win = MainWindow()
win.show()
app.exec_()