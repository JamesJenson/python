# 含义
# 特点:key不能重复,值可以重复;元素是无序的;key为不可变对象(字符串\整数);动态伸缩;蓝菲较大内存,空间换时间的数据结构
dic = {'id': 111, 'name': '张三'}  # json格式数据
'''可变序列,键值对存储,无序的序列'''
print(dic, type(dic))

# 字典的创建
'''第一种:直接等于{}创建'''
dic = {'id': 111, 'name': '张三'}  # json格式数据
print(dic, type(dic))
'''第二种:内置函数dict()生成'''
dic = dict(name=111, age=20)
print(dic, type(dic))
'''第三种:空字典'''
dic = {}
print(dic, type(dic))

# 字典元素的获取
'''第一种:[]获取'''
dic = {'id': 111, 'name': '张三'}  # json格式数据
print(dic['id'], type(dic['id']))  # 如果不存在key报错
'''第二种:get()获取'''
print(dic.get('id'))
print(dic.get('aa'))  # 如果不存在key,默认返回None
print(dic.get('aa', 0))  # 如果不存在key,返回指定的值0

# 键的判断
# in和not in 来判断
print('bb' in dic)
print('bb' not in dic)

# 键值对的删除
del dic['id']
print(dic)
# 清空字典元素
dic.clear()
print(dic)
# 增加元素
dic['aaa'] = 90
print(dic)
# 修改元素
dic['aaa'] = 80
print(dic)

# 获取字段视图
dic.keys()  # 获取字典的所有key
print(dic.keys(), type(dic.keys()))
print(list(dic.keys()))  # 转成列表视图
dic.values()  # 获取字典的所有值
print(dic.values(), type(dic.values()))
print(list(dic.values()))  # 转成列表视图
dic.items()  # 获取字典的所有键值对
print(dic.items(), type(dic.items()))
print(list(dic.items()))  # 转成列表视图

# 字典的遍历
dic = {'id': 111, 'name': '张三'}
for item in dic:
    print(item, dic[item], dic.get(item))

# 字典生成公式
'''内置函数zip()生成,zip打包是会以短的列表为限制生成'''
item = ['aaa', 'bbb', 'ccc']
price = [220, 333, 444, 555]
d = {item.upper(): price for item, price in zip(item, price)}
print(d)
