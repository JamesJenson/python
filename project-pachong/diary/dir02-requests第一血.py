import requests

if __name__ == "__main__":
    # 1 指定url
    url = 'https://www.sogou.com/'
    # 2 发起请求,返回的一个响应对象
    resp = requests.get(url=url)
    # 3 获取响应数据,对应地址的字符串形式的页面数据
    page_text = resp.text
    print(page_text)
    # 4 持久化存储
    with open('../data/sougou.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print('爬取数据结束!!')
