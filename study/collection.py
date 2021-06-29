# 集合,可变类型序列,没有value的序列,不可重复的序列,无序
# 集合创建方式
c = {1, 2, 3, 4, 4, 5, 5}
print(c)
'''内置函数set()创建,会自动去掉重复的元素,只保留一个'''
c = set(range(6))  # range
print(c, type(c))
c = set([11, 22, 33, 22, 33, 44])  # 列表转
print(c, type(c))
c = set((11, '22', '22', '34'))  # 元组转
print(c, type(c))
c = set('python')  # 字符串转
print(c, type(c))
c = set({1, 3, 2, 4, 5, 6})  # 集合转
print(c, type(c))

# 定义空集合
c = set()
# c = {}  错误写法,会生成一个空的字典

# 集合的操作
'''判断操作:in和not in'''
'''add():新增操作,一次只能添加一个元素'''
c = set('python')
print(c)
c.add('b')
print(c)
'''update():新增操作,至少添加一个元素'''
c.update(['3', 5, 3])
print(c)
c.update(('4', 9, 'aaa'))
print(c)
'''remove():删除操作,会报异常,删除指定元素'''
c.remove('aaa')
print(c)
# c.remove('bbb') 删除不存在的会报错
'''discard():删除操作,不会报异常,删除指定元素'''
c.discard('bbb')
'''pop():无参内置行数,删除操作,不确定删除那个'''
c.pop()
print(c)
'''clear():清空集合'''
c.clear()
print(c)

# 集合间的对比
'''集合相等:==和!=判断,只判断元素相同,不判断顺序'''
c1 = {1, 2, 3, 4, 5}
c2 = {5, 2, 3, 4, 1}
print(c1 == c2)
print(c1 != c2)
'''子集:b.issubset(a),b是否是a的子集'''
c3 = {1, 2, 3, 4, 5, 6}
c4 = {5, 2, 3, 4, 1}
c5 = {5, 2, 3, 0, 1, 8}
print(c4.issubset(c3))
print(c5.issubset(c3))
'''超集:b.issuperset(a),b是否是a的超集'''
print(c3.issuperset(c4))
print(c3.issuperset(c5))
'''交集:是否有交集,有交集为false,无交集为True'''
c6 = {'a', 'b', 'c'}
print(c3.isdisjoint(c4))
print(c6.isdisjoint(c3))

# 集合的数学操作,不改变原集合的数据
'''求交集:'''
c7 = {1, 2, 3, 4, 5, 6}
c8 = {5, 2, 3, 4, 1, 9}
print(c7.intersection(c8))
print(c7 & c8)
'''求并集:'''
print(c7.union(c8))
print(c7 | c8)
'''求差集:a.difference(b),a中元素不在b中的元素'''
print(c7.difference(c8))
print(c7 - c8)
'''对称差集:求出a,b中互相没有的元素'''
print(c7.symmetric_difference(c8))
print(c7 ^ c8)

# 集合生成公式
c = {i * i for i in range(10)}
print(c)
