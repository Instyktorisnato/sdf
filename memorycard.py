from view import (
app,main_layout,button1,button2,button3,button4,ok_button,answergroup
)
from PyQt5.QtWidgets import QWidget
from random import shuffle
def showresult():
    button = answergroup.checkedButton()
    if button:
        if button.text() == rightanswer:
            print('right')
        else:
            print('not right')


window = QWidget()
window.resize(600,400)
window.setWindowTitle('Memory Card')
answerlist = ['Біл Гейтс','Марк Цукерберг','Стів Джобс','Ілон Маск']
rightanswer = answerlist[0]
shuffle(answerlist)
button1.setText(answerlist[0])
button2.setText(answerlist[1])
button3.setText(answerlist[2])
button4.setText(answerlist[3])


window.setLayout(main_layout)
window.show()
ok_button.clicked.connect(showresult)

app.exec_()




