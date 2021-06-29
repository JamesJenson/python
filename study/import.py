## 第三方库调用
# import 库名
import xlrd

xlsx = xlrd.open_workbook('e:/aaa.xlsx')
print(type(xlsx))

a = range(20)
print(a)
print(list(a))