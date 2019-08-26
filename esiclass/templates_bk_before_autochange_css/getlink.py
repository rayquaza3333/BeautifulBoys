def getlink(a):
    """
    a here is the path to our html file. Ig: 'example.html'
    """

    with open(a, "r", encoding='utf-8') as f:
        text= f.read()
    # Add all urls character between with "http" and end characte
    links =[]
    link = ''
    i = 0
    add = False
    while i <= (len(text) - 7):

        check = (text[i] + text[i+1] + text[i+2] + text[i+3]+ text[i+4]+ text[i+5]+ text[i+6]).lower()
        if check == 'http://' or check =='https:/':
            add = True

        check =['"',")","<","&",">","'"]
        if text[i] in check:
            add = False
        if add:
            link += text[i]
        else:
            links.append(link)
            link = ''
        i += 1
    # Eliminate empty list item
    while '' in links:
        links.remove('')
    for x in links:
        print(x)
    print(a)

if __name__ == '__main__':
    getlink('cungduong.html')
