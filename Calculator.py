import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from calc import Ui_MainWindow

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #кнопки ввода
        self.ui.Button0.clicked.connect(lambda: self.NumericButton_clicked('0'))
        self.ui.Button1.clicked.connect(lambda: self.NumericButton_clicked('1'))
        self.ui.Button2.clicked.connect(lambda: self.NumericButton_clicked('2'))
        self.ui.Button3.clicked.connect(lambda: self.NumericButton_clicked('3'))
        self.ui.Button4.clicked.connect(lambda: self.NumericButton_clicked('4'))
        self.ui.Button5.clicked.connect(lambda: self.NumericButton_clicked('5'))
        self.ui.Button6.clicked.connect(lambda: self.NumericButton_clicked('6'))
        self.ui.Button7.clicked.connect(lambda: self.NumericButton_clicked('7'))
        self.ui.Button8.clicked.connect(lambda: self.NumericButton_clicked('8'))
        self.ui.Button9.clicked.connect(lambda: self.NumericButton_clicked('9'))
        self.ui.Button_unar_minus.clicked.connect(self.UnarMinus_clicked)
        self.ui.Button_point.clicked.connect(self.Point_clicked)

        #кнопки операций
        self.ui.Button_div.clicked.connect(lambda: self.OperationButton_clicked(':'))
        self.ui.Button_minus.clicked.connect(lambda: self.OperationButton_clicked('-'))
        self.ui.Button_sum.clicked.connect(lambda: self.OperationButton_clicked('+'))
        self.ui.Button_multipl.clicked.connect(lambda: self.OperationButton_clicked('*'))

        #кнопка очистки
        self.ui.Button_clear.clicked.connect(self.ClearButton_clicked)

        #кнопка результата
        self.ui.Button_eq.clicked.connect(lambda: self.Result(self.ui.LineEdit1.text(), self.ui.LineEdit2.text(), self.ui.Label_operation.text()))

    def Result(self, N1, N2, Op): #вывод результата
        if N1 != '':
            floatN1 = float(N1)
        else:
            pass
        if N2 != '':
            floatN2 = float(N2)
        else:
            pass
        if N1 == '' and N2 != '':
            Result = N2
            self.ui.TexBox_result.setText(Result)
        elif N2 == '' and N1 != '':
            Result = N1
            self.ui.TexBox_result.setText(Result)
        elif N2 == '' and N1 == '':
            self.ui.TexBox_result.setText('Нет значений в окнах ввода')
        elif N2 != '' and N1 != '' and Op == '?':
            self.ui.TexBox_result.setText('Выберите операцию')
        elif N2 != '' and N1 != '':
            if Op == '+':
                Result = floatN1 + floatN2
                self.ui.TexBox_result.setText(str(format(Result, '.9f')))
            elif Op == '-':
                Result = floatN1 - floatN2
                self.ui.TexBox_result.setText(str(format(Result, '.9f')))
            elif Op == '*':
                Result = floatN1 * floatN2
                self.ui.TexBox_result.setText(str(format(Result, '.9f')))
            elif Op == ':':
                if floatN2 != 0:
                    Result = floatN1 / floatN2
                    self.ui.TexBox_result.setText(str(format(Result, '.9f')))
                else:
                    self.ui.TexBox_result.setText('Нельзя делить на ноль')
                
    def OperationButton_clicked(self, op): #вывод операции
        self.ui.Label_operation.setText(op)

    def Point_clicked(self): #постановка точки в окне ввода
        if self.ui.LineEdit1.hasFocus():
            Text = self.ui.LineEdit1.text()
            if Text != '' and not ',' in Text:
                self.ui.LineEdit1.setText(Text + '.')
        elif self.ui.LineEdit2.hasFocus():
            Text = self.ui.LineEdit2.text()
            if Text != '' and not ',' in Text:
                self.ui.LineEdit2.setText(Text + '.')

    def NumericButton_clicked(self, n): #ввод цифр
        if self.ui.LineEdit1.hasFocus():
            Text = self.ui.LineEdit1.text()
            if Text != '0':
                self.ui.LineEdit1.setText(self.ui.LineEdit1.text() + n)
        elif self.ui.LineEdit2.hasFocus():
            Text = self.ui.LineEdit1.text()
            if Text != '0':
                self.ui.LineEdit2.setText(self.ui.LineEdit2.text() + n)

    def UnarMinus_clicked(self): #ввод унарного минуса
        if self.ui.LineEdit1.hasFocus():
            Text = self.ui.LineEdit1.text()
            if not Text.startswith('-') and Text != '' and Text != '0' or Text.startswith('0.'):
                self.ui.LineEdit1.setText('-' + Text)
            elif Text.startswith('-'):
                self.ui.LineEdit1.setText(Text[1:])
        elif self.ui.LineEdit2.hasFocus():
            Text = self.ui.LineEdit2.text()
            if Text.startswith('-') and Text != '' and Text != '0':
                self.ui.LineEdit2.setText('-' + Text)
            elif Text.startswith('-') or Text.startswith('-0.'):
                self.ui.LineEdit2.setText(Text[1:])
    
    def ClearButton_clicked(self): #очистка окон
        self.ui.LineEdit2.setText('')
        self.ui.LineEdit1.setText('') 
        self.ui.Label_operation.setText('?')
        self.ui.TexBox_result.setText('')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    app.exec_()