from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QRadioButton, QMessageBox
from PyQt5.QtCore import Qt

def right_answer():
    message = QMessageBox()
    message.setText('Ти виграв!')
    message.exec_()
def wrong_answer():
    message = QMessageBox()
    message.setText('Ти програв!')
    message.exec_()

app = QApplication([])
main_window = QWidget()
main_window.resize(600, 400)
main_window.setWindowTitle('Memory Card')

question = QLabel('Скільки днів в високосному році?')
answer1 = QRadioButton('364')
answer1.clicked.connect(wrong_answer)
answer2 = QRadioButton('365')
answer2.clicked.connect(wrong_answer)
answer3 = QRadioButton('367')
answer3.clicked.connect(wrong_answer)
answer4 = QRadioButton('366')
answer4.clicked.connect(right_answer)

layout_answer1 = QHBoxLayout()
layout_answer2 = QHBoxLayout()
layout_answer1.addWidget(answer1, alignment=Qt.AlignHCenter)
layout_answer1.addWidget(answer2, alignment=Qt.AlignHCenter)
layout_answer2.addWidget(answer3, alignment=Qt.AlignHCenter)
layout_answer2.addWidget(answer4, alignment=Qt.AlignHCenter)
# print(dir(layout_answer1))
main_layout = QVBoxLayout(spacing=50)
main_layout.addWidget(question, alignment=Qt.AlignHCenter)
main_layout.addLayout(layout_answer1)
main_layout.addLayout(layout_answer2)
main_window.setLayout(main_layout)


main_window.show()
app.exec_()


