import xlrd, xlwt, xlutils

# data = xlrd.open_workbook("2.微保_防癌_站内_1续_赔付率.xlsx")
# print(data.sheet_loaded(0))  # 工作表是否被加载
# print(data.sheet_loaded(1))  # 工作表是否被加载
# print(data.sheet_loaded(2))  # 工作表是否被加载
# data.unload_sheet(0) # 根据索引或者名称卸载工作表
# print(data.sheet_loaded(0))
# print(data.sheet_loaded(1))  # 工作表是否被加载

# 工作表的获取
# print(data.sheets())  # 获取全部的sheet,数组
# print(data.sheets()[0])
# data.sheet_by_index(0)  # 获取索引为0的工作表
# data.sheet_by_name("总结")  # 根据名称获取工作表
# print(data.sheet_names()) # 获取工作表的所有名称
# print(data.nsheets) # 返回工作表的的数量

# 操作excel行
# sheet = data.sheet_by_index(0)
# print(sheet.nrows)  # 获取当前sheet下的有效行数
# print(sheet.row(0))  # 获取第一行的内容,组成的列表
# print(sheet.row_types(0))  # 获取指定行的数据类型 0(空)\1(字符串)\2(num)\3(date)\4(bool)\5(error)
# print(sheet.row(0)[2]) # 获取第一行第三列的值
# print(sheet.row(0)[2].value) # 获取第一行第三列的值
# print(sheet.row_values(0)) # 得到指定行单元格的值的列表
# print(sheet.row_len(0)) # 获取单元格的长度

# 操作excel列
# sheet = data.sheet_by_index(0)
# print(sheet.ncols)  # 当前工作表的有效列
# print(sheet.col(2))  # 获取单元格列的数据信息
# print(sheet.col(2)[1].value)  # 获取单元格指定列指定行的数据信息
# print(sheet.col_values(0))  # 得到指定列单元格的值的列表
# print(sheet.col_types(1)) # 合并的单元格会被默认成空

# 操作excel单元格
# sheet = data.sheet_by_index(0)
# print(sheet.cell(1, 2))  # 坐标获取单元格对象
# print(sheet.cell_type(1, 2))  # 单元格数据类型
# print(sheet.cell(1, 2).ctype)  # 单元格数据类型
# print(sheet.cell(1, 2).value)  # 单元格的数据
# print(sheet.cell_value(1, 2))  # 单元格的数据
#

# 创建工作簿
# wb = xlwt.Workbook()
# # 创建工作表
# ws = wb.add_sheet('CNY')
# # 填充数据
# ws.write_merge(0, 1, 0, 5, '2019年货币兑换表')
# data = (('01/01/2019', 4.54646, 1, 0.8888, 0.0672, 6.8885), ('01/01/2019', 4.54646, 1, 0.8888, 0.0672, 6.8885),
#         ('01/01/2019', 4.54646, 1, 0.8888, 0.0672, 6.8885))
#
# for i, item in enumerate(data):  # 获取索引的方法
#     for j, val in enumerate(item):
#         ws.write(i + 2, j, val)
#
# # 新建sheet也添加图片
# # wsImage = wb.add_sheet('image')
# # wsImage.insert_bitmap('微信截图_20210608235716.bmp', 0, 0)
# # 保存数据
# wb.save('2019-CNY.xls')
