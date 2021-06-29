# 列表的创建
# 有序\重复\多种数据类类型\索唯一\动态分配和回收内存
# 第一种方式
lst = ['aaa', 'bbb', 5.6, True]
print(id(lst), type(lst), lst)
print(lst[:2])
print(lst[-2:])

for item in lst:
    print(id(item), type(item), item)
else:
    print('打印完成')

# 第二种方式 内置函数
lst = list([4, 5, 6, 7, '张三', '李四'])
print(id(lst), type(lst), lst)
a = lst[:2]
print(id(a))
print(lst[:2:2])
print(lst[-2:])

for item in lst:
    print(id(item), type(item), item)
else:
    print('打印完成')

# index获取列表索引
print(lst.index(5))  # 返回第一个出现的索引
# print(lst.index('aaa')) # 没有查到元素则会报异常
print(lst.index('张三', 4, 6))

# 列表的查询操作
print(lst[3])  # 正向索引
print(lst[-1])  # 逆向索引
# print(lst[-8])  # 超出列表索引会报错
# print(lst[8])  # 超出列表索引会报错

# 获取列表中多个元素,切片语法会新建一个lst数组(新数组)
'''特点:
    原数组片段的拷贝;
    可选范围截取,可选步长截取;
    lst[start:stop:step];
    lst[start,stop] 默认步长为1;
    步长为负数时,从start开始往前跑,直到到对应的结束索引位置(start>stop)'''
print(lst[5:3:-1])  # 特殊情况,从最后一个开始取一直到3,等价于list[5:3:-1]
print(lst[::-1])  # 逆序输出 等价于list[5::-1]
print(lst[-4:-3:-1])  # 不满足start>stop,输出为空
print(lst[3:1:-1])
print(lst[-3:-5:-1])

# 列表中插入元素
lst = ['张三', '李四', '王五']
lst1 = ['赵六', '孙七']
'''append:往列表末尾添加元素,不改变列表的id'''
print(lst, id(lst))
lst.append(1)
print(lst, id(lst))
'''extend:往列表末尾一次性添加多个元素,不改变列表id'''
print(lst, id(lst))
lst.extend(lst1)
print(lst, id(lst))
'''insert:往任意位置添加一个元素,不改变列表id'''
print(lst, id(lst))
lst.insert(3, 'insert')
print(lst, id(lst))
'''切片:给指定切片替换为至少一个元素,不改变列表id'''
lst3 = ['aa', 'bb', 'cc']
print(lst, id(lst))
lst[1:2] = lst3
print(lst, id(lst))

# 列表删除元素
lst4 = [1, 2, 3, 4, 5, 6, 7, 2, 1, 2, 4, 5]
'''remove:移除列表中的一个元素,重复也只移出第一个,不存在就报错,id不变'''
lst4.remove(2)  # 移出列表中一个元素,如果有重复也只移出第一个
print(lst4, id(lst4))
'''pop:根据索引删除元素,不指定索引,删除最后一个元素,索引不存在就报错,id不变'''
lst4.pop(1)
print(lst4, id(lst4))
lst4.pop()
print(lst4, id(lst4))
'''切片:删除至少一个元素,生产一个新对象'''
new_lst = lst4[1:3]
print(lst4, id(lst4))
print(new_lst, id(new_lst))
lst4[1:3] = []  # 替换成空列表的代替删除元素
print(lst4, id(lst4))

# 清除列表中所有元素,对象id还在
lst4.clear()
print(lst4, id(lst4))
# 删除列表,对象id消息,打印报错
del lst4
# print(lst4)

# 修改列表的元素,指定索引修改数据
'''索引修改,单值'''
lst5 = [10, 20, 30, 40, 50, 60]
lst5[1] = 1
print(lst5, id(lst5))
'''切片赋值,多值修改'''
lst5[:2] = ['a', 'a', 'a', 'a']
print(lst5, id(lst5))

# 列表排序
lst6 = [1, 2, 9, 6, 5, 8, 3, 47]
'''不填值默认升序'''
print(lst6, id(lst6))
lst6.sort()  # 不填值默认reverse=False
print(lst6, id(lst6))
'''reverse=true:降序排序'''
lst6.sort(reverse=True)
print(lst6, id(lst6))
'''内置函数sorted生成一个新的列表对象,源列表不变'''
new_lst6 = sorted(lst6, reverse=False)
print(lst6, id(lst6))
print(new_lst6, id(new_lst6))

# 列表生成公式,循环并对单个值计算得出结果放到列表中
lst7 = [i for i in range(1, 10)]
print(lst7, id(lst7))
lst7 = [i*i for i in range(1, 10)]
print(lst7, id(lst7))
