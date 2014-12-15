# -*- coding: utf-8 -*-

import urllib2, re
import sys
import time

# urls
url = 'https://sites.google.com/site/deeplearningworkshopnips2014/accepted-papers'
check = 'deeplearningworkshopnips2014\/([\d]+?)\.pdf\?attredirects=0">([\w\W]+?)<\/a>'
# download url ( 2 parts )
durl1 = 'https://sites.google.com/site/deeplearningworkshopnips2014/'
durl2 = '.pdf?attredirects=0'

# proxy
proxy = urllib2.ProxyHandler({'http': '127.0.0.1:8087'})
proxys = urllib2.ProxyHandler({'https': '127.0.0.1:8087'})

# if  you need to use http/https mode, change the param to proxy/proxys
opener = urllib2.build_opener(proxys)
urllib2.install_opener(opener)
a = urllib2.urlopen(url)
b = a.read()
a.close()

data = re.findall( check, b)
pp = len(data)

for i in range(len(data)):

    tmp = ''.join( data[i][1].split(':') )
    tmp = ''.join( tmp.split('"') )
    
    #print i,'   ',data[i][0],data[i][1]
    fn = str(i+1) + '_' + str(data[i][0]) + '_' + tmp + '.pdf'
    print fn


    durl = durl1 + str(data[i][0]) + durl2
    try:
        a = urllib2.urlopen(durl)
    except :
        print a.geturl()
        break
    filedata = a.read()
    #a.close()
    with open(fn,"wb") as code:
        code.write(filedata)

    print str(i+1) + '/' + str(pp) + ' completed'
    time.sleep(5)





