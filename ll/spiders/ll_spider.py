#coding:utf-8

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from ll.items import UrlItem
import urllib2
import sys

#'''http://movie.douban.com/celebrity/1049732/photos/'''

class testImage(BaseSpider):
    name='ll'
    search_key=["赵本山"]
    allowed_domain=["douban.com"]
    start_urls=[]
    f=open('test2.txt','wb')

   #for i in range(0,1120,40):    
        #start_urls.append('http://movie.douban.com/celebrity/1049732/photos/?type=C&start=%d&sortby=vote&size=a&subtype=a'%i)
    for key in search_key:
        encoded=urllib2.quote(key)
        print("http://movie.douban.com/subject_search?search_text=%s+&cat=1002"%encoded)
        start_urls.append("http://movie.douban.com/subject_search?search_text=%s+&cat=1002"%encoded)
    def parse(self,response):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        hxs=HtmlXPathSelector(response)
        #sites=hxs.select('//ul/li/div/a/img/@src').extract()
        sites=hxs.select('//em/text()').extract()
        items=[]
        for site in sites:
            #site=site.replace('thumb','raw')
            self.f.write(site.decode('utf-8'))
            self.f.write('\r\n')
            item=UrlItem()
            item['url']=site
            items.append(item)
        return items