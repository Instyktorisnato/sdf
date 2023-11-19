from app import app
from PyQt5.QtWidgets import (
    QLabel, QRadioButton, QVBoxLayout, QHBoxLayout, QSpinBox, QGroupBox, QPushButton, QButtonGroup
)
from PyQt5.QtCore import Qt
main_layout = QVBoxLayout()

menu_layout = QHBoxLayout()
menu_button = QPushButton('меню')
pause_button = QPushButton('пауза')
rest_choice = QSpinBox()
rest_choice.setValue(30)
rest_label = QLabel('хвилин')
menu_layout.addWidget(menu_button,alignment=(Qt.AlignLeft|Qt.AlignTop))
menu_layout.addWidget(pause_button,alignment=(Qt.AlignRight|Qt.AlignTop))
menu_layout.addWidget(rest_choice,alignment=(Qt.AlignRight|Qt.AlignTop))
menu_layout.addWidget(rest_label,alignment=(Qt.AlignRight|Qt.AlignTop))

main_layout.addLayout(menu_layout)

quiz_label = QLabel('Засновник Майкрософт...')
main_layout.addWidget(quiz_label,alignment=(Qt.AlignCenter|Qt.AlignTop))

answergroup = QButtonGroup()
answerbox = QGroupBox('Варіанти відповідей')
button1 = QRadioButton()
button2 = QRadioButton()
button3 = QRadioButton()
button4 = QRadioButton()
answergroup.addButton(button1)
answergroup.addButton(button2)
answergroup.addButton(button3)
answergroup.addButton(button4)
layout_answer1 = QHBoxLayout()
layout_answer2 = QHBoxLayout()
layout_answer = QVBoxLayout()
layout_answer1.addWidget(button1, alignment=Qt.AlignHCenter)
layout_answer1.addWidget(button2, alignment=Qt.AlignHCenter)
layout_answer2.addWidget(button3, alignment=Qt.AlignHCenter)
layout_answer2.addWidget(button4, alignment=Qt.AlignHCenter)
layout_answer.addLayout(layout_answer1)
layout_answer.addLayout(layout_answer2)
answerbox.setLayout(layout_answer)
main_layout.addWidget(answerbox)

ok_button = QPushButton('Відповісти')
main_layout.addWidget(ok_button,alignment=Qt.AlignCenter)



