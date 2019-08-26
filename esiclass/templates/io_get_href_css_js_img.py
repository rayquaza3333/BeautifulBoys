from bs4 import BeautifulSoup
import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]


def get_href_css_js_img(file):
    with open(file, "r", encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, features='html.parser')

    # Anker link
    print('[anker href in {}] \n'.format(file))
    for a in soup.findAll('a'):
        print(a['href'])

    # Handle css link
    print('[href link in {}] \n'.format(file))
    for a in soup.findAll('link'):
        if a['href'][0:4] == 'css/' and  a['href'][-4:] == '.css':
            html = html.replace(a['href'],"{% static  " + "'" + a['href'] + "'" + " %}")

    # javascript link
    print('[js script in {}] \n'.format(file))
    for a in soup.findAll('script',{"src":True}):
        if a['src'][0:3] == 'js/' and  a['src'][-3:] == '.js':
            html = html.replace(a['src'],"{% static  " + "'" + a['src'] + "'" + " %}")

    # images link
    print('[img script in {}] \n'.format(file))
    for a in soup.findAll('img',{"src":True}):
        if a['src'][0:7] == 'images/' and  a['src'][-4:] == '.jpg':
            html = html.replace(a['src'],"{% static  " + "'" + a['src'] + "'" + " %}")

    # Affect the file
    with open(file, "w", encoding='utf-8') as f:
        f.write(html)
        f.close()


i = 1
for f in files:
    print('----[]{}: {}] \n'.format(i,f))
    get_href_css_js_img(f)
    i += 1
