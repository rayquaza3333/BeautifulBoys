from bs4 import BeautifulSoup
import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]

def get_href(file):
    with open(file, "r", encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, features='html.parser')

    hrefs =[]
    print('[href in {}] \n'.format(file))
    for a in soup.findAll('a'):
        print(a['href'])

def get_css(file):
    with open(file, "r", encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, features='html.parser')
    hrefs =[]
    print('[css link in {}] \n'.format(file))
    for a in soup.findAll('link'):
        print(a['href'])

def get_js(file):
    with open(file, "r", encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, features='html.parser')

    hrefs =[]
    print('[js script in {}] \n'.format(file))
    for a in soup.findAll('script',{"src":True}):
        print(a['src'])

i = 1
for f in files:
    print('----[]{}: {}] \n'.format(i,f))
    get_href(f)
    get_css(f)
    get_js(f)
    i += 1
