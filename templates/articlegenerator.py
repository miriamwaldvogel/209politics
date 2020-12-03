from tkinter import Tk, IntVar, Entry, Checkbutton, Button, Label
from datetime import datetime
import os, os.path
import errno
w = Tk()
newimg = IntVar()
oldimg = IntVar()
artimg = IntVar()
smallimg = IntVar()
standimg = IntVar()
covid = IntVar()
elections = IntVar()
latest = IntVar()
opinion = IntVar()
policy = IntVar()
imgname = Entry(w)
newalt = Entry(w)
path = Entry(w)
oldalt = Entry(w)
imgalign = Entry(w)
caption = Entry(w)
credit = Entry(w)
headline = Entry(w)
htmlname = Entry(w)
pageid = Entry(w)
n = datetime.now()
d = [n.strftime("%Y"), n.strftime("%m"), n.strftime("%B"), n.strftime("%d"), "%s:%s %s"%(n.strftime("%-I"), n.strftime("%M"), n.strftime("%p").lower())]

def mkdir(p):
    try:
        os.makedirs(p)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(p):
            pass
        else: raise

def article():
    mkdir(os.path.dirname('/home/miriamwaldvogel/209politics/%s/%s/%s/'%(d[0], d[1], d[3])))
    f = open("/home/miriamwaldvogel/209politics/%s/%s/%s/%s.html"%(d[0], d[1], d[3], htmlname.get()), "w")
    f.write('<!DOCTYPE html> <html lang="en" dir="ltr"> <head> <meta charset="utf-8"> <meta name="description" content=""> <meta name="keywords" content=""> <meta name=\'viewport\' content=\'width=device-width, initial-scale=1\'> <meta name="twitter:card" content="summary"> <meta name="twitter:site" content="@209politics"> <meta name="twitter:title" content="%s"> <meta name="twitter:image" content="https://209politics.com/images/favicon.png"> <link rel="icon" type="image/png" href="/images/favicon.png"> <link rel="stylesheet" href="/css/article.css"> <link rel="stylesheet" href="/css/global.css"> <link rel="stylesheet" href="/css/footer.css"> <link rel="stylesheet" href="/css/header.css"> <link rel="stylesheet" href="/css/more.css"> <link rel="stylesheet" href="/css/stories.css"> <link href=\'https://fonts.googleapis.com/css?family=Rubik\' rel=\'stylesheet\'> <link href="https://fonts.googleapis.com/css?family=Libre Baskerville" rel="stylesheet"> <script type="text/javascript" src="/js/articleformat.js"></script> <script type="text/javascript" src="/js/header.js"></script> <script async src="https://www.googletagmanager.com/gtag/js?id=UA-174685284-1"></script> <script> window.dataLayer = window.dataLayer || []; function gtag(){dataLayer.push(arguments);} gtag(\'js\', new Date()); gtag(\'config\', \'UA-174685284-1\'); </script> <title>%s - 209 Politics</title> </head> <body> <div id="content"> <div id="headercontainer"> <button type="button" id="sidebar" onclick="sidebar();">&#9776;</button> <div id="logocontainer"> <a href="https://209politics.com/"> <img src="/images/favicon-horizontal.png" alt="209 Politics" id="logo"> </a> </div> <div id="searchcontainer"> <div id="searchimgcontainer" onclick="searchtoggle();"> <img src="/images/search.svg" alt="Search sybmol" id="searchimg"> </div> <div id="formcontainer1"> <form id="searchform" action="https://www.google.com/search" method="get"> <input type="hidden" name="q" value="site:209politics.com"> <input type="text" name="q" value="" id="searchbox1"> <input type="submit" value="GO" class="searchbutton" id="searchbutton1"> </form> </div> </div> </div> <div id="sectionscontainer" class="sections"> <div id="homenavcontainer" class="headernavcontainer"> <a href="https://209politics.com/" id="latest" class="section">HOME</a> </div> <div id="latestnavcontainer" class="headernavcontainer"> <a href="/latest" id="latest" class="section">LATEST</a> </div> <div id="electionsnavcontainer" class="headernavcontainer"> <a href="/elections" id="elections" class="section">ELECTIONS</a> </div> <div id="policynavcontainer" class="headernavcontainer"> <a href="/policy" class="section">POLICY</a> </div> <div id="intnavcontainer" class="headernavcontainer"> <a href="/covid-19" class="section">COVID-19</a> </div> <div id="contactnavcontainer" class="headernavcontainer"> <a href="/interactives" class="section">INTERACTIVES</a> </div> </div> <div id="formcontainer2"> <form id="searchform" action="https://www.google.com/search" method="get"> <input type="hidden" name="q" value="site:209politics.com"> <input type="text" name="q" value="" id="searchbox2"> <input type="submit" value="GO" class="searchbutton" id="searchbutton1"> </form> </div> <div id="filler"></div> <div id="articlecontainer"> <h1 id="title">%s</h1> <div id="infocontainer"> <p id="time">%s %d, %s at %s</p> </div> <div id="paragraphcontainer">'%(headline.get(), headline.get(), headline.get(), d[2], int(d[3]), d[0], d[4]))
    if artimg.get():
        f.write('<div id="img1container" class="%simg"><img src="%s" alt="%s" id="img1"><p id="img1caption" class="caption">%s</p><p id="img1credit" class="credit">%s</p></div>' % (imgalign.get(), imgname.get(), newalt.get(), caption.get(), credit.get()))
    g = open("/home/miriamwaldvogel/209politics/templates/article.txt", "r")
    h = g.readlines()
    for i in h:
        f.write('<p class="paragraph">')
        f.write(i)
        f.write('</p>')
    g.close()
    f.write('<div id="more"> <p id="moretitle">MORE LIKE THIS</p> <div id="morearticlescontainer"></div> </div> </div> </div> <div id="footer"> <p id="socialmediafooter"> <a href="https://twitter.com/209Politics" id="twitterfooter" class="sociallinkfooter">Twitter: @209politics</a> • <a href="https://www.instagram.com/209.politics/" id="instagramfooter" class="sociallinkfooter">Instagram: @209.politics</a> • <a href="https://www.facebook.com/209Politics" id="facebookfooter" class="sociallinkfooter">Facebook: @209Politics</a> </p> <p id="navfooter"> <a href="/index" id="homenavfooter" class="navfooter">Home</a> • <a href="/latest" id="latestnavfooter" class="navfooter">Latest</a> • <a href="/elections" id="electionsnavfooter" class="navfooter">Elections</a> • <a href="/policy" id="policynavfooter" class="navfooter">Policy</a> • <a href="/covid-19" id="covidnavfooter" class="navfooter">COVID-19</a> • <a href="/interactives" class="section">INTERACTIVES</a> • <a href="/contact" id="contactnavfooter" class="navfooter">Contact us</a> </p> </div> </body> </html> ')
    f.close()
    if newimg.get():
        if smallimg.get():
            size = ["smallimg", "smalltext"]
        else:
            size = ["standardimg", "standardtext"]
        s = '\n<div id="%scontainer" class="storycontainer bigstory"><a href="/%s/%s/%s/%s.html" class="storylink"><div class="storyimgcontainer %s"><img src="/%s/%s/%s/%s" alt="%s" class="storyimg"></div><div class="storytextcontainer %s"><p class="mainstory headline storyheadline">%s</p><p class="articledate">%s %d, %s</p></div></a></div>'%(pageid.get(), d[0], d[1], d[3], htmlname.get(), size[0], d[0], d[1], d[3], imgname.get(), newalt.get(), size[1], headline.get(), d[2], int(d[3]), d[0])
        m = '<div id="mainstorycontainer" class="mainstory"> <a href="%s/%s/%s/%s.html" id="mainstorylink" class="mainstory"> <div id="mainstoryimgcontainer"> <img src="%s/%s/%s/%s" alt="%s" id="mainstoryimg"> </div> <h1 id="mainstoryheadline" class="mainstory headline">%s</h1> <p id="mainstorydate" class="mainstory articledate">%s %d, %s</p> </a> </div>' % (d[0], d[1], d[3], htmlname.get(), d[0], d[1], d[3], imgname.get(), newalt.get(), headline.get(), d[2], int(d[3]), d[0])
    else:
        if smallimg.get():
            size = ["smallimg", "smalltext"]
        else:
            size = ["standardimg", "standardtext"]
        s = '\n<div id="%scontainer" class="storycontainer bigstory"><a href="/%s/%s/%s/%s.html" class="storylink"><div class="storyimgcontainer %s"><img src="%s" alt="%s" class="storyimg"></div><div class="storytextcontainer %s"><p class="mainstory headline storyheadline">%s</p><p class="articledate">%s %d, %s</p></div></a></div>'%(pageid.get(), d[0], d[1], d[3], htmlname.get(), size[0], path.get(), oldalt.get(), size[1], headline.get(), d[2], int(d[3]), d[0])
        m = '<div id="mainstorycontainer" class="mainstory"> <a href="%s/%s/%s/%s.html" id="mainstorylink" class="mainstory"> <div id="mainstoryimgcontainer"> <img src="%s" alt="%s" id="mainstoryimg"> </div> <h1 id="mainstoryheadline" class="mainstory headline">%s</h1> <p id="mainstorydate" class="mainstory articledate">%s %d, %s</p> </a> </div>' % (d[0], d[1], d[3], htmlname.get(), path.get() , oldalt.get(), headline.get(), d[2], int(d[3]), d[0])
    p = [covid.get(), elections.get(), latest.get(), opinion.get(), policy.get()]
    q = ["covid-191", "elections1", "latest1", "opinion1", "policy1"]
    for i, j in enumerate(p):
        if j == 1:
            f = open("/home/miriamwaldvogel/209politics/%s.html"%q[i], "r")
            g = f.read().split('<div id="articlescontainer">')
            f.close()
            f = open("/home/miriamwaldvogel/209politics/%s.html"%q[i], "w")
            f.write(g[0]+'<div id="articlescontainer">')
            f.write(s)
            f.write(g[1])
            f.close()
    f = open("/home/miriamwaldvogel/209politics/articles.html", "r")
    g = f.read().split('<div id="articlescontainer">')
    f.close()
    f = open("/home/miriamwaldvogel/209politics/articles.html", "w")
    f.write(g[0]+'<div id="articlescontainer">')
    f.write(s)
    f.write(g[1])
    f.close()
    f = open("/home/miriamwaldvogel/209politics/index.html", "r")
    g = f.read().split('<div id="leftpanel">')
    f.close()
    f = open("/home/miriamwaldvogel/209politics/index.html", "w")
    f.write(g[0]+'<div id="leftpanel">')
    f.write(m)
    h = open("/home/miriamwaldvogel/209politics/articles.html", "r")
    i = h.read()
    h.close()
    f.write(i.split('<div id="articlescontainer">', 1)[1].split('</a>', 1)[0]+"</a></div>")
    f.write(g[1].split('<br>', 1)[1])
    f.close()
    global w
    w.destroy()

Checkbutton(w, text="New image", variable=newimg).grid(row=0, column=0)
Checkbutton(w, text="Old image", variable=oldimg).grid(row=0, column=1)
Checkbutton(w, text="Article image", variable=artimg).grid(row=0, column=2)
Label(w, text="Image name").grid(row=1, column=0)
imgname.grid(row=2, column=0)
Label(w, text="Alt").grid(row=3, column=0)
newalt.grid(row=4, column=0)
Label(w, text="Path").grid(row=1, column=1)
path.grid(row=2, column=1)
Label(w, text="Alt").grid(row=3, column=1)
oldalt.grid(row=4, column=1)
Label(w, text="center/right/left").grid(row=1, column=2)
imgalign.grid(row=2, column=2)
Label(w, text="Caption").grid(row=3, column=2)
caption.grid(row=4, column=2)
Label(w, text="Credit").grid(row=5, column=2)
credit.grid(row=6, column=2)
Label(w, text="Articleinfo").grid(row=6, column=0)
Checkbutton(w, text="Small", variable=smallimg).grid(row=7, column=0)
Checkbutton(w, text="Standard", variable=standimg).grid(row=8, column=0)
Label(w, text="Headline").grid(row=9, column=0)
headline.grid(row=10, column=0)
Label(w, text="Html name").grid(row=11, column=0)
htmlname.grid(row=12, column=0)
Label(w, text="Page id").grid(row=13, column=0)
pageid.grid(row=14, column=0)
Label(w, text="Pages").grid(row=6, column=1)
Checkbutton(w, text="COVID", variable=covid).grid(row=7, column=1)
Checkbutton(w, text="Elections", variable=elections).grid(row=8, column=1)
Checkbutton(w, text="Latest", variable=latest).grid(row=9, column=1)
Checkbutton(w, text="Opinion", variable=opinion).grid(row=10, column=1)
Checkbutton(w, text="Policy", variable=policy).grid(row=11, column=1)
Button(w, text="Submit", command=article).grid(row=15, column=1)
w.mainloop()
