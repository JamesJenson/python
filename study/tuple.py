# 元组,不可变有序序列,无增删改功能,增删改时id会变
# 小括号定义
t = (33, 'aaa', 44)
print(t, type(t))
t = '111', 33, 4  # 该种方式定义时括号可省略
print(t, type(t))
'''内置函数定义:tuple()'''
t = tuple(('aaa', 333, 99))
print(t)
'''元组中只有一个元素时,必用小括号和逗号'''
t = ('python',)
print(t, type(t))
t = 'python',
print(t, type(t))
'''空元组'''
t = ()
print(t)
t = tuple()
print(t)

'''特点:
    在多任务环境下,同时操作对象时不需要加锁
    元组中存储的是对象的引用:引用不可变对象,则完全固定;引用可变对象,则可变对象中的数据可变,但id不能变'''
# 元组的元素的获取,索引获取
t = tuple(('python', 'aa', 'bb', 3))
print(t[0])
print(t[1])
# print(t[6]) 索引越界
# 元组的遍历
t = tuple(('python', 'aa', 'bb', 3))
for item in t:
    print(item, type(item), id(item))
