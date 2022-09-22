import pdfkit
import os, sys
cur_file_dir = os.path.abspath(__file__).rsplit("\\", 1)[0]

# 你自己填入url
url = "https://mp.weixin.qq.com/s?__biz=MzUxNTk1NDEwNg==&mid=2247483894&idx=1&sn=96d6389d41b0e73d3b2c42eb30939692&chksm=f9af8523ced80c355aa8740845ce2ca12d29eba5fa77aefce90d3ca57e050c5f8cae333cb593&token=1539350061&lang=zh_CN#rd"

output_path = os.path.join(cur_file_dir, 'test.pdf')
pdfkit.from_url(url, output_path)