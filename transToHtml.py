import urllib.request
 
def getHtml(url):
    html = urllib.request.urlopen(url).read()
    return html
 
def saveHtml(file_name, file_content):
    #    注意windows文件命名的禁用符，比如 /
    with open(file_name.replace('/', '_') + ".html", "wb") as f:
        #   写文件用bytes而不是str，所以要转码
        f.write(file_content)
 
aurl = "https://mp.weixin.qq.com/s?__biz=MzUxNTk1NDEwNg==&mid=2247483894&idx=1&sn=96d6389d41b0e73d3b2c42eb30939692&chksm=f9af8523ced80c355aa8740845ce2ca12d29eba5fa77aefce90d3ca57e050c5f8cae333cb593&token=1539350061&lang=zh_CN#rd"
html = getHtml(aurl)
saveHtml("test", html)
 
print("下载成功")