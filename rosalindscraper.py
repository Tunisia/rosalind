#!/usr/bin/python

from bs4 import BeautifulSoup
import urllib

path = '/home/tunisia/Projects/rosalind/'

html = BeautifulSoup(urllib.urlopen('http://rosalind.info/problems/list-view/'))

tr_all = html.find_all('tr')
probnum = 0
url_base = 'http://www.rosalind.info'

for tr in tr_all[1:]:
    probnum += 1
    td =  tr.find_all('td')
    abbrev = td[0].string
    title = td[1].a.string[:-2].rstrip().replace('\n','')
    filename = 'prob%d_%s - %s.py' % (probnum,abbrev,title)
    pathNname = path+filename
    url = url_base + td[1].a['href']
    shebang = '#!/usr/bin/python\n\n'
    
    myfile = open(pathNname,'w')
    myfile.write(shebang + '# ' + url)
    myfile.close()