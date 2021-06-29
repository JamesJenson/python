import requests
import json

if __name__ == "__main__":
    print('aaa')
    # 指定地址
    url = 'https://movie.douban.com/j/chart/top_list'
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
    }
    # 参数封装
    data = {
        'type': 24,
        'interval_id': '100:90',
        'action': '',
        'start': 0,  # 开始的索引位置
        'limit': 20  # 一次请求取出的条数
    }
    # 发起请求
    resp = requests.get(url=url, params=data, headers=headers)
    # 持久化数据
    json_str = resp.json()
    fileName = '../data/豆瓣.json'
    fp = open(fileName, 'w', encoding='utf-8')
    json.dump(json_str, fp=fp, ensure_ascii=False)
    print('over!!')
