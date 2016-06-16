from bs4 import BeautifulSoup
import urllib.request
class info:
    name=""
    title=""
    count=0
    url=""
def getdata(str):
    infolist=list()
    url=urllib.request.urlopen("http://www.douyu.com/directory/game/LOL")
    soup = BeautifulSoup(url,"html5lib")
    s=soup.select('#live-list-contentbox > li')
    for x in s:
        t=info()
        t.title= x.find("h3", class_="ellipsis").string
        t.name= x.find("span", class_="dy-name ellipsis fl").string
        t.count=x.find("span",class_="dy-num fr").string
        t.url="http://www.douyu.com/"+x["data-rid"]
        infolist.append(t)
    return infolist