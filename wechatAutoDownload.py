import requests
import json
import csv
import urllib.request
import pdfkit
import os, sys

def convert(file_name):
    file_name = file_name.replace('/', '_')
    file_name = file_name.replace('|', '_')
    file_name = file_name.replace(':', '_')
    file_name = file_name.replace('!', '')
    return file_name

def getHtml(url):
    html = urllib.request.urlopen(url).read()
    return html
 
def saveHtml(file_name, file_content):
    #    注意windows文件命名的禁用符，比如 /
    file_name = convert(file_name)
    with open('articles/'+file_name + ".html", "wb") as f:
        #   写文件用bytes而不是str，所以要转码
        f.write(file_content)

def getGZHJson(appid, secret):
    cnt = 0
    path = " https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential"
    url = path + "&appid=" + appid + "&secret=" + secret
    result = requests.get(url)
    token = json.loads(result.text)
    access_token = token['access_token']
    data = {
        "type": "news",
        "offset": 0,
        "count": 1,
    }
    headers = {
        'content-type': "application/json",
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    url = 'https://api.weixin.qq.com/cgi-bin/material/batchget_material?access_token=' + access_token
    result = requests.post(url=url, data=json.dumps(data), headers=headers)
    result.encoding = result.apparent_encoding
    result = json.loads(result.text)
    count = int(result['total_count'])
    gzh_dict = {"news_item": []}
    for i in range(0, count):
        data['offset'] = i
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        result.encoding = result.apparent_encoding
        result = json.loads(result.text)
        for item in result['item'][0]['content']['news_item']:
            temp_dict = {}
            temp_dict['title'] = item["title"]
            temp_dict['digest'] = item["digest"]
            temp_dict['url'] = item["url"]
            temp_dict['thumb_url'] = item["thumb_url"]
            # 保存到html
            # html = getHtml(item["url"])
            # saveHtml(item["title"], html)
            # 保存到PDF
            pdfkit.from_url(item["url"], 'articles/'+convert(item["title"])+'.pdf')
            print('[*]'+ str(cnt) +' ' + item["title"] +' Done\n')
            cnt += 1
            gzh_dict['news_item'].append(temp_dict)
    return json.dumps(gzh_dict)

if __name__ == '__main__':
    articles = getGZHJson('APPID', 'SECRET')
