import xlrd
import xlwt

from Constant import list_dic_model

rd_book = xlrd.open_workbook(r'E:\进展因子\赔付率计算源数据.xlsx')
# 获取sheet页列表
sheet = rd_book.sheet_by_index(1)
sheet_name = sheet.name
print(sheet_name)
if '赔款' in sheet_name or '保费' in sheet_name:
    # 获取匹配的坐标位置
    site_model = {}
    for model in list_dic_model:
        site_vlue = sheet.cell_value(model['site']['row'], model['site']['col'])
        if site_vlue == '1':
            site_model = model
    if not bool(site_model):
        print(False)
    site_row = site_model['site']['row']
    site_col = site_model['site']['col']
    # 新建一个workbook
    new_book = xlwt.Workbook()
    new_sheet = new_book.add_sheet(sheet_name)
    # 获取数据定位之上的表头数据
    for i in range(0, site_row + 1):
        old_row = sheet.row(i)
        for j, item in enumerate(old_row):
            val = item.value
            if val:
                new_sheet.row(i).write(j, val)

    # 获取一些特殊定位值的坐标
    # 列总计
    total_col_site = 0
    for j, item in enumerate(sheet.row(site_row)):
        val = item.value
        if val == '总计':
            total_col_site = j
    # 获取数据定位之下的业绩数据
    not_empty_rows = []
    next_row = site_row + 1
    fist_value = sheet.cell_value(next_row, 0)
    while True:
        old_row = sheet.row(next_row)
        # 总计前面插入进展因子行
        if fist_value == '总计' or fist_value == '':
            new_sheet.row(next_row).write(0, '进展因子')
            next_row += 1
        for j, item in enumerate(old_row):
            val = item.value
            if str(val) and (not str(val).isspace()):
                new_sheet.row(next_row).write(j, val)
                if j != 0 and j < total_col_site:
                    if next_row not in not_empty_rows:
                        not_empty_rows.append(next_row)
        next_row += 1
        if fist_value == '总计' or fist_value == '':
            break
        fist_value = sheet.cell_value(next_row, 0)
    # 有效数据最大行
    max_row = next_row - 1
    next_col = site_col
    while True:
        if next_col == 1:
            next_col += 1
            continue
        if sheet.cell_value(site_row, next_col) == '总计':
            break
        # 获取边界的行数
        mid_row = site_row
        for i in range(site_row + 1, max_row):
            if i not in not_empty_rows:
                continue
            val = sheet.cell_value(i, next_col)
            if val:
                mid_row = i
        if mid_row == site_row:
            next_col += 1
            continue
        else:
            for i in range(site_row + 1, max_row):
                if i not in not_empty_rows:
                    continue
                val = sheet.cell_value(i, next_col)
                print(val)
                if (not str(val)) or str(val).isspace():
                    if i < mid_row:
                        new_sheet.row(i).write(next_col, 0)
                    elif i > mid_row:
                        new_sheet.row(i).write(next_col, '-')
        next_col += 1
    new_book.save(r'E:\进展因子\result\赔付率计算源数据.xls')
