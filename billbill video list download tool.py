import requests
import json
import os
from datetime import datetime

from bs4 import BeautifulSoup

# 参考链接:
#   https://zhuanlan.zhihu.com/p/117569614
#   https://blog.csdn.net/weixin_42914706/article/details/129112667

def print_directory(data):
    soup = BeautifulSoup(data, 'html.parser')
    target = 'window.__INITIAL_STATE__='
    script_tags = soup.find_all('script')
    count = 1
    for script in script_tags:
        if target in script.text:
            data = script.text.replace(target, "").split('};')[0] + '}'
            data = json.loads(data)
            for index in data.get('videoData').get('pages'):
                print('P{0} {1}'.format(count, index.get('part')))
                count += 1
            break


if __name__ == '__main__':
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = 'Bilibili视频目录_{0}.txt'.format(current_time)
    
    # 在这里设置你想要分析的B站视频URL
    url = "https://www.bilibili.com/video/BV1Qi4y1R7tW"  # 请替换为实际的B站视频URL
    
    if url == "t":
        print("请先在代码中设置正确的B站视频URL")
        print("请修改第36行的url变量，将其替换为实际的B站视频URL")
    else:
        print("网址: ", url)
        print("访问网址获取数据")
        # 添加请求头以模拟浏览器访问
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Referer': 'https://www.bilibili.com/',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
        res = requests.get(url, headers=headers)
        if os.path.exists(file_name):
            os.remove(file_name)
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(res.text)
        print_directory(res.text)
input( )