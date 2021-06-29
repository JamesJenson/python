print("hello world!!")

## 变量
# 区分大小写
a = "abc"
A = 5
print(a)

## 字符串,引号展示类型
a = 'ab' \
    'c'  # 换行显示方法,不改变结果
print(a)
a = "ab" \
    "c"  # 换行显示方法,不改变结果
print(a)
a = '''ab''"
dd
f'''  # 可用于换行,把换行符也打印,中间的单引号和双引号不用转义
B = a
print(a)
print(B)

## 加减乘除,字符串之间不能相乘,相减,相除,可相加;字符串和数字间可相乘(结果为字符串的数据倍拼接)
a = 5
b = 6
d = "abc"
c = b / a
print(c)
c = b + a
print(c)
c = b * a
print(c)
c = a - b
print(c)
c = a * d
print(c)

## 字符串替换
c = d.replace('c', '666')  # 内置函数替换方法
print(c)
x = 'abcd%sfg' % '0000'  # %s的替换方法
print(x)
x = 'abcd{}fg'.format('0000')  # {}的替换方法
print(x)

## 字符串某部分内容(切片)
x = 'abcdefghijklmnopqstuvwxyz'
print(x[0:5])  # 正序,包前不包后
print(x[:5])  # 正序,起点0,可不写
print(x[2:5])  # 正序,包前不包后
print(x[-3:])  # 倒叙,最后一位不写直接截取最后串
print(x[-5:-3])  # 倒叙,包前不包后

## 条件判断(true和false首字母大写)
# 运算符:==,!=,<,>,<=,>=
x = 'bbb'
if x == 'aaa':  # False(False,0,[],'',None),True(True,数字,字符串,其他内容)
    print(x)
else:
    print(a)

if False:  # False(False,0,[],'',None),True(True,数字,字符串,其他内容)
    print(x)
else:
    print(a)

## 循环,嵌套循环和java一样
# for循环
a_list = [1, 2, 3, 4, 5, 6]
for i in a_list:
    print(i)
print(i)  # for循环中的i可以在循环外面取到

for j in range(3,5): # range(0,5),循环从0开始,0<=j<5,实际值是0-4
    print(j)
print(j)

