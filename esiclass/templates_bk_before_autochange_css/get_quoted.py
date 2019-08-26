from bs4 import BeautifulSoup
import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]

i = 1

for f in files:
    print('----[]{}: {}] \n'.format(i,f))

    """
    a here is the path to our html file. Ig: 'example.html'
    """

    with open(f, "r", encoding='utf-8') as f:
        text= f.read()
    # Add all urls character between with "http" and end characte
    links =[]
    link = ''
    i = 0
    add = False
    while i <= (len(text) - 2):

        if text[i] == '"' or text[i] == "'":
            check = text[i]
            while True:
                if text[i+1] == check or text[i+1] == check:
                    links.append(link)
                    link = ''
                    break
                    # i += should be placed outside of this loop todo
                    # prevent the outside loop from infinity loops
                else:
                    link += text[i+1]
                    i += 1
                print(text[i+1])
        i += 1
    # Eliminate empty list item
    while '' in links:
        links.remove('')
    for x in links:
        print(x)
