import xlrd
import xlwt
import style
import os

from Constant import list_dic_model
from commonFunc import get_col_name, get_rate_formula, get_muli_formula, batch_get_books


def checkFile(path):
    print(path)
    pass


def execute(path):
    all_path = batch_get_books(path)
    if not bool(all_path):
        return
    for filePath in all_path:
        rd_book = xlrd.open_workbook(filePath)
        # 新建一个workbook
        new_book = xlwt.Workbook()
        # 获取sheet页列表
        sheets = rd_book.sheets()
        for sheet in sheets:
            sheet_name = sheet.name
            # 获取匹配的坐标位置
            site_model = {}
            for model in list_dic_model:
                site_vlue = sheet.cell_value(model['site']['row'], model['site']['col'])
                if site_vlue == '1':
                    site_model = model
            if not bool(site_model):
                continue
            site_row = site_model['site']['row']
            site_col = site_model['site']['col']
            new_sheet = new_book.add_sheet(sheet_name)
            # 获取数据定位之上的表头数据
            for i in range(0, site_row + 1):
                old_row = sheet.row(i)
                for j, item in enumerate(old_row):
                    val = item.value
                    if val:
                        new_sheet.row(i).write(j, val, style.defaultStyle)

            # 获取一些特殊定位值的坐标
            # 列总计
            total_col_site = 0
            for j, item in enumerate(sheet.row(site_row)):
                val = item.value
                if val == '总计':
                    total_col_site = j
            # 获取数据定位之下的业绩数据
            not_empty_rows = []  # 列表非空行
            empty_cols = []  # 列表中空的列
            next_row = site_row + 1  # 初始化第一行
            next_col = site_col  # 初始化第一列
            rate_row = 0  # 初始化进展因子行
            fist_value = sheet.cell_value(next_row, 0)  # 初始化第一行第一列的值
            # 复制行的循环
            while True:
                old_row = sheet.row(next_row)
                # 总计前面插入进展因子行
                if fist_value == '总计' or fist_value == '':
                    new_sheet.row(next_row).write(0, '进展因子', style.defaultStyle)
                    rate_row = next_row
                    next_row += 1
                for j, item in enumerate(old_row):
                    val = item.value
                    if str(val) and (not str(val).isspace()):
                        new_sheet.row(next_row).write(j, val, style.defaultStyle)
                        if j != 0 and j < total_col_site:
                            if next_row not in not_empty_rows:
                                not_empty_rows.append(next_row)
                next_row += 1
                if fist_value == '总计' or fist_value == '':
                    break
                fist_value = sheet.cell_value(next_row, 0)

            while True:
                if next_col == 1:
                    next_col += 1
                    continue
                if sheet.cell_value(site_row, next_col) == '总计':
                    break
                # 获取边界的行数
                mid_row = site_row
                min_row = site_row + 1
                first_flag = True
                for i in range(site_row + 1, rate_row):
                    if i not in not_empty_rows:
                        continue
                    val = sheet.cell_value(i, next_col)
                    if val and first_flag:
                        min_row = i
                        first_flag = False
                    if val:
                        mid_row = i
                if mid_row == site_row:
                    empty_cols.append(next_col)
                    next_col += 1
                    continue
                else:
                    cur_name = get_col_name(next_col + 1)
                    pre_name = get_col_name(next_col)
                    formula = get_rate_formula(cur_name, pre_name, min_row + 1, mid_row + 1)
                    new_sheet.row(rate_row).write(next_col, xlwt.Formula(formula), style.defaultStyle)
                    for i in range(site_row + 1, rate_row):
                        if i not in not_empty_rows and i < mid_row:
                            continue
                        val = sheet.cell_value(i, next_col)
                        if (not str(val)) or str(val).isspace():
                            if i < mid_row:
                                new_sheet.row(i).write(next_col, 0, style.zoreStyle)
                            elif i > mid_row:
                                muli_formula = get_muli_formula(cur_name, pre_name, rate_row + 1, i + 1)
                                new_sheet.row(i).write(next_col, xlwt.Formula(muli_formula), style.collerStyle)
                next_col += 1
        result_path = path + '/result'
        if not os.path.exists(result_path):
            os.mkdir(result_path)
        result_path = result_path + '/' + os.path.basename(filePath).replace('xlsx', 'xls')
        new_book.save(result_path)
