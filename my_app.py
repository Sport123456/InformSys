# напиши здесь код основного приложения и первого экрана
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout
app=QApplication([])
main_win=QWidget()
main_win.show()

text1=('Добро пожаловать в программу по определению состояния здоровья')
sen1=QLabel(text1)
text2=('Данное приложение позволит вам с помощбю теста Руфье провести первичную диагностику вашего здоровья\n'
'Проба Руф1ье представляет собой')
sen2=QLabel(text2)
button=QPushButton('Начать')

LayoutV=QVBoxLayout()
LayoutV.addWidget(sen1,alignment=Qt.AlignCenter)
LayoutV.addWidget(sen2,alignment=Qt.AlignCenter)
LayoutV.addWidget(button,alignment=Qt.AlignCenter)

main_win.setLayout(LayoutV)
app.exec_()
