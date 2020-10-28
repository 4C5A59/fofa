# !/usr/bin/env python
# coding: utf-8

import requests, re
import urllib

headers = {
        'Accept-Encoding' : 'gzip, deflate',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36'
    }
    
def login(url, i):
     print('check no.',i)
     try: 
        login_url = '{}/logincheck_code.php'.format(url)   
        res = requests.get(login_url,headers=headers,timeout=5)                
        if '"status":1' in res.text:
           content = urllib.urlopen(url).read()
           title = re.findall(r'<title>(.*?)</title>', content)
           print url
           with open('TDurl.txt', 'a') as f:
                f.write(url +'                    ' + title[0] + '\n')       
        else:
            pass
     except:
        pass
    
def get_url():
    i = 1
    with open('affffofa.txt', 'r') as f:
        for line in f:
            url = line.replace('\n', '')
            if url[0:5] == 'https':
                url = url
            elif url[0:4] == 'http':
                url = url
            else:
                url = 'http://' + url
            login(url, i)
            i += 1

if __name__ == '__main__':  
    get_url()