from bs4 import BeautifulSoup
import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]


def get_href_css_js_img(file):
    with open(file, "r", encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, features='html.parser')
#     urls =['{% url 'esiapp:about' %}',
#      '{% url 'esiapp:business' %}',
#      '{% url 'esiapp:coming_soon' %}',
#      '{% url 'esiapp:communication' %}',
#      '{% url 'esiapp:contact' %}',
#      '{% url 'esiapp:course_details' %}',
#      '{% url 'esiapp:form' %}',
#      '{% url 'esiapp:hocvien' %}',
#      '{% url 'esiapp:index' %}',
#      '{% url 'esiapp:language' %}',
#      '{% url 'esiapp:login' %}',
# ]
#
#     for u in urls:
#         html = html.replace(u,"{% url " + "'" + "esiclass:" + u[0:-5] + "'" +" %}")

    html = html.replace("'{% url 'esiapp:","'{% url 'esiapp:")

    # Affect the file
    with open(file, "w", encoding='utf-8') as f:
        f.write(html)
        f.close()


i = 1
for f in files:
    print('----[]{}: {}] \n'.format(i,f))
    get_href_css_js_img(f)
    i += 1
