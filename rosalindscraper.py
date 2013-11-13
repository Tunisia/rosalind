#!/usr/bin/python

from bs4 import BeautifulSoup
import urllib

path = '/home/tunisia/Desktop/Project Euler/'

for probnum in range(1,444):
    html = BeautifulSoup(urllib.urlopen('http://projecteuler.net/problem=%d' % probnum))
    title = html.h2
    title = title.get_text().replace('/','_')
    filename = 'prob%d - %s.py' % (probnum, title)
    pathNname = path + filename
    
    task = html.find('div', attrs = {'class' : 'problem_content'})
    task = task.get_text().strip().split('\n')
    task = '\n'.join(['#' + line for line in task])
    
    file = open(pathNname,'w')
    file.write('#!/usr/bin/python\n\n' + task)
    file.close()
