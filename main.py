from PyQt5.QtWidgets import *
import random 
import database

app = QApplication([])
window = QWidget()
menu_btn = QPushButton('Меню')
relax_btn = QPushButton('Відпочити')
timer_sbx = QSpinBox()
min_lbl = QLabel("Хвилин")
quest_lbl = QLabel("2+2")
var1_btn = QRadioButton("1")
var2_btn = QRadioButton("2")
var3_btn = QRadioButton("3")
var4_btn = QRadioButton("4")
answer_btn = QPushButton("Відповісти")
group = QGroupBox("Варіанти відповідей")
res_lbl = Qlable("Результат")
main_line = QVBoxLayout()
group_main_line.addWidget(res_lbl)
group_main_line


horisontal_line1 = QHBoxLayout()
horisontal_line1.addWidget(menu_btn)
horisontal_line1.addStretch(1)
horisontal_line1.addWidget(relax_btn)
horisontal_line1.addWidget(timer_sbx)
horisontal_line1.addWidget(min_lbl)
main_line.addLayout(horisontal_line1)
main_line.addWidget(quest_lbl)

group_main_line = QVBoxLayout()
group_main_line.addWidget(var1_btn)
group_main_line.addWidget(var2_btn)
group_main_line.addWidget(var3_btn)
group_main_line.addWidget(var4_btn)
group.setLayout(group_main_line)
main_line.addWidget(group)
main_line.addWidget(answer_btn)

answers = [var1_btn, var2_btn, var3_btn, var4_btn]

def set_quest():
    random.shuffle(answers)
    current_question = database.question[database.nomer]
    quest_lbl.setText(current_question["запитання"])
    answers[0].setText(current_question["Правельна відповідь"])
    answers[1].setText(current_question["Не правельна відповідь1"])
    answers[2].setText(current_question["Не правельна відповідь2"])
    answers[3].setText(current_question["Не правельна відповідь3"])
set_quest()



window.setLayout(main_line)
window.show()
app.exec()