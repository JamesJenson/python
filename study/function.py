## 内置函数
# type(x):判断数据类型
a = 'aaa'
b = 5
print(type(a))
print(type(b))
print('-----------------------------')
# str(x):转换成字符串类型
a = 666
print(type(a))
print(type(str(a)))
print('-----------------------------')
# int(x):转换成整数类型
a = '666'
print(type(a))
print(type(int(a)))
print('-----------------------------')
# len(x):衡量数据的长度(不支持数字的衡量)
print(len(a))
a = ['a', 'b', 'c', 'd']
print(len(a))
print('-----------------------------')
# round(x,i):保留i位小数,四舍五入,超出原位数不补零
a = 1.4456545
print(type(a))
print(a)
print(round(a, 3))
print('-----------------------------')
# input(提示语):输入字符功能,让用户输入值
# a = input('请输入您的姓名:')
print(a)
print('-----------------------------')


# def 函数名(参数): 创建自己的函数,变量只能在函数内部使用(同java)
def area_all(up, down, height): # 形参
    area = (up + down) * height / 2
    print(area)

'''传入实参:关键字实参,顺序实参'''
area_all(up=5, down=6, height=7)  # 方法一(推荐),可以随意替换参数位置,不影响结果
area_all(5, 6, height=7)  # 方法二,参数带key时,必须是从最后一个参数开始连续的带key,不可间隔带key
area_all(5, 6, 7)  # 方法三,不可随意替换参数位置
print('-----------------------------')
'''
1.如果函数没有返回值,return可以会略
2.函数的返回值如果是一个,直接返回类型
3.函数的返回值如果是多个,返回的结果为元组
'''







