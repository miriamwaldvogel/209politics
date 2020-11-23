from datetime import datetime
from pyperclip import copy
import os, os.path
import errno
def mkdir(p):
    try:
        os.makedirs(p)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(p):
            pass
        else: raise

n = datetime.now()
d = [n.strftime("%Y"), n.strftime("%m"), n.strftime("%B"), n.strftime("%d"), "%s:%s %s"%(n.strftime("%-I"), n.strftime("%M"), n.strftime("%p").lower())]
#center/right/left, img source, alt, caption, credit
i = ["center", "van-buskirk-golf-course.jpeg", "Van Buskirk Golf Course", "Van Buskirk Golf Course", "golf-advisor.com"]
t = ["Contracts, Grants Moving Forward for Van Buskirk Golf Course", "van-buskirk-contract-grants"]
l = 1
ids = [["standardimg", "standardtext"], ["smallimg", "smalltext"], ["", ""]]
id = "sj"
p = ['articles', 'covid-191', 'elections1', 'latest1', 'policy1']
q = [1, 1, 1, 1, 1, 1]
mkdir(os.path.dirname('/home/miriamwaldvogel/209politics/%s/%s/%s/'%(d[0], d[1], d[3])))
f = open("/home/miriamwaldvogel/209politics/%s/%s/%s/%s.html"%(d[0], d[1], d[3], t[1]), "w")
f.write('<!DOCTYPE html> <html lang="en" dir="ltr"> <head> <meta charset="utf-8"> <meta name="description" content=""> <meta name="keywords" content=""> <meta name=\'viewport\' content=\'width=device-width, initial-scale=1\'> <meta name="twitter:card" content="summary"> <meta name="twitter:site" content="@209politics"> <meta name="twitter:title" content="%s"> <meta name="twitter:image" content="https://209politics.com/images/favicon.png"> <link rel="icon" type="image/png" href="/images/favicon.png"> <link rel="stylesheet" href="/css/article.css"> <link rel="stylesheet" href="/css/global.css"> <link rel="stylesheet" href="/css/footer.css"> <link rel="stylesheet" href="/css/header.css"> <link rel="stylesheet" href="/css/more.css"> <link rel="stylesheet" href="/css/stories.css"> <link href=\'https://fonts.googleapis.com/css?family=Rubik\' rel=\'stylesheet\'> <link href="https://fonts.googleapis.com/css?family=Libre Baskerville" rel="stylesheet"> <script type="text/javascript" src="/js/articleformat.js"></script> <script type="text/javascript" src="/js/header.js"></script> <script async src="https://www.googletagmanager.com/gtag/js?id=UA-174685284-1"></script> <script> window.dataLayer = window.dataLayer || []; function gtag(){dataLayer.push(arguments);} gtag(\'js\', new Date()); gtag(\'config\', \'UA-174685284-1\'); </script> <title>%s - 209 Politics</title> </head> <body> <div id="content"> <div id="headercontainer"> <button type="button" id="sidebar" onclick="sidebar();">&#9776;</button> <div id="logocontainer"> <a href="https://209politics.com/"> <img src="/images/favicon-horizontal.png" alt="209 Politics" id="logo"> </a> </div> <div id="searchcontainer"> <div id="searchimgcontainer" onclick="searchtoggle();"> <img src="/images/search.svg" alt="Search sybmol" id="searchimg"> </div> <div id="formcontainer1"> <form id="searchform" action="https://www.google.com/search" method="get"> <input type="hidden" name="q" value="site:209politics.com"> <input type="text" name="q" value="" id="searchbox1"> <input type="submit" value="GO" class="searchbutton" id="searchbutton1"> </form> </div> </div> </div> <div id="sectionscontainer" class="sections"> <div id="homenavcontainer" class="headernavcontainer"> <a href="https://209politics.com/" id="latest" class="section">HOME</a> </div> <div id="latestnavcontainer" class="headernavcontainer"> <a href="/latest" id="latest" class="section">LATEST</a> </div> <div id="electionsnavcontainer" class="headernavcontainer"> <a href="/elections" id="elections" class="section">ELECTIONS</a> </div> <div id="policynavcontainer" class="headernavcontainer"> <a href="/policy" class="section">POLICY</a> </div> <div id="covidnavcontainer" class="headernavcontainer"> <a href="/covid-19" class="section">COVID-19</a> </div> <div id="contactnavcontainer" class="headernavcontainer"> <a href="/contact" class="section">CONTACT US</a> </div> </div> <div id="formcontainer2"> <form id="searchform" action="https://www.google.com/search" method="get"> <input type="hidden" name="q" value="site:209politics.com"> <input type="text" name="q" value="" id="searchbox2"> <input type="submit" value="GO" class="searchbutton" id="searchbutton1"> </form> </div> <div id="filler"></div> <div id="articlecontainer"> <h1 id="title">%s</h1> <div id="infocontainer"> <p id="time">%s %d, %s at %s</p> </div> <div id="paragraphcontainer">'%(t[0], t[0], t[0], d[2], int(d[3]), d[0], d[4]))
if i != ["", "", "", "", ""]:
    f.write('<div id="img1container" class="%simg"><img src="%s" alt="%s" id="img1"><p id="img1caption" class="caption">%s</p><p id="img1credit" class="credit">%s</p></div>' % (i[0], i[1], i[2], i[3], i[4]))
g = open("/home/miriamwaldvogel/209politics/templates/article.txt", "r")
h = g.readlines()
for i in h:
    f.write('<p class="paragraph">')
    f.write(i)
    f.write('</p>')
g.close()
f.write('<div id="more"> <p id="moretitle">MORE LIKE THIS</p> <div id="morearticlescontainer"></div> </div> </div> </div> <div id="footer"> <p id="socialmediafooter"> <a href="https://twitter.com/209Politics" id="twitterfooter" class="sociallinkfooter">Twitter: @209politics</a> • <a href="https://www.instagram.com/209.politics/" id="instagramfooter" class="sociallinkfooter">Instagram: @209.politics</a> • <a href="https://www.facebook.com/209Politics" id="facebookfooter" class="sociallinkfooter">Facebook: @209Politics</a> </p> <p id="navfooter"> <a href="/index" id="homenavfooter" class="navfooter">Home</a> • <a href="/latest" id="latestnavfooter" class="navfooter">Latest</a> • <a href="/elections" id="electionsnavfooter" class="navfooter">Elections</a> • <a href="/policy" id="policynavfooter" class="navfooter">Policy</a> • <a href="/covid-19" id="covidnavfooter" class="navfooter">COVID-19</a> • <a href="/contact" id="contactnavfooter" class="navfooter">Contact us</a> </p> </div> </body> </html> ')
f.close()
copy('<div id="%scontainer" class="storycontainer bigstory"><a href="/%s/%s/%s/%s.html" class="storylink"><div class="storyimgcontainer %s"><img src="/%s/%s/%s/%s" alt="%s" class="storyimg"></div><div class="storytextcontainer %s"><p class="mainstory headline storyheadline">%s</p><p class="articledate">%s %d, %s</p></div></a></div>'%(id, d[0], d[1], d[3], t[1], ids[l][0], d[0], d[1], d[3], i[0], i[2], ids[l][1], t[0], d[2], int(d[3]), d[0]))
s = '\n<div id="%scontainer" class="storycontainer bigstory"><a href="/%s/%s/%s/%s.html" class="storylink"><div class="storyimgcontainer %s"><img src="/%s/%s/%s/%s" alt="%s" class="storyimg"></div><div class="storytextcontainer %s"><p class="mainstory headline storyheadline">%s</p><p class="articledate">%s %d, %s</p></div></a></div>'%(id, d[0], d[1], d[3], t[1], ids[l][0], d[0], d[1], d[3], i[0], i[2], ids[l][1], t[0], d[2], int(d[3]), d[0])
copy(s)
for i, j in enumerate(p):
    if q[i] == 1:
        print(j)
        f = open("/home/miriamwaldvogel/209politics/%s.html"%j, "r")
        g = f.read().split('<div id="articlescontainer">')
        f.close()
        f = open("/home/miriamwaldvogel/209politics/%s.html"%j, "w")
        f.write(g[0]+'<div id="articlescontainer">')
        f.write(s)
        f.write(g[1])
        f.close()
