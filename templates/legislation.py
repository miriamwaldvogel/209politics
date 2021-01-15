# -*- coding: utf-8 -*-
import csv, re
filter = {}
sl = 13
tl = 22
people = {'mcnerney': ['jerry-mcnerney', 'McNerney', 'congress'],
'harder': ['josh-harder', 'Harder', 'congress'],
'eggman': ['susan-talamantes-eggman', 'Eggman', 'legislature'],
'cooper': ['jim-cooper', 'Cooper', 'legislature'],
'villapudua': ['carlos-villapudua', 'Villapudua', 'legislature'],
'flora': ['heath-flora', 'Flora', 'legislature']
}
statelegs = [{"Aguiar-Curry": ["D", "Winters", "Cecilia "],
"Bauer-Kahan": ["D", "Orinda", "Rebecca "],
"Bloom": ["D", "Santa Monica", "Richard "],
"Bonta": ["D", "Oakland", "Rob "],
"Burke":["D", "Inglewood", "Autumn "],
"Carrillo":["D", "Los Angeles", "Wendy "],
"Cooper": ["D", "Elk Grove", "Jim "],
"Cristina Garcia": ["D", "Bell Gardens", ""],
"Eduardo Garcia": ["D", "Coachella", ""],
"Flora": ["R", "Manteca", "Heath "],
"Irwin":["D", "Thousand Oaks", "Jacqui "],
"Low": ["D", "Silicon Valley", "Evan "],
"Mayes": ["I", "Palm Springs", "Chads"],
"Muratsuchi": ["D", "Torrance", "Al "],
"Petrie-Norris": ["D", "Laguna Beach", "Cottie "],
"Quirk": ["D", "Hayward", "Bill "],
"Quirk-Silva": ["D", "Fullerton", "Sharon "],
"Reyes": ["D", "San Bernardino", "Eloise "],
"Robert Rivas": ["D", "Hollister", ""],
"Blanca Rubio": ["D", "Baldwin Park", ""],
"Santiago": ["D", "Los Angeles", "Miguel "],
"Stone": ["D", "Monterey", "Mark "],
"Villapudua": ["D", "Stockton", "Carlos "],
"Wicks": ["D", "Berkeley", "Buffy "],
"Weber": ["D", "San Diego", "Shirley "],
"Wood": ["D", "Santa Rosa", "Jim "]
},
{
"Borgeas": ["R", "Fresno", "Andreas "],
"Caballero": ["D", "Merced", "Anna "],
"Eggman": ["D", "Stockton", "Susan Talamantes "],
"Gonzalez":["D", "Long Beach", "Lena "],
"Limón":["D", "Santa Barbara", "Monique "],
"McGuire": ["D", "Santa Rosa", "Mike "],
"Wiener": ["D", "San Francisco", "Scott "],
}]
allleg = {}
def filteradd(p, k, a, j):
    global filter
    if a not in filter[p][k]:
        filter[p][k][a] = [j]
    else:
        filter[p][k][a].append(j)
def makefilters(p, a, n):
    s = """<div class="filters">
<p class="filtertitle">%s</p>"""%n
    for i in filter[p][a]:
        s += """\n<div class="filterbox">
<input type="checkbox" id="%s" class="checkbox" onchange="filter('%s', '%s', '%s');" checked="true">
<label for="%s" class="filter">%s</label>
</div>"""%(i.replace(" ", "-"), p, i, a, i.replace(" ", "-"), i)
    s += '\n</div>\n'
    return(s)
def leg(pol):
    global filter, allleg
    f = open('/home/miriamwaldvogel/209politics/projects/legislativetracker/data/%s-leg.csv'%pol, 'r')
    filter[pol] = {'type': {}, 'role':{
    'sponsor': [],
    'cosponsor': [],
    }, 'status':{}, 'area':{}, 'committees':{}, 'date':[]}
    r = csv.reader(f)
    header = next(r)
    o = 9
    p = ''
    for j, i in enumerate(r):
        if i[0] not in allleg:
            allleg[i[0]] = i
        elif i != allleg[i[0]]:
            print(i)
            print(allleg[i[0]])
        filter[pol]['date'].append(i[4])
        if people[pol][1] in i[5]:
            filter[pol]['role']['sponsor'].append(j)
        else:
            filter[pol]['role']['cosponsor'].append(j)
        filteradd(pol, 'area', i[3], j)
        filteradd(pol, 'type', i[1], j)
        for k in i[7].split("/"):
            filteradd(pol, 'committees', k, j)
        s = ''
        legstatus = i.index('TRUE')
        if header[legstatus] in filter[pol]['status']:
            filter[pol]['status'][header[legstatus]].append(j)
        else:
            filter[pol]['status'][header[legstatus]] = [j]
        if legstatus % 2 == 1:
            for k, l in enumerate(header[o:]):
                if i[k+o] == "":
                    break
                if k+o == legstatus:
                    s+=('<p class="status current">%s</p>'%l)
                elif k % 2 == 0 and k != 2 and k != 6:
                    s+=('<p class="status">%s</p>'%l)
        else:
            for k, l in enumerate(header[o:]):
                if i[k+o] == "":
                    break
                if k+o == legstatus:
                    s+=('<p class="status current">%s</p>'%l)
                    if k != 9:
                        break
                elif k % 2 == 0 and k != 2 and k != 6:
                    s+=('<p class="status">%s</p>'%l)
        if pol != "harder" and pol != "mcnerney":
            a = '<a href="/projects/legislativetracker/%s/%s.html" class="cosponsorlink">' % (people[pol][2], i[0].replace('.', '', 2).lower().replace(' ', '-', 1))
        else:
            a = '<a href="%s" class="cosponsorlink" target="_blank">' % i[6]
        billname = i[0].replace('.', '', 2).lower().replace(' ', '-', 1)
        p += """
        <div class="leg show">
            <p class="name"><a href="/projects/legislativetracker/%s/%s.html?acq=%s" class="leglink">%s - %s</a></p>
            <p class="desc">%s</p>
            <p class="are">Policy Area: %s</p>
            <p class="date">Introduced: %s</p>
            <p class="sponsor">Sponsor: %s | %s view cosponsors</a></p>
            <p class="com">Committees: %s</p>
            <p class="action">Latest action: %s</p>
            <div class="statuscontainer">
                <p class="statustitle">Status: </p>
                %s
            </div>
        </div>""" % (people[pol][2], billname, people[pol][0], i[1], i[0], i[2], i[3], i[4], i[5], a, i[7], i[8], s)
        if billname == "hr-40":
            legfile = open("/home/miriamwaldvogel/209politics/projects/legislativetracker/data/%s/%s.csv"%(people[pol][2], billname), "r")
            legr = csv.reader(legfile)
            legr.next()
            g = open("/home/miriamwaldvogel/209politics/projects/legislativetracker/%s/%s.html"%(people[pol][2], billname), "w")
            g.write("""<!DOCTYPE html>
            <html lang="en" dir="ltr">
            <head>
              <meta charset="utf-8">
              <meta name="description" content="">
              <meta name="keywords" content="">
              <meta name='viewport' content='width=device-width, initial-scale=1'>
              <link rel="icon" type="image/png" href="/images/favicon.png">
              <link rel="stylesheet" href="/css/header.css">
              <link rel="stylesheet" href="/css/global.css">
              <link rel="stylesheet" href="/css/footer.css">
              <link rel="stylesheet" href="../css/legislation.css">
              <link href='https://fonts.googleapis.com/css?family=Rubik' rel='stylesheet'>
              <link href="https://fonts.googleapis.com/css?family=Libre Baskerville" rel="stylesheet">
              <script type="text/javascript" src="/js/header.js"></script>
              <script async src="https://www.googletagmanager.com/gtag/js?id=UA-174685284-1"></script>
              <script>
                window.dataLayer = window.dataLayer || [];

                function gtag() {
                  dataLayer.push(arguments);
                }
                gtag('js', new Date());
                gtag('config', 'UA-174685284-1');
              </script>
              <title>%s - 209 Politics Legislative Tracker</title>
            </head>
            <body>
              <div id="content">
                <div id="headercontainer">
                  <button type="button" id="sidebar" onclick="sidebar();">&#9776;</button>
                  <div id="logocontainer">
                    <a href="https://209politics.com/">
                      <img src="/images/favicon-horizontal.png" alt="209 Politics" id="logo">
                    </a>
                  </div>
                  <div id="searchcontainer">
                    <div id="searchimgcontainer" onclick="searchtoggle();">
                      <img src="/images/search.svg" alt="Search sybmol" id="searchimg">
                    </div>
                    <div id="formcontainer1">
                      <form id="searchform" action="https://www.google.com/search" method="get">
                        <input type="hidden" name="q" value="site:209politics.com">
                        <input type="text" name="q" value="" id="searchbox1">
                        <input type="submit" value="GO" class="searchbutton" id="searchbutton1">
                      </form>
                    </div>
                  </div>
                </div>
                <div id="sectionscontainer" class="sections">
                  <div id="homenavcontainer" class="headernavcontainer">
                    <a href="https://209politics.com/" id="latest" class="section">HOME</a>
                  </div>
                  <div id="latestnavcontainer" class="headernavcontainer">
                    <a href="/latest" id="latest" class="section">LATEST</a>
                  </div>
                  <div id="electionsnavcontainer" class="headernavcontainer">
                    <a href="/elections" id="elections" class="section">ELECTIONS</a>
                  </div>
                  <div id="policynavcontainer" class="headernavcontainer">
                    <a href="/policy" class="section">POLICY</a>
                  </div>
                  <div id="covidnavcontainer" class="headernavcontainer">
                    <a href="/covid-19" class="section">COVID-19</a>
                  </div>
                  <div id="intnavcontainer" class="headernavcontainer">
                    <a href="/interactives" class="section">INTERACTIVES</a>
                  </div>
                </div>
                <div id="formcontainer2">
                  <form id="searchform" action="https://www.google.com/search" method="get">
                    <input type="hidden" name="q" value="site:209politics.com">
                    <input type="text" name="q" value="" id="searchbox2">
                    <input type="submit" value="GO" class="searchbutton" id="searchbutton1">
                  </form>
                </div>
                <div id="filler"></div>
                <div id="titlecontainer">
                  <div id="backbutton"><a href="" id="backurl">BACK</a></div>
                  <h1 id="title">%s</h1>
                  <p id="legtext"><b>%s</b> - %s</p>
                </div>
                <div id="firstleginfo">
                  <p class="are">Policy Area: %s</p>
                  <p class="date">Introduced: %s</p>
                  <div id="sponsors">
                  """%(i[0], i[0], i[1], i[2], i[3], i[4]))
            if pol != "mcnerney" and pol != "harder":
                involved = legr.next()
                role = ["Principal coauthors: ", "Coauthors: "]
                title = ["Asms. ", "Sens. "]
                z = re.split(", | and |and ", involved[2])
                allinvolved = ''
                q = "<p>Introduced by "
                if "Assembly" in z[0]:
                    if len(z) > 1:
                        q += "Asms. "
                    else:
                        q += "Asm. "
                    z[0] = z[0].split(" ", 2)[2]
                else:
                    if len(z) > 1:
                        q += "Sens. "
                    else:
                        q += "Sen. "
                for k in z:
                    if k != "":
                        memberinfo = statelegs[0][k]
                        q += "%s%s (%s-%s), "%(memberinfo[2], k, memberinfo[0], memberinfo[1])
                q = q[:len(q)-2]
                q += "</p>\n"
                allinvolved += q
                for m, k in enumerate(role):
                        q = "<p>%s"%k
                        for o in range(3, 5):
                            if involved[2*m+o] != "":
                                q += title[o-3]
                                for l in re.split(", | and |and ", involved[2*m+o]):
                                    if l != "":
                                        memberinfo = statelegs[o-3][l]
                                        q += "%s%s (%s-%s), "%(memberinfo[2], l, memberinfo[0], memberinfo[1])
                        q = q[:len(q)-2]
                        q += "</p>\n"
                        if len(q) > 27:
                            allinvolved += q
            else:
                allinvolved = i[5]
            actionlist = []
            for k in legr:
                actionlist.append('<p class="action">%s - %s</p>'%(k[0], k[1]))
                lastdate = k[0]
                lastaction = k[1]
            actions = ''
            for k in actionlist[::-1]:
                actions += k
            legfile.close()
            g.write("""
                    %s
                  </div>
                  <p id="togglesponsors" onclick="sponsortoggle();"></p>
                  <p class="com">Committees: %s</p>
                  <p class="actiontop">Latest action: %s - %s</a>
                  </p>
                  <div class="statuscontainer">
                    <p class="statustitle">Status: </p>
                    %s
                  </div>
                </div>
                <div id="legdesc">
                  <p class="legdesc"></p>
                </div>
                <div id="actions">
                  <p id="actionstitle">Actions</p>
                  %s
                </div>
                <div id="footer">
                  <p id="socialmediafooter">
                    <a href="https://twitter.com/209Politics" id="twitterfooter" class="sociallinkfooter">Twitter: @209Politics</a> •
                    <a href="https://www.instagram.com/209.politics/" id="instagramfooter" class="sociallinkfooter">Instagram: @209.politics</a> •
                    <a href="https://www.facebook.com/209politics" id="facebookfooter" class="sociallinkfooter">Facebook: @209Politics</a>
                  </p>
                  <p id="navfooter">
                    <a href="https://209politics.com/" id="homenavfooter" class="navfooter">Home</a> •
                    <a href="/latest" id="latestnavfooter" class="navfooter">Latest</a> •
                    <a href="/elections" id="electionsnavfooter" class="navfooter">Elections</a> •
                    <a href="/policy" id="policynavfooter" class="navfooter">Policy</a> •
                    <a href="/covid-19" id="covidnavfooter" class="navfooter">COVID-19</a> •
                    <a href="/interactives" id="covidnavfooter" class="navfooter">Interactives</a> •
                    <a href="/contact" id="contactnavfooter" class="navfooter">Contact us</a>
                  </p>
                </div>
              </div>
              <script type="text/javascript" src="../js/leg.js"></script>
            </body>
            </html>"""%(allinvolved, i[7], lastdate, lastaction, s, actions))
            g.close()
    f.close()
    statusfilters = ''
    for i in filter[pol]['status']:
        statusfilters += """<div class="filterbox">
<input type="checkbox" id="%s" class="checkbox" onchange="filter('%s', '%s', 'status');" checked="true">
<label for="%s" class="filter">%s</label>
</div>\n"""%(i.replace(" ", "-"), pol, i, i.replace(" ", "-"), i)
    areafilters = ''
    for i in filter[pol]['area']:
        areafilters += """<div class="filterbox">
    <input type="checkbox" id="%s" class="checkbox" onchange="filter('%s', '%s', 'area');" checked="true">
    <label for="%s" class="filter">%s</label>
    </div>\n""" % (i.replace(" ", "-"), pol, i, i.replace(" ", "-"), i)
    f = open('/home/miriamwaldvogel/209politics/projects/legislativetracker/people/%s.html' % people[pol][0], 'r')
    g = f.read().split('<!--Python marker-->', 1)
    f.close()
    f = open('/home/miriamwaldvogel/209politics/projects/legislativetracker/people/%s.html' % people[pol][0], 'w')
    f.write(g[0]+'<!--Python marker-->\n'+makefilters(pol, 'type', 'Legislation type')+makefilters(pol, 'status', 'Status')+makefilters(pol, 'area', 'Policy area')+makefilters(pol, 'committees', "Committees"))
    f.write("""<input type="reset" id="datereset" value="Reset all" onclick="showall();">
        </form>
        </div>
        </div>
        <div id="filterimgcontainer" onclick="filtershow();">
        <img src="/images/filter.svg" alt="filter" id="filterimg">
        </div>
        <div id="legcontainer">
        <p id="legtitle">Sponsored and cosponsored legislation</p>
        <div id="legislation">"""+p)
    f.write('</div>\n</div>'+'<div id="footer">'+g[1].split('<div id="footer">')[1])
    f.close()
def multiplepols(pols):
    for i in pols:
        leg(i)
    f = open('/home/miriamwaldvogel/209politics/projects/legislativetracker/js/member.js', 'r')
    g = f.read()
    f.close()
    f = open('/home/miriamwaldvogel/209politics/projects/legislativetracker/js/member.js', 'w')
    f.write("var para = %s;\n" % filter)
    f.write("window.onscroll"+g.split("window.onscroll", 1)[1])
    f.close()
multiplepols(list(people.keys()))
