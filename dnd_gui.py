# Main application GUI
# Work in progress, more features are to be added

# Imports
import sys
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication, QLineEdit, QLabel, QSpinBox, QGridLayout, QMessageBox
from new_window import NewWindow
from character import Character

# Global variables
character_list = []
monster_list = []


# User interface
class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Buttons on the main user interface
        character_btn = QPushButton('Make Character', self)
        character_btn.setToolTip('Make a new character')

        character_btn.move(20, 20)
        character_btn.clicked.connect(self.creation_click)

        stat_btn = QPushButton('Check Characters', self)
        stat_btn.setToolTip('Check the current characters')
        stat_btn.move(20, 45)
        stat_btn.clicked.connect(self.stat_click)

        character_btn.resize(stat_btn.sizeHint())
        stat_btn.resize(stat_btn.sizeHint())

        self.setGeometry(300, 300, 300, 200)
        self.showMaximized()

    # Character creation click event
    def creation_click(self):
        self.w = NewWindow()
        self.w.move(300, 300)
        self.w.setWindowTitle("Character Creation")

        self.layout = QGridLayout(self.w)
        self.layout.setSpacing(2)

        self.name_label = QLabel("Name:", self.w)
        self.sex_label = QLabel("Sex:", self.w)
        self.race_label = QLabel("Race:", self.w)
        self.level_label = QLabel("Level:", self.w)
        self.dex_label = QLabel("Dex:", self.w)
        self.strength_label = QLabel("Strength:", self.w)

        self.name = QLineEdit(self.w)
        self.sex = QLineEdit(self.w)
        self.race = QLineEdit(self.w)
        self.level = QSpinBox(self.w)
        self.dex = QSpinBox(self.w)
        self.strength = QSpinBox(self.w)

        self.submit_btn = QPushButton("Submit", self.w)


        self.layout.addWidget(self.name_label, 1, 0)
        self.layout.addWidget(self.name, 1, 1)
        self.layout.addWidget(self.sex_label, 2, 0)
        self.layout.addWidget(self.sex, 2, 1)
        self.layout.addWidget(self.race_label, 3, 0)
        self.layout.addWidget(self.race, 3, 1)
        self.layout.addWidget(self.level_label, 4, 0)
        self.layout.addWidget(self.level, 4, 1)
        self.layout.addWidget(self.dex_label, 5, 0)
        self.layout.addWidget(self.dex, 5, 1)
        self.layout.addWidget(self.strength_label, 6, 0)
        self.layout.addWidget(self.strength, 6, 1)
        self.layout.addWidget(self.submit_btn, 7, 0)

        self.w.setLayout(self.layout)
        self.w.setFixedSize(350, 300)
        self.submit_btn.clicked.connect(self.submit_click)

        self.w.show()

    def submit_click(self):
        name_value = self.name.text()
        sex_value = self.sex.text()
        race_value = self.race.text()
        level_value = self.level.value()
        dex_value = self.dex.value()
        strength_value = self.strength.value()
        new_character = Character(name_value, sex_value, race_value, level_value,
                                  dex_value, strength_value)
        global character_list
        character_list.append(new_character)
        msg = QMessageBox()
        msg.setText("Successfully created the character.")
        msg.setWindowTitle("Success")
        msg.exec_()
        self.w.destroy()

    # Stat/Character check click event
    def stat_click(self):
        msg = QMessageBox()
        msg.setWindowTitle("Character Information")
        text = (character_list[0].return_name() + "\n" + character_list[0].return_sex() +
                    "\n" + character_list[0].return_race() + "\n" + str(character_list[0].return_level()) +
                    "\n" + str(character_list[0].return_dex()) + "\n" + str(character_list[0].return_strength()))
        msg.setText(text)
        msg.exec_()


# Main method
def main():
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())


# Runs the program
if __name__ == '__main__':
    main()
