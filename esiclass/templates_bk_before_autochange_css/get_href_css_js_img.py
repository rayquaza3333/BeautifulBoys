from bs4 import BeautifulSoup
import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]


def get_href_css_js_img(file):
    hrefs =[]
    with open(file, "r", encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, features='html.parser')

    print('[anker href in {}] \n'.format(file))
    for a in soup.findAll('a'):
        print(a['href'])

    print('[href link in {}] \n'.format(file))
    for a in soup.findAll('link'):
        print(a['href'])

    print('[js script in {}] \n'.format(file))
    for a in soup.findAll('script',{"src":True}):
        print(a['src'])

    print('[img script in {}] \n'.format(file))
    for a in soup.findAll('img',{"src":True}):
        print(a['src'])


i = 1
for f in files:
    print('----[]{}: {}] \n'.format(i,f))
    get_href_css_js_img(f)
    i += 1
