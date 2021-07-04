import commonFunc as Cf
from PySide2.QtWidgets import QApplication, QMessageBox, QFileDialog, QFileSystemModel, QTreeWidgetItem, \
    QAbstractItemView
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QDir, Qt


class MainUI:
    def __init__(self):
        # 创建主窗口
        qfile = QFile("mainUI.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()

        self.ui = QUiLoader().load(qfile)
        self.ui.chooseFile.clicked.connect(self.chooseFile)  # 绑定点击方法
        self.model = ''

    def chooseFile(self):
        file_path = QFileDialog.getExistingDirectory(self.ui, "", "C:/")  # 起始路径
        self.ui.filePath.setText(file_path)
        # 获取对应的文件名称
        trees = Cf.get_books_tree(file_path)
        print(trees)
        self.ui.treeWidget.headerItem().setText(0, "检测到的文件")
        self.ui.treeWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        for i in range(len(trees)):
            root = QTreeWidgetItem(self.ui.treeWidget)
            root.setText(0, trees[i]['fileName'])
            for j in range(len(trees[i]['fileSheetNames'])):
                child = QTreeWidgetItem(root)
                child.setText(0, trees[i]['fileSheetNames'][j])
                child.setCheckState(0,Qt.Checked)
            root.setCheckState(0, Qt.Checked)



app = QApplication([])
status = MainUI()
status.ui.show()
app.exec_()
