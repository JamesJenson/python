from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile


class Status:
    def __init__(self):
        # 创建主窗口
        qfile = QFile("测试.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()

        self.ui = QUiLoader().load(qfile)
        self.ui.button.clicked.connect(self.handleCalc)  # 绑定点击方法

    def handleCalc(self):
        info = self.ui.text1.toPlainText()
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
        QMessageBox.about(self.ui, '统计结果', f'''薪资2000以上的有:\n{s_a_2000}\n薪资2000以下的有:\n{s_b_2000}''')


app = QApplication([])
status = Status()
status.ui.show()
app.exec_()
