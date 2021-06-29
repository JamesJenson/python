# 定义excel-sheet对象
class DealSheet:

    # 初始化sheet页的模板
    def __init__(self, sheet):
        self.sheet = sheet
        self.set_sheet_model(sheet)

    # 检验并设置sheet格式
    def set_sheet_model(self, sheet):
        pass

    # 校验当前模板sheet下的数据行内容并设值
    def check_add(self):
        pass
    # 校验当前模板sheet下的数据内容并还原
    def check_del(self):
        pass
