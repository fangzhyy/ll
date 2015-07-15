#coding:utf-8

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from ll.items import UrlItem
import urllib2
import sys
import re
import time

#'''http://movie.douban.com/celebrity/1049732/photos/'''

class testImage(BaseSpider):
    name='ll'
    search_key=["杰西卡·阿尔芭 ","斯嘉丽·约翰逊","莫妮卡·贝鲁奇","娜塔莎·金斯基", "伊娃·格林","凯拉·奈特莉","安妮·海瑟薇","泰莎·法米加"]
    allowed_domain=["douban.com"]
    start_urls=[]
    f=open('test2.txt','wb')
    reload(sys)
    sys.setdefaultencoding('utf-8')
   #for i in range(0,1120,40):    
        #start_urls.append('http://movie.douban.com/celebrity/1049732/photos/?type=C&start=%d&sortby=vote&size=a&subtype=a'%i)
    for key in search_key:
        encoded=urllib2.quote(key)
        print("http://movie.douban.com/subject_search?search_text=%s+&cat=1002"%encoded)
        start_urls.append("http://movie.douban.com/subject_search?search_text=%s+&cat=1002"%encoded)
        
    def parse(self,response):
        #get main page
        #get name
        url=response.url
        print 'url=',url
        s1=url[str.find(url,'search_text=')+len('search_text='):]
        print 's1=',s1
        s2=s1[0:str.find(s1,'+&cat')]
        print 's2=',s2
        name=urllib2.unquote(s2)
        hxs=HtmlXPathSelector(response)
        sites=hxs.select('//em/../a/@href').extract()
        items=[]
        for site in sites:
            yield Request(url=site,meta={'name':name},callback=self.parse_image_count)
    
    def parse_image_count(self, response):
        hxs=HtmlXPathSelector(response)
        sites=hxs.select('//div[@class="mod"]/div[@class="hd"]/h2/span/a/text()').extract();
        image_count=0
        for site in sites:
            id_str=""    
            for c in site:
                if(c>='0' and c<='9'):
                    id_str+=c
            if(len(id_str)>0):
                image_count=int(id_str)
                print 'count=',image_count
        base_url=response.url+'/photos/?type=C&start=%d&sortby=vote&size=a&subtype=a'
        for i in range(0,image_count,40):    
            target_url=base_url%i
            print 'target_url=',target_url
            time.sleep(1)
            yield Request(url=target_url,meta={'name':response.meta['name']},callback=self.parse_image_url)
    
    def parse_image_url(self, response):
        name=response.meta['name']
        hxs=HtmlXPathSelector(response)
        sites=hxs.select('//ul/li/div/a/img/@src').extract()
        items=[]
        for site in sites:
            site=site.replace('thumb','raw')
            item=UrlItem()
            item['url']=site
            item['name']=name
            items.append(item)
        return items
        