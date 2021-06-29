import requests
import json

if __name__ == "__main__":
    # 指定url
    post_url = 'https://fanyi.baidu.com/sug'
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
    }
    # 参数处理
    kw = input('enter a word:')
    data = {
        'kw': kw
    }
    # 获取结果
    resp = requests.post(url=post_url, data=data, headers=headers)
    # 处理结果,json()方法返回的是obj(服务器响应的结果是json数据类型,则可以用json(),否则会报错),响应数据类型看Content-Type = Application/json
    json_str = resp.json()
    # print(json_str)
    # 持久化存储
    fileName = '../data/' + kw + '.json'
    fp = open(fileName, 'w', encoding='utf-8')
    json.dump(json_str, fp=fp, ensure_ascii=False)
    print('over!!')
