import openpyxl

# 打开文件:workbook对象
wb = openpyxl.load_workbook('test.xlsx')
# 表单的名称
names = wb.sheetnames
print(names)
# 遍历表单,打印表单名称
for sheet in wb:
    print(sheet.title)

# 创建一个新的表单
mySheet = wb.create_sheet("aaa")
# 根据sheetName获取sheet
sheetGet = wb.get_sheet_by_name('aaa')
print(sheetGet)
sheetGet = wb['aaa']
print(sheetGet)

# 表单的活跃页
ws = wb.active
print(ws)
# 单元格对象
c = ws['A2']
print(ws['A1'])
print(ws['A1'].value)
print('row{} , col{} is {}'.format(c.row, c.column, c.value))

# 保存文件
wb.close()
