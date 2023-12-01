from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (
        QFileDialog, 
        QVBoxLayout,
        QLabel,
        QDialog
    )


REMOVING_CHARS = ["/", "\\", ".", ",", "-", "_", "+",]

def clean_phone_numbers(values):
    for phone in values:
        for char in REMOVING_CHARS:
            phone = phone.replace(char, "")

        if len(phone) > 12:
            splitted_numbers = phone.split()[0]

            if len(splitted_numbers) == 9:
                splitted_numbers = f"998{splitted_numbers}"
            
            yield splitted_numbers

        else:
            splitted_numbers = phone.split()

            for phone in splitted_numbers:
                if not phone:
                    continue

                if len(phone) == 9:
                    phone = f"998{phone}"
                
                yield phone


def show_popup(text, success=False):
    dialog = QDialog()
    if success:
        dialog.setWindowTitle("Удалось")
    else:
        dialog.setWindowTitle("Ошибка")

    dialog.setGeometry(750, 300, 350, 200)
    dialog.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint)
    dialog.setWindowFlag (QtCore.Qt.WindowCloseButtonHint)

    image_label = QLabel()
    if success:
        pixmap = QtGui.QPixmap("img/success.png")
    else:
        pixmap = QtGui.QPixmap("img/error.png")
    pixmap = pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio)
    image_label.setPixmap(pixmap)
    image_label.setAlignment(QtCore.Qt.AlignCenter)

    label = QLabel(text)
    label.setAlignment(QtCore.Qt.AlignCenter)
    font = QtGui.QFont()
    font.setPointSize(12)
    label.setFont(font)

    layout = QVBoxLayout()
    layout.addWidget(image_label)
    layout.addWidget(label)
    dialog.setLayout(layout)

    dialog.exec_()


def open_file():
    file_path, _ = QFileDialog.getOpenFileName(None, 'Choose File', '', 'All Files (*);;Excel Files (*.xlsx);;')
    return file_path