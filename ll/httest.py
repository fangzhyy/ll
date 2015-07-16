import sys
from scrapy.selector import HtmlXPathSelector

f=open("ht.html")
data=f.read()
hxs=HtmlXPathSelector(data)
target=hxs.select('//em')
sites=target.select('../a/@herf').extract()
for site in sites:
    print(site)