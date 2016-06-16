import time
from datetime import timedelta
from multiprocessing import Pool

import requests
from BeautifulSoup import BeautifulSoup as BS
from urlparse import urljoin, urldefrag

from tornado import httpclient, gen, ioloop, queues


AUTH = ('root','zhangjie123')
import base64
b64s = base64.encodestring('%s:%s' % AUTH)[:-1]
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Authorization': 'Basic %s' % b64s,
    'Accept-Encoding':'gzip, deflate',
    'Accept': '*/*',
    'Connection':'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
}

URLS = {
    'HX':'http://www.huxiu.com/whatsnew.html?f=nav_article_whatsnew',
}

base_url = 'http://www.huxiu.com/whatsnew.html?f=nav_article_whatsnew'
concurrency = 10

ss = requests.session()
ss.headers.update(HEADERS)

post_ss = requests.session()
DATAS = []

def normal_get(url):
    s = time.time()
    rsp = ss.get(url)
    print('fetched %s' % url)
    soup = BS(rsp.content)
    domain = 'http://www.huxiu.com'
    div_tags = soup.findAll('div', attrs={'class':'mob-ctt'}, limit=10)
    urls = [domain + div.a.get('href') for div in div_tags]
    print 'handle base url using time: %.3f seconds' % (time.time()-s)
    return urls

def detail_hand(detail_url):
    rsp = ss.get(detail_url)
    if rsp.ok:
        data = {}
        soup = BS(rsp.content)
        print 'handling detial url %s' % (detail_url,)
        title_tag = soup.find('h1', attrs={'class':'t-h1'})
        data['title'] = title_tag.text
        content_tag = soup.find('div', attrs={'id':'article_content'})
        p_tags = content_tag.findAll('p')
        data['summary'] = p_tags[0].text
        res = (p_tag.text for p_tag in p_tags)
        data['content'] = '\n'.join(res)
        data['category'] = 'http://127.0.0.1:8000/api-info/categorys/3/'

        global DATAS
        DATAS.append(data)

def post_to_mydb(data):
    post_url = 'http://localhost:8000/api-info/news.json'
    rsp = post_ss.post(post_url, auth=AUTH, data=data)
    print rsp.status_code


def main():
    start = time.time()
    urls = normal_get(base_url)
    map(detail_hand, urls)
    #io_loop = ioloop.IOLoop.current()
    #io_loop.run_sync(foo)
    pool = Pool(5)
    pool.map(post_to_mydb, DATAS)
    pool.close()
    pool.join()
    
    print 'Done in %.3f seconds' % (time.time() - start,)



if __name__ == '__main__':
    main()
