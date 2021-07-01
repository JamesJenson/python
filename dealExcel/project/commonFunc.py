import os
import xlrd
import string


# 检查行数是否存在数据
def check_row_invalid():
    pass


# 检查当前sheet页中的存在的非数字类型的字符
def check_number():
    pass


# 指定行数中某些位置的值及颜色
def set_val_col():
    pass


# 批量获取book文件路径，没有匹配到对应文件则返回[]
def batch_get_books(file_dir):
    book_paths = []
    # 校验当前是文件夹还是文件（必须为已存在的文件），如果是文件夹或者不存在文件，则为false
    if os.path.isfile(file_dir):
        if file_dir.endswith('.xlsx'):
            book_paths.append(file_dir)
        return book_paths
    # 如果路径不存在或者文件不存在则任务当前文件夹找不到(路径错误、不存在的文件)
    for root, dirs, files in os.walk(file_dir):  # 获取所有文件
        for file in files:  # 遍历所有文件名
            if os.path.splitext(file)[1] == '.xlsx':
                book_paths.append(os.path.join(root, file))  # 拼接绝对路径并放入列表
    return book_paths


# 获取book,sheet目录树
def get_books_tree(file_dir):
    trees = []
    book_paths = batch_get_books(file_dir)
    if book_paths:
        for file_path in book_paths:
            book = xlrd.open_workbook(file_path)
            file_info = {'fileName': os.path.basename(file_path), 'fileSheetNames': book.sheet_names()}
            trees.append(file_info)
    return trees


# 获取指定列的字母标号
def get_col_name(columnIndex):
    ret = ''
    ci = columnIndex - 1
    index = ci // 26
    if index > 0:
        ret += getColumnName(index)
    ret += string.ascii_uppercase[ci % 26]
    return ret


# 获取进展因子公式
def get_rate_formula(curName, preName, minRow, maxRow):
    formula = '''=IF(ISERROR(SUMIFS([A][B]:[A][C],[A][B]:[A][C],"<>")/SUMIFS([D][B]:[D][C],[D][B]:[D][C],"<>")),1,SUMIFS([A][B]:[A][C],[A][B]:[A][C],"<>")/SUMIFS([D][B]:[D][C],[D][B]:[D][C],"<>"))'''
    formula = formula.replace('[A]', curName).replace('[B]', str(minRow)).replace('[C]', str(maxRow)).replace('[D]', preName)
    return formula

# 获取计算的值的公式
def get_muli_formula(curName, preName, rateRow, curRow):
    formula = '''=[A][B]*[C][D]'''
    formula = formula.replace('[A]', curName).replace('[B]', str(rateRow)).replace('[C]', preName).replace('[D]', str(curRow))
    return formula