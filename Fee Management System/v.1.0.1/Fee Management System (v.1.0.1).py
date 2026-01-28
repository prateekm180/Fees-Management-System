import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QLineEdit, QTableWidget,
    QTableWidgetItem, QMessageBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor, QFont

def light_theme():
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor("#f5f5f5"))
    palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.black)
    palette.setColor(QPalette.ColorRole.Base, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.black)
    palette.setColor(QPalette.ColorRole.Button, QColor("#e0e0e0"))
    palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.black)
    return palette


def dark_theme():
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor("#121212"))
    palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Base, QColor("#1e1e1e"))
    palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Button, QColor("#2b2b2b"))
    palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
    return palette

class FeeManagementSystem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dark_mode = False
        self.setWindowTitle("Fee Management System")
        self.showMaximized()  
        self.init_ui()

    def init_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout()
        central.setLayout(main_layout)

        header = QHBoxLayout()
        title = QLabel("Fee Management System")
        title.setFont(QFont("Segoe UI", 20, QFont.Weight.Bold))

        self.theme_btn = QPushButton("🌙 Night Mode")
        self.theme_btn.clicked.connect(self.toggle_theme)

        header.addWidget(title)
        header.addStretch()
        header.addWidget(self.theme_btn)

        content = QHBoxLayout()

        form_card = QVBoxLayout()
        form_title = QLabel("Add Fee Record")
        form_title.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Student Name")

        self.class_input = QLineEdit()
        self.class_input.setPlaceholderText("Class")

        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Fee Amount")

        add_btn = QPushButton("Add Record")
        add_btn.clicked.connect(self.add_record)

        form_card.addWidget(form_title)
        form_card.addWidget(self.name_input)
        form_card.addWidget(self.class_input)
        form_card.addWidget(self.amount_input)
        form_card.addWidget(add_btn)
        form_card.addStretch()

        table_card = QVBoxLayout()
        table_title = QLabel("Fee Records")
        table_title.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))

        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["Name", "Class", "Amount"])
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(
            self.table.horizontalHeader().ResizeMode.Stretch
        )

        table_card.addWidget(table_title)
        table_card.addWidget(self.table)

        content.addLayout(form_card, 1)
        content.addLayout(table_card, 2)

        main_layout.addLayout(header)
        main_layout.addLayout(content)

    def add_record(self):
        name = self.name_input.text()
        cls = self.class_input.text()
        amt = self.amount_input.text()

        if not name or not cls or not amt:
            QMessageBox.warning(self, "Error", "All fields are required")
            return

        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(name))
        self.table.setItem(row, 1, QTableWidgetItem(cls))
        self.table.setItem(row, 2, QTableWidgetItem(amt))

        self.name_input.clear()
        self.class_input.clear()
        self.amount_input.clear()

    def toggle_theme(self):
        app = QApplication.instance()
        self.dark_mode = not self.dark_mode

        if self.dark_mode:
            app.setPalette(dark_theme())
            self.theme_btn.setText("☀ Light Mode")
        else:
            app.setPalette(light_theme())
            self.theme_btn.setText("🌙 Night Mode")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setPalette(light_theme())
    window = FeeManagementSystem()
    window.show()
    sys.exit(app.exec())
