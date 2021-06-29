# string的创建和驻留机制
# 1.驻留机制(内存地址一样即id一样) ,创建新的字符串时先查找内存中是否存在,存在就将id赋给新的变量
a = 'python'
print(a, id(a))
b = "python"
print(b, id(b))
c = '''python'''
print(c, id(c))

# 交互模式(python自带ide,cmd)的驻留情况
'''字符串的长度为0或1时'''
'''符合标识符的字符串:字母和下划线'''
'''字符串旨在编译时驻留,而非运行时:在程序编译时将字符串生成好,针对通过方法生成的字符串,须在运行时生成新的'''
'''[-5,256]之间的整数数字'''
'''sys中的intern方法强制2个字符串指向同一个对象'''
'''pycharm对字符串的驻留做了强制处理'''
'''特点:
    避免频繁创建和销毁,提升效率和节约内存
    建议使用join方法,而非+,join批量添加,new一次对象,效率较高'''

# 字符串的查找:存在时,返回子串匹配的首字母的索引
'''index():查找子串第一次出现的位置,如果不存在,抛异常'''
'''rindex():查找子串最后一次出现的位置,如果不存在,抛异常'''
'''find():查找子串第一次出现的位置,如果不存在,则返回-1,推荐使用'''
'''rfind():查找子串最后一次出现的位置,如果不存在,则返回-1,推荐使用'''

# 字符串大小写转换操作,均会生成新的字符串对象,生成新的Id
'''upper():把字符串中所有字符都转成大写字母'''
'''lower():把字符串中所有字母转换成小写字母'''
'''swapcase():把字符串中所有大写字母转成小写字母,把所有小写字母转成大写字母'''
'''capitalize():把第一个字符转换成大写,把其余字符转换成小写'''
'''title():把每个单词的第一个字符转换成大写,把每个单词的剩余字符转换成小写'''

# 字符串内容对齐的操作
'''center():居中对齐,参数一指定宽度(小于字符串长度,则返回字符串,不做变化),参数二指定填充符(可选默认空格),'''
a = 'python'
print(a.center(20))
print(a.center(20, '$'))
'''ljust():左对齐,参数一指定宽度(小于字符串长度,则返回字符串,不做变化),参数二指定填充符(可选默认空格),'''
print(a.ljust(20))
print(a.ljust(20, '$'))
'''rjust():右对齐,参数一指定宽度(小于字符串长度,则返回字符串,不做变化),参数二指定填充符(可选默认空格),'''
print(a.rjust(20))
print(a.rjust(20, '$'))
'''zfill():右对齐,左边用0补充,只有一个参数,用于指定字符串的宽度(小于字符串长度,则返回字符串,不做变化)'''
print(a.zfill(20))
print('-123456789'.zfill(20))  # 特殊情况,首位为负号时,负号算一位,且补零在其后,在数值前
print('-aaaaaa'.zfill(20))  # 特殊情况,首位为负号时,负号算一位,且补零在其后,在数值前

# 字符串的劈分操作,返回列表
b = 'aaa bbb ddd,eee,rrr,ttt,uuu'
'''split():从左侧开始劈分,sep指定分隔符(默认空格);maxsplit指定劈分的最大次数,剩余子串会作为单独一部分'''
lst = b.split()
print(lst)
lst = b.split(sep=',')
print(lst)
lst = b.split(sep=',', maxsplit=2)
print(lst)
'''rsplit():从右侧开始劈分,sep指定分隔符(默认空格);maxsplit指定劈分的最大次数,剩余子串会作为单独一部分'''
lst = b.rsplit()
print(lst)
lst = b.rsplit(sep=',')
print(lst)
lst = b.rsplit(sep=',', maxsplit=2)
print(lst)

# 字符串的判断操作
'''isindentifier():判断是否是合法的标识符(字母+下划线+汉字)'''
print('python,hello'.isidentifier())  # False
print('python_hello'.isidentifier())  # True
print('张三_hello'.isidentifier())  # True
'''isspace():判断是否全部由空白字符组成(回车\换行\水平制表符)'''
print('\r'.isspace())  # True
print('\n'.isspace())  # True
print('\t'.isspace())  # True
print(' '.isspace())  # True
'''isalpha():判断是否全部由字母组成(字母,汉字)'''
print('abc'.isalpha())  # True
print('张三'.isalpha())  # True
print('张三1'.isalpha())  # False
'''isdecimal():判断是否全部由十进制的数字组成,只限十进制数字'''
print('123'.isdecimal())  # True
print('123四'.isdecimal())  # False
'''isnumeric():判断是否全部由数字组成(十进制数字\汉字数字\罗马数字)'''
print('123'.isnumeric())  # True
print('123四'.isnumeric())  # False
print('0b0101'.isnumeric())  # False
'''isalnum():判断是否全部由字母(汉字)和数字组成'''
print('aaa3'.isalnum())  # True
print('张三3'.isalnum())  # True
print('张三_3'.isalnum())  # False
print('张三*3'.isalnum())  # False

# 字符串的替换和合并,生成新的内存对象,新的id
'''replace():参数一指定被替换的字符串,参数二指定替换子串的字符串,参数三指定最大的替换次数(可选,默认全部替换)'''
c = 'hello,python,pythonpythonpythonpython'
print(c.replace('python', 'java'))
print(c.replace('python', 'java', 2))
'''join():将列表或元组中的字符串合并成一个字符串'''
lst = ['Java', 'C#', 'python']
print(','.join(lst))
print('|'.join(lst))
print(''.join(lst))
t = ('java', 'python')
print(','.join(t))
print('|'.join(t))
print(''.join(t))
'''join对象是字符串时,会将字符串按单个字符分隔'''
print(','.join('hello,python'))
print('|'.join('hello,python'))
print(''.join('hello,python'))

# 字符串的比较 >,>=,<,<=,==,!=
'''比较规则:字母从头开始依次比较,相等则比较下一个,不等则返回False,比较都相等则返回True'''
'''比较原理:比较的时字符的ordinalValue(原始值-ASCII码值),内置函数ord()可以获取原始值.对应的chr()函数可以通过原始值获取对应的字符;类似java中的char类型的转换'''
f = 'a'
print(ord(f))
print(chr(97))

# 字符串切片,由于字符串不具备增删改操作,所以切片会产生新的对象

# 字符串格式化,解决内存浪费的问题
'''%做占位符:%s字符串,%d数字,后面替换对象为元组'''
print('我叫%s,今年%d岁' % ('余志翔', 28))
'''{}做占位符'''
print('我叫{0},今年{1}岁'.format('余志翔', 28))
'''f-string'''
name = '余志翔'
age = 28
print(f'我叫{name},今年{age}岁')
'''定义宽度和精度'''
print('%10d' % 99)  # 10表示宽度
print('%.3f' % 99.34343425)  # .3f表示精度
print('%10.3f' % 99.34343425)  # 同时表示宽度和精度
print('{:.4}'.format(99.34343425))  # .3表示宽度,从头开始数3位数字
print('{:.3f}'.format(99.34343425))  # .3表示精度,小数点后3位
print('{:10.3f}'.format(99.34343425333))  # 同时表示宽度和精度

# 字符串编码转换
g = '余志翔'
'''编码'''
print(g.encode(encoding='GBK'))  # 在GBK中一个中文占两个字节
print(g.encode(encoding='UTF-8'))  # 在utf-8中一个中文占三个字节
'''解码:编码和解码的格式必须一致,不然或报错'''
byte1 = g.encode(encoding='GBK')
byte2 = g.encode(encoding='UTF-8')
print(byte1.decode(encoding='GBK'))
print(byte2.decode(encoding='UTF-8'))
