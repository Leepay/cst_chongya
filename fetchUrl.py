url_dict = {}

url_format_to_match = 'href="https://mp.weixin.qq.com/s'
start_loc = 6
title_format_to_match = "<span>"
with open('公众号.html','r') as f:
    for line in f.readlines():
        locate_url = line.find(url_format_to_match)
        if locate_url >= 0:
            url = line[locateUrl+start_loc:].split('\"')[0]
            locate_title = line[locateUrl+start_loc:].find(title_format_to_match)
            title = line[locate_title].split('<\span>')[0]
            url_dict.update({title:url})
print(url_dict)