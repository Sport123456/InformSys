# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout,QVBoxLayout,QLineEdit,QHBoxLayout
app=QApplication([])
main_win=QWidget()
main_win.show()

text1=('Введите Ф.И.О')
label1=QLabel(text1)
ed1=QLineEdit()
text2=('Полных лет')
label2=QLabel(text2)
ed2=QLineEdit()
text3=('Лягте на спину и замерьте пульс за 15 секунд')
label3=QLabel(text3)
button1=QPushButton('Начать первый тест')
text4=('Секундомер')
label4=QLabel(text4)

LayoutV1=QVBoxLayout()
LayoutV2=QVBoxLayout()
LayoutH1=QHBoxLayout()

LayoutV1.addWidget(label1,alignment=Qt.AlignLeft)
LayoutV1.addWidget(ed1,alignment=Qt.AlignLeft)
LayoutV1.addWidget(label2,alignment=Qt.AlignLeft)
LayoutV1.addWidget(ed2,alignment=Qt.AlignLeft)
LayoutV1.addWidget(label3,alignment=Qt.AlignLeft)
LayoutV1.addWidget(button1,alignment=Qt.AlignLeft)

##main_win.setLayout(LayoutV1)
LayoutV2.addWidget(label4,alignment=Qt.AlignCenter)

LayoutH1.addLayout(LayoutV1)
LayoutH1.addLayout(LayoutV2)
main_win.setLayout(LayoutH1)
app.exec_()