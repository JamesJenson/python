# coding:utf-8
import xlwt
import time

# 为样式创建字体
font = xlwt.Font()
# 字体类型
font.name = 'Andale WT'
# 字体颜色
font.colour_index = 0
# 字体大小，11为字号，20为衡量单位
font.height = 20 * 8
# 字体加粗
font.bold = False
# 下划线
font.underline = False
# 斜体字
font.italic = False

# 设置单元格对齐方式
alignment = xlwt.Alignment()
# 0x01(左端对齐)、0x02(水平方向上居中对齐)、0x03(右端对齐)
alignment.horz = 0x02
# 0x00(上端对齐)、 0x01(垂直方向上居中对齐)、0x02(底端对齐)
alignment.vert = 0x01
# 设置自动换行
alignment.wrap = 1

# 设置边框
borders = xlwt.Borders()
# 细实线:1，小粗实线:2，细虚线:3，中细虚线:4，大粗实线:5，双线:6，细点虚线:7
# 大粗虚线:8，细点划线:9，粗点划线:10，细双点划线:11，粗双点划线:12，斜点划线:13
# borders.left = 1
# borders.right = 2
# borders.top = 3
# borders.bottom = 4
# borders.left_colour = i
# borders.right_colour = i
# borders.top_colour = i
# borders.bottom_colour = i

# # 设置背景颜色
# pattern = xlwt.Pattern()
# # 设置背景颜色的模式
# pattern.pattern = xlwt.Pattern.SOLID_PATTERN
# # 背景颜色
# pattern.pattern_fore_colour = 43

# 计算结果的言责
collerStyle = xlwt.XFStyle()
collerStyle.font = font
pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = 43
collerStyle.pattern = pattern

# 默认的样式
defaultStyle = xlwt.XFStyle()
defaultStyle.font = font

# 补充0的样式
zoreStyle = xlwt.XFStyle()
zoreStyle.font = font
dp = xlwt.Pattern()
dp.pattern = xlwt.Pattern.SOLID_PATTERN
dp.pattern_fore_colour = 2
zoreStyle.pattern = dp

