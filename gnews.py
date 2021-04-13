from requests_html import HTMLSession
session=HTMLsession()
url="https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en"
r=session.get(url)
r.html.render(sleep=1, scrolldown=0)
articles=r.html.find('article')
print('article')
nl=[]
for item in articles:
    try:
        ni=item.find('h3',first=True)
        na={
        'title':ni.text,
        'link':ni.absolute_links}
        nl.append(na)
    except:
        pass
for i in range(len(nl)):
    print(i+')'+nl[i].title+'\n')
    print('link for the article is :'+nl[i].link+'\n')