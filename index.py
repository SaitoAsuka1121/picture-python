
from urllib import response
import requests
import os
from tqdm import tqdm
from progress.bar import IncrementalBar 
import time
import json
import random
headers={"User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}

user_agent_list = ["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/61.0",
                    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
                    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
                    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
                    ]
headers['User-Agent'] = random.choice(user_agent_list)
requests.packages.urllib3.disable_warnings()

def getImageUrl(id,file_path):
    info = requests.get("https://www.nogizaka46.net.cn/pic/nogizaka/getImageUrl?name=%s.txt" % id,headers=headers,verify=False)
    datas = json.loads(info.content.decode('utf-8'))
    bar = IncrementalBar(id+':', max = len(datas['data'])) 
    for url in datas['data']:
        time.sleep(0.3)
        save_img(url,file_path)
        bar.next()
    print()
def getMemberInfo(name,file_path):
    
    info = requests.get("https://www.nogizaka46.net.cn/pic/pic_group/getMemberInfo?name=%s" % name,headers=headers,verify=False)
    datas = json.loads(info.content.decode('utf-8'))
    for data in datas['data']:
        time.sleep(0.5)
        # print(data['memberId'] + "正在下载中!")
        getImageUrl(data['memberId'],file_path)
        

def save_img(url,file_path):
    file_name = file_path + "/" + os.path.basename(url)
    if(url!=''):
        response = requests.get(url,headers=headers,verify=False)
        with open(file_name,'wb') as f:
            f.write(response.content)
if __name__=='__main__':
    memberName = 'all'
    file_path = 'nogizaka46/%s' % memberName
    if not os.path.exists(file_path):
        print("文件夹 %s 不存在,正在建立" % file_path)
        os.makedirs(file_path)
    getMemberInfo(memberName,file_path)