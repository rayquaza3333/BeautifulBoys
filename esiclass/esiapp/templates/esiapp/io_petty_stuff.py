from bs4 import BeautifulSoup
import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]


def get_href_css_js_img(file):
    with open(file, "r", encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, features='html.parser')
    urls =['about.html',
     'business.html',
     'coming_soon.html',
     'communication.html',
     'contact.html',
     'course_details.html',
     'form.html',
     'hocvien.html',
     'index.html',
     'language.html',
     'login.html',
]

    for u in urls:
        html = html.replace(u,"{% url " + "'" + "esiclass:" + u[0:-5] + "'" +" %}")

    # Affect the file
    with open(file, "w", encoding='utf-8') as f:
        f.write(html)
        f.close()


i = 1
for f in files:
    print('----[]{}: {}] \n'.format(i,f))
    get_href_css_js_img(f)
    i += 1
