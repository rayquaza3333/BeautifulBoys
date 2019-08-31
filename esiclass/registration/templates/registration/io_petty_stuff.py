from bs4 import BeautifulSoup
import os
files = ('pronoun.html',)


def get_href_css_js_img(file):
    with open(file, "r", encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, features='html.parser')


    # link link


    # Anker link
    # print('[anker href in {}] \n'.format(file))
    # for a in soup.findAll('a'):
    #     print(a['href'])


    # Handle css link


    # javascript link
    print('[js script in {}] \n'.format(file))
    for a in soup.findAll('script',{"src":True}):
        if a['src'][-3:] == '.js':
            html = html.replace(a['src'],"{% static  " + "'" + "esiapp/" + a['src'] + "'" + " %}")

    # images link

    # Affect the file
    with open(file, "w", encoding='utf-8') as f:
        f.write(html)
        f.close()


i = 1
for f in files:
    print('----[]{}: {}] \n'.format(i,f))
    get_href_css_js_img(f)
    i += 1
