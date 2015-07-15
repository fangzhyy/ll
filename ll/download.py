# -*- coding: utf-8 -*-
import sys
import os
import time
import urllib2,httplib
import json
import codecs
class imageDownload():
    filePath="../files"
    reload(sys)
    sys.setdefaultencoding('utf-8')    
    def startDownload(self):
        if not(os.path.exists(self.filePath)):
            os.mkdir(self.filePath)
        with codecs.open('../imageUrls.json', 'r','utf-8') as f:
            for line in f:
                self.doDownload(line)

    
    def doDownload(self, item):
        jitem = json.loads(item, encoding="utf-8")
        url=jitem['url'].encode('ascii')
        name=jitem['name']
        folder="../files/%s"%name
        if not(os.path.exists(folder)):
            os.mkdir(folder)        
        offset=str.rfind(url, u"/")
        if(offset>0):
            fileName=url[offset:]
            idStr=""
            for c in fileName:
                if(c<='9' and c>='0'):
                    idStr+=c
            if(os.path.exists(folder+"/%s.jpg"%idStr)):
                return False
            refer="http://movie.douban.com/celebrity/1049732/photo/%s/"%(idStr)
            request=urllib2.Request(url)
            request.add_header("Referer", refer)
            request.add_header("User-Agent", "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; MyIE9; BTRS123646; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)")
            data=urllib2.urlopen(request).read()
            print 'datalen = ', len(data)
            newFile=open(folder+"/%s.jpg"%idStr,"w");
            newFile.write(data)
            newFile.close()
            return True
        return False
          
            
downloader=imageDownload()
downloader.startDownload()