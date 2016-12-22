#coding=utf-8
import urllib
import time

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

for i in range(38, 333):
	html = getHtml("http://www.580san.com/ip.php?%E4%B8%8A%E6%B5%B7&"+str(i)+'/')
	j = i+1
	w = open('data/'+str(j)+'.txt', 'w+')
	w.write(html)
	w.close()
	print j,'-done!'
	time.sleep(2)

#print html