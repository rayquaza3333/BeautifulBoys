from bs4 import BeautifulSoup
import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]


def get_href_css_js_img(file):
    with open(file, "r", encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, features='html.parser')
#     urls =['{% url 'about' %}',
#      '{% url 'business' %}',
#      '{% url 'coming_soon' %}',
#      '{% url 'communication' %}',
#      '{% url 'contact' %}',
#      '{% url 'course_details' %}',
#      '{% url 'form' %}',
#      '{% url 'hocvien' %}',
#      '{% url 'index' %}',
#      '{% url 'language' %}',
#      '{% url 'login' %}',
# ]
#
#     for u in urls:
#         html = html.replace(u,"{% url " + "'" + "esiclass:" + u[0:-5] + "'" +" %}")

    html = html.replace("{% include 'esiapp/header.html' %}","{% include 'esiapp/header.html' %}")
    html = html.replace("{% include 'esiapp/footer.html' %}","{% include 'esiapp/footer.html' %}")

    # Affect the file
    with open(file, "w", encoding='utf-8') as f:
        f.write(html)
        f.close()


i = 1
for f in files:
    print('----[]{}: {}] \n'.format(i,f))
    get_href_css_js_img(f)
    i += 1
