from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox


class Status:
    def __init__(self):
        # 创建主窗口
        self.window = QMainWindow()
        self.window.resize(500, 400)  # 窗口的启动时的大小
        self.window.move(200, 100)  # 窗口的启动时的定位,左上角定位法,x=200,y=100
        self.window.setWindowTitle('测试窗口')  # 设置窗口的名称

        # 窗口下设置文本编辑器
        self.textEdit = QPlainTextEdit(self.window)
        self.textEdit.resize(400, 300)  # 编辑器的像素大小
        self.textEdit.move(10, 10)  # 相对于父级窗口的定位,左上角定位法
        self.textEdit.setPlaceholderText('请输入检测内容')  # 提示语

        # 设置按钮
        self.button = QPushButton('测试', self.window)
        self.button.move(15, 320)
        self.button.clicked.connect(self.handleCalc)  # 绑定点击方法

    def handleCalc(self):
        print('aaa')
        info = self.textEdit.toPlainText()
        print(info)
        s_a_2000 = ''
        s_b_2000 = ''
        for line in info.splitlines():
            if not line.strip():
                continue
            parts = line.split(' ')
            parts = [p for p in parts if p]
            name, salary, age = parts
            if int(salary) >= 2000:
                s_a_2000 = name + "\n"
            else:
                s_b_2000 = name + "\n"
        QMessageBox.about(self.window, '统计结果', f'''薪资2000以上的有:\n{s_a_2000}\n薪资2000以下的有:\n{s_b_2000}''')

app = QApplication([])
status = Status()
status.window.show()
app.exec_()