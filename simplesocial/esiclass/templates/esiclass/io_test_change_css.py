from bs4 import BeautifulSoup
import os

def get_href_css_js_img(file):
    with open(file, "r+", encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, features='html.parser')

    # Handle css link
    print('[href link in {}] \n'.format(file))
    for a in soup.findAll('link'):
        if a['href'][0:4] == 'css/' and  a['href'][-4:] == '.css':
            # a['href'] = "{% static" + "'" + a['href'] + "'" + "%}"
            html = html.replace(a['href'],"{% static" + "'" + a['href'] + "'" + "%}")

    with open(file, "w", encoding='utf-8') as f:
        f.write(html)
        f.close()


f= 'test_header.html'
print('----[]file: {}] \n'.format(f))
get_href_css_js_img(f)
