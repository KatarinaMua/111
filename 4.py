from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import randint, shuffle 

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
       
app = QApplication([])

questions_list = [] 
questions_list.append(
        Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
questions_list.append(
        Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(
        Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))

window = QWidget()
window.setWindowTitle('Memo Card')
window.resize(400, 300)

but_main = QPushButton('Ответить')
lb_Question = QLabel('Самый сложный вопрос в мире!')

RadioGroupBox = QGroupBox("Варианты ответов")
a = QRadioButton('Вариант 1')
b = QRadioButton('Вариант 2')
c = QRadioButton('Вариант 3')
d = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(a)
RadioGroup.addButton(b)
RadioGroup.addButton(c)
RadioGroup.addButton(d)

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(a)
layout_ans2.addWidget(b)
layout_ans3.addWidget(c)
layout_ans3.addWidget(d)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

main_lay1 = QHBoxLayout()
main_lay2 = QHBoxLayout()
main_lay3 = QHBoxLayout()

main_lay1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
main_lay2.addWidget(RadioGroupBox)   
main_lay2.addWidget(AnsGroupBox)  
AnsGroupBox.hide()

main_lay3.addStretch(1)
main_lay3.addWidget(but_main, stretch=2)
main_lay3.addStretch(1)

mainLayout = QVBoxLayout()

mainLayout.addLayout(main_lay1, stretch=2)
mainLayout.addLayout(main_lay2, stretch=8)
mainLayout.addStretch(1)
mainLayout.addLayout(main_lay3, stretch=1)
mainLayout.addStretch(1)
mainLayout.setSpacing(5)
window.setLayout(mainLayout)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    but_main.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    but_main.setText('Ответить')
    RadioGroup.setExclusive(False)
    a.setChecked(False)
    b.setChecked(False)
    c.setChecked(False)
    d.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [a, b, c, d]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
        print('Рейтинг: ', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг: ', (window.score/window.total*100), '%')
    
def next_question():
    window.total += 1
    print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)

def click_OK():
    if but_main.text() == 'Ответить':
        check_answer()
    else:
        next_question()

but_main.clicked.connect(click_OK)

window.score = 0
window.total = 0
next_question()
window.show()
app.exec()
