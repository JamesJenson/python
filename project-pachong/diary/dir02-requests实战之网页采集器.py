import requests

# UA: User-Agent(请求载体的身份标识)
# UA检测: 门户网站的服务器会检测对应请求的载体的身份标识,如果检测到是某一款浏览器,则为正常请求
# 如果不是基于某一款的身份标识,则标识该请求为不正常请求(爬虫),服务器则会拒绝当前请求返回数据

# UA伪装:让爬虫对应的请求载体的身份标识伪装成某一款浏览器
if __name__ == "__main__":
    # UA封装到字典当中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
    }

    url = 'https://www.sogou.com/web'
    # 处理url携带的参数:封装到字典中
    kw = input("enter a word:")
    parm = {'query': kw}
    # 对指定的url发起的请求对应的url是携带参数的,并且请求过程中处理了参数
    resp = requests.get(url=url, params=parm,headers=headers)
    page_text = resp.text
    fileName = '../data/' + kw + '.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName, '保存成功!!')
