# 程序组件包:运行程序,主窗口,按钮\文本编辑器
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox

def handleCalc():
    print('aaa')
    info = textEdit.toPlainText()
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
    QMessageBox.about(window, '统计结果', f'''薪资2000以上的有:\n{s_a_2000}\n薪资2000以下的有:\n{s_b_2000}''')

'''创建主程序'''
app = QApplication([])

'''创建主窗口'''
window = QMainWindow()
window.resize(500, 400)  # 窗口的启动时的大小
window.move(200, 100)  # 窗口的启动时的定位,左上角定位法,x=200,y=100
window.setWindowTitle('测试窗口')  # 设置窗口的名称

'''窗口下设置文本编辑器'''
textEdit = QPlainTextEdit(window)
textEdit.resize(400, 300)  # 编辑器的像素大小
textEdit.move(10, 10)  # 相对于父级窗口的定位,左上角定位法
textEdit.setPlaceholderText('请输入检测内容')  # 提示语

'''设置按钮'''
button = QPushButton('测试', window)
button.move(15, 320)
button.clicked.connect(handleCalc) # 绑定点击方法

'''窗口展示按钮:没有代码不会停留直接执行完成'''
window.show()
'''应用程序循环操作防止程序停止'''
app.exec_()


