from PyQt5.QtCore import Qt  
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox,   
QRadioButton, QPushButton, QLabel) 
 
app = QApplication([]) 
window = QWidget() 
 
btn_OK = QPushButton('Ответить') 
lb_Question = QLabel("Какой национальности не существует?") 
 
RadioGroupBox = QGroupBox("Варианты ответов") 
rbtn_1 = QRadioButton('энцы') 
rbtn_2 = QRadioButton('смурфы') 
rbtn_3 = QRadioButton('чулымцы') 
rbtn_4 = QRadioButton('алеуты') 
 
layout_ans1 = QHBoxLayout() 
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout() 
 
layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2) 
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4) 
 
layout_ans1.addLayout(layout_ans2) 
layout_ans1.addLayout(layout_ans3) 
 
RadioGroupBox.setLayout(layout_ans1) 
 
AnsGroupBox = QGroupBox("Результат теста") 
lb_Result = QLabel("Правельно или неправельно") 
lb_Correct = QLabel("Правельный ответ") 
 
layout_res = QHBoxLayout() 
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop)) 
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter) 
AnsGroupBox.setLayout(layout_res) 
 
layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout() 
 
layout_line1=QHBoxLayout() 
layout_line2=QHBoxLayout() 
layout_line3= QHBoxLayout() 
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter)) 
layout_line2.addWidget (RadioGroupBox) 
layout_line2.addWidget (AnsGroupBox) 
 
AnsGroupBox.hide() 
 
layout_line3.addStretch(1) 
layout_line3.addWidget(btn_OK, stretch =2) 
layout_line3.addStretch(1) 
 
layout_card=QVBoxLayout() 
 
layout_card.addLayout(layout_line1, stretch=2) 
layout_card.addLayout (layout_line2, stretch=8) 
layout_card.addStretch(1) 
layout_card.addLayout (layout_line3, stretch=1) 
layout_card.addStretch(1) 
layout_card.setSpacing(5) 
 
window = QWidget() 
window.setLayout(layout_card) 
window.setWindowTitle('Memo Card') 
window.show() 
app.exec() 
 
def show_result(): 
    RadioGroupBox.hide() 
    AnsGroupBox.show() 
    btn_OK.setText("Следуй вопрос") 
     
def show_question(): 
    RadioGroupBox.show() 
    AnsGroupBox.hide() 
    btn_OK.setText("Oтветить") 
    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked (False) 
    rbtn_2.setChecked (False) 
    rbtn_3.setChecked (False) 
    rbtn_4.setChecked (False) 
    RadioGroup.setExclusive(True) 
    [rbtn_1, rbtn_2, rbtn_3, rbtn_4] 
def ask(question, right_answer, wrongs, wrong2, wrong3): 
    shuffle (answers) 
    answers[0].setText (right_answer) 
    answers[1].setText (wrong1) 
    answers[2].setText (wrong2) 
    answers[3].setText (wrong3) 
    lb_Question.setText(question) 
    lb_Correct.setText(right_answer) 
    show_question() 
 
def show_correct (res): 
    lb_Result.setText (res) 
    show_result() 
 
def check_answer(): 
    if answers[0].IsChecked(): 
        show_correct("Правильно!") 
    else: 
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked(): 
            show_correct("Heвepно!") 

def next_question():
    print(f"Статистика\n-Всего вопросов: {window.total}\n-Правильных ответов: {window.score}")
 
window.setLayout (layout_card) 
window.setWindowTitle("Memory Card") 
ask("Государственный язык Бразилии", "Португальский", "Бразильский", "Испанский", 'Итальянский') 


id_result.setText (res)
shoLnesult)
def check enser ()
1f ensvars[0].1scecad ():
sho_correct("pasunswo!")
indow.score1
print (f"PeaTHNr: (round(edo.scarehdndas.tocal°1, 2)])
else:3

    1f enswer[1].isChecked() or answers2[2]-ischecked() or answers[3] isChecked():
        show_correct("Неверно!")
            print(f"Рейтинг: {round (window.score/window.total*100,2)}%")

def next_question():
    print (f"Статистики\n-Всего вопросов: {window.total}\n-Павильных ответов: {window.score}")
    if len(questions list) > 0:
        cur_question = randint(0, len(question_list) - 1)
        q = questions_llst[cur_question]
        ask()
        questions_list.pop(cur_question)
        window.total += 1
    else:
        victory_win = QMessageBox()
        victory_win.setText('ВЫ ОТВЕТИЛИ НА ВСЕ ВОПРООСЫ!")
        victory_win.exec_()

def click_OK():
    if btn_OK.text () == 'Ответить':
        check enswer()
    else:
        next question()

window.setlayout(layout_card)
window.setwindowTitle("Memory Card")
window.total - 0
window.score - 0
window.resize(300, 200)
btn_OK.clicked.commect(ick Or)
next_question()
window.show()
app.exec_()