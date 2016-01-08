#!/usr/bin/python
# coding: utf-8
import urllib2
import urllib
import re


def getHtml(url):
    User_Agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
    headers = {
        'User-Agent': User_Agent,
    }
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    html = response.read()
    return html



if __name__ == '__main__':
    old_url = 'http://tieba.baidu.com/p/3933793221?see_lz=1'
    totalpage_pattern = r'pn=(\d+)\">尾页'
    html = getHtml(old_url)
    page_count = int(re.findall(totalpage_pattern,html)[0])
    print 'We have found %d pages content' % page_count
    content_pattern = r'class=\"d_post_content j_d_post_content \">(.*?)</div>'
    re_cp = re.compile(content_pattern)
    f = open('f:/1.html','w')
    f.write('<!DOCTYPE html>')
    for page in range(1,11):
        url = 'http://tieba.baidu.com/p/3933793221?see_lz=1&pn=' + str(page)
        print url
        print 'Downloading the %d page' % page
        content = re.findall(re_cp,getHtml(url))
        f.writelines(content)
    f.close()

    print 'misson accomplished'
