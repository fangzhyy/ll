#download.py

import sys
import os
import time
import urllib2,httplib

class imageDownload():
    filePath="../files"
    def startDownload(self):
        if not(os.path.exists(self.filePath)):
            os.mkdir(self.filePath)
        f=open("../test.txt",'r')
        content=f.readlines()
        f.close()
        for line in content:
           if(self.doDownload(line)):
               time.sleep(1)

    
    def doDownload(self, url):
        str.strip(url);
        offset=str.rfind(url, "/")
        if(offset>0):
            fileName=url[offset:]
            idStr=""
            for c in fileName:
                if(c<='9' and c>='0'):
                    idStr+=c
            if(os.path.exists(self.filePath+"/%s.jpg"%idStr)):
                return False
            refer="http://movie.douban.com/celebrity/1049732/photo/%s/"%(idStr)
            request=urllib2.Request(url)
            request.add_header("Referer", refer)
            request.add_header("User-Agent", "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; MyIE9; BTRS123646; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)")
            data=urllib2.urlopen(request).read()
            newFile=open(self.filePath+"/%s.jpg"%idStr,"w");
            newFile.write(data)
            newFile.close()
            return True
        return False
          
            
downloader=imageDownload()
downloader.startDownload()