import xlrd
import xlwt

from Constant import list_dic_model

rd_book = xlrd.open_workbook(r'F:\进展因子\赔付率计算源数据.xlsx')
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

    # 获取数据定位之下的业绩数据
    next_row = site_row + 1
    fist_value = sheet.cell_value(next_row, 0)
    while True:
        old_row = sheet.row(next_row)
        for j, item in enumerate(old_row):
            val = item.value
            if str(val):
                new_sheet.row(next_row).write(j, val)
        if fist_value == '总计' or fist_value == '':
            break
        next_row += 1
        fist_value = sheet.cell_value(next_row, 0)
    # 执行列循环并查找最左列
    max_row = next_row

    new_book.save(r'F:\进展因子\result\赔付率计算源数据.xls')
