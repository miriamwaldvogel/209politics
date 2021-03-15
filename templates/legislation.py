# -*- coding: utf-8 -*-
from csv import reader
from re import split
statelegs = [{"Aguiar-Curry": ["D", "Winters", "Cecilia "],
"Arambula":["D", "Fresno", "Joaquin "],
"Bauer-Kahan": ["D", "Orinda", "Rebecca "],
"Bennett":["D", "Santa Barbara", "Steve "],
"Berman":["D", "Menlo Park", "Marc "],
"Bigelow":["R", "Madera", "Frank "],
"Bloom": ["D", "Santa Monica", "Richard "],
"Boerner Horvath":["D", "Oceanside", "Tasha "],
"Bonta": ["D", "Oakland", "Rob "],
"Burke":["D", "Inglewood", "Autumn "],
"Calderon":["D", "Norwalk", "Lisa "],
"Carrillo":["D", "Los Angeles", "Wendy "],
"Cervantes":["D", "Corona", "Sabrina "],
"Chau":["D", "Monterey Park", "Ed "],
"Chen":["R", "Brea", "Phillip "],
"Chiu":["D", "San Francisco", "David "],
"Choi":["R", "Irvine", "Steven "],
"Cooley":["D", "Rancho Cordova", "Ken "],
"Cooper": ["D", "Elk Grove", "Jim "],
"Cunningham":["R", "San Luis Obispo", "Jordan "],
"Megan Dahle":["R", "Redding", ""],
"Daly":["D", "Anaheim", "Tom "],
"Davies":["R", "Laguna Niguel", "Laurie "],
"Flora": ["R", "Modesto", "Heath "],
"Fong":["R", "Bakersfield", "Vince "],
"Frazier":["D", "Fairfield", "Jim "],
"Friedman":["D", "Glendale", "Laura "],
"Gabriel":["D", "Woodland Hills", "Jesse "],
"Gallagher":["R", "Yuba City", "James "],
"Cristina Garcia": ["D", "Bell Gardens", ""],
"Eduardo Garcia": ["D", "Coachella", ""],
"Gipson":["D", "Carson", "Mike "],
"Lorena Gonzalez":["D", "San Diego", ""],
"Gray":["D", "Merced", "Adam "],
"Grayson":["D", "Concord", "Timothy "],
"Holden":["D", "Pasadena", "Chris "],
"Irwin":["D", "Thousand Oaks", "Jacqui "],
"Jones-Sawyer":["D", "South Los Angeles", "Reginald Byron "],
"Kalra":["D", "San Jose", "Ash "],
"Kamlager":["D", "Culver City", "Sydney "],
"Kiley":["R", "Roseville", "Kevin "],
"Lackey":["R", "Palmdale", "Tom "],
"Lee":["D", "Milpitas", "Alex "],
"Levine":["D", "Petaluma", "Marc "],
"Low": ["D", "Silicon Valley", "Evan "],
"Maienschein":["D", "Poway", "Brian "],
"Mathis":["R", "Visalia", "Devon "],
"Mayes": ["I", "Palm Springs", "Chads "],
"McCarty":["D", "Sacramento", "Kevin "],
"Medina":["D", "Riverside", "Jose "],
"Mullin":["D", "San Mateo", "Kevin "],
"Muratsuchi": ["D", "Torrance", "Al "],
"Nazarian":["D", "Van Nuys", "Adrin "],
"Nguyen":["R", "Garden Grove", "Janet "],
"O'Donnell":["D", "Long Beach", "Patrick "],
"Patterson":["R", "Clovis", "Jim "],
"Petrie-Norris": ["D", "Laguna Beach", "Cottie "],
"Quirk": ["D", "Hayward", "Bill "],
"Quirk-Silva": ["D", "Fullerton", "Sharon "],
"Ramos":["D", "Highland", "James "],
"Rendon":["D", "Lakewood", "Anthony "],
"Reyes": ["D", "San Bernardino", "Eloise "],
"Luz Rivas":["D", "Arleta", ""],
"Robert Rivas": ["D", "Hollister", ""],
"Rodriguez":["D", "Pomona", "Freddie "],
"Blanca Rubio": ["D", "Baldwin Park", ""],
"Salas":["D", "Hanford", "Rudy "],
"Santiago": ["D", "Los Angeles", "Miguel "],
"Seyarto":["R", "Murrieta", "Kelley "],
"Smith":["R", "Victorville", "Thurston "],
"Stone": ["D", "Monterey", "Mark "],
"Ting":["D", "San Francisco", "Phillip "],
"Valladares":["R", "Santa Clarita", "Suzette Martinez "],
"Villapudua": ["D", "Stockton", "Carlos "],
"Voepel":["R", "El Cajon", "Randy "],
"Waldron":["R", "Escondido", "Marie "],
"Ward":["D", "San Diego", "Christopher "],
"Weber": ["D", "San Diego", "Shirley "],
"Wicks": ["D", "Berkeley", "Buffy "],
"Wood": ["D", "Santa Rosa", "Jim "]
},
{
"Allen":["D", "Santa Monica", "Benjamin "],
"Archuleta":["D", "Pico Rivera", "Bob "],
"Atkins":["D", "San Diego", "Toni "],
"Bates": ["R", "Laguna Niguel", "Patricia "],
"Becker":["D", "San Mateo", "Josh "],
"Borgeas": ["R", "Fresno", "Andreas "],
"Bradford":["D", "Gardena", "Steven "],
"Caballero": ["D", "Merced", "Anna "],
"Cortese":["D", "San Jose", "Dave "],
"Dahle":["R", "Redding", "Brian "],
"Dodd":["D", "Napa", "Bill "],
"Durazo":["D", "Los Angeles", "Maria Elena "],
"Eggman": ["D", "Stockton", "Susan Talamantes "],
"Glazer":["D", "Antioch", "Steven "],
"Gonzalez":["D", "Long Beach", "Lena "],
"Grove":["R", "Bakersfield", "Shannon "],
"Hertzberg":["D", "Van Nuys", "Robert "],
"Hueso":["D", "Chula Vista", "Ben "],
"Hurtado":["D", "Sanger", "Melissa "],
"Jones":["R", "Santee", "Brian "],
"Laird":["D", "San Luis Obispo", "John "],
"Leyva":["D", "Chino", "Connie "],
"Limón":["D", "Santa Barbara", "Monique "],
"McGuire": ["D", "Santa Rosa", "Mike "],
"Melendez":["R", "Lake Elsinore", "Melissa "],
"Min":["D", "Irvine", "Dave "],
"Newman":["D", "Fullerton", "Josh "],
"Nielsen":["R", "Tehama", "Jim "],
"Ochoa Bogh":["R", "Rancho Cucamonga", "Rosilicie "],
"Pan":["D", "Sacramento", "Richard "],
"Portantino":["D", "La Cañada Flintridge", "Anthony "],
"Roth":["D", "Riverside", "Richard "],
"Rubio":["D", "Baldwin Park", "Susan "],
"Skinner":["D", "Berkeley", "Nancy "],
"Stern":["D", "Thousand Oaks", "Henry "],
"Umberg":["D", "Anaheim", "Thomas "],
"Wieckowski":["D", "Fremont", "Bob "],
"Wiener": ["D", "San Francisco", "Scott "],
"Wilk":["R", "Lancaster", "Scott "],
}]
statelegs[0]["""O\xe2\x80\x99Donnell"""] = statelegs[0]["O'Donnell"]
people = {'mcnerney': ['jerry-mcnerney', 'McNerney', 'congress'],
'harder': ['josh-harder', 'Harder', 'congress'],
'eggman': ['susan-talamantes-eggman', 'Eggman', 'legislature'],
'cooper': ['jim-cooper', 'Cooper', 'legislature'],
'villapudua': ['carlos-villapudua', 'Villapudua', 'legislature'],
'flora': ['heath-flora', 'Flora', 'legislature']
}
filter = {}
statusstart = 9
def filteradd(p, k, a, j):
    global filter
    if a not in filter[p][k]:
        filter[p][k][a] = [j]
    else:
        filter[p][k][a].append(j)
def makefilters(p, a, n):
    s = """<div class="filters">
<p class="filtertitle">%s</p>"""%n
    for i in sorted(filter[p][a]):
        s += """\n<div class="filterbox">
<input type="checkbox" id="%s" class="checkbox" onchange="filter('%s', '%s', '%s');" checked="true">
<label for="%s" class="filter">%s</label>
</div>"""%(i.replace(" ", "-"), p, i, a, i.replace(" ", "-"), i)
    s += '\n</div>\n'
    return(s)
def legislation(pol):
    global filter
    f = open("/home/miriamwaldvogel/209politics/projects/legislativetracker/data/%s-leg.csv"%pol, "r")
    r = reader(f)
    filter[pol] = {'type': {}, 'status':{}, 'area':{}, 'committees':{}, 'date':[]}
    legblocks = ""
    for j, i in enumerate(r):
        legname = i[0].replace('.', '').lower().replace(' ', '-')
        legf = open("/home/miriamwaldvogel/209politics/projects/legislativetracker/data/%s/%s.csv"%(pol, legname), "r")
        legr = reader(legf)
        header = legr.next()
        leginfo = legr.next()
        if pol != "harder" and pol != "mcnerney":
            collabhtml = ""
            role = legr.next()
            collabs = legr.next()
            for k in range(3):
                if collabs[k] != "":
                    collabhtml += "<p>%s: "%role[k]
                    for m in split(", | and |and ", collabs[k]):
                        if m != "":
                            if "Senator" in m:
                                if "Senators" in m:
                                    collabhtml += "Sens. "
                                else:
                                    collabhtml += "Sen. "
                                statehouse = 1
                                lastname = m.split(" ", 1)[1]
                                memberinfo = statelegs[statehouse][lastname]
                                collabhtml += ("%s%s (%s-%s), "%(memberinfo[2], lastname, memberinfo[0], memberinfo[1]))
                            elif "Assembly" in m:
                                if "Members" in m:
                                    collabhtml += "Asms. "
                                else:
                                    collabhtml += "Asm. "
                                statehouse = 0
                                lastname = m.split(" ", 2)[2]
                                memberinfo = statelegs[statehouse][lastname]
                                collabhtml += ("%s%s (%s-%s), "%(memberinfo[2], lastname, memberinfo[0], memberinfo[1]))
                            else:
                                memberinfo = statelegs[statehouse][m]
                                collabhtml += ("%s%s (%s-%s), "%(memberinfo[2], m, memberinfo[0], memberinfo[1]))
                    collabhtml = collabhtml[:len(collabhtml)-2]+"</p>\n"
        actionlist = []
        desc = ""
        legr.next()
        for k in legr:
            if k[0] != "":
                actionlist.append('<p class="action">%s - %s</p>'%(k[0], k[1]))
                lastdate = k[0]
                lastaction = k[1]
            if k[2] != "":
                desc += '<p class="legdesc">%s</p>'%k[2]
        actions = ''
        for k in actionlist[::-1]:
            actions += k
        legf.close()
        filter[pol]['date'].append(leginfo[4])
        filteradd(pol, 'area', leginfo[3], j)
        filteradd(pol, 'type', leginfo[1], j)
        for k in leginfo[7].split("/"):
            filteradd(pol, 'committees', k, j)
        legstatus = leginfo.index('TRUE')
        status = ""
        if header[legstatus] in filter[pol]['status']:
            filter[pol]['status'][header[legstatus]].append(j)
        else:
            filter[pol]['status'][header[legstatus]] = [j]
        if legstatus % 2 == 1:
            for k, l in enumerate(header[statusstart:]):
                if leginfo[k+statusstart] == "":
                    break
                if k+statusstart == legstatus:
                    status+=('<p class="status current">%s</p>'%l)
                elif k % 2 == 0 and k != 2 and k != 6 and k != 12:
                    status+=('<p class="status">%s</p>'%l)
        else:
            for k, l in enumerate(header[statusstart:]):
                if leginfo[k+statusstart] == "":
                    break
                if k+statusstart == legstatus:
                    status+=('<p class="status current">%s</p>'%l)
                    if k != 9:
                        break
                elif k % 2 == 0 and k != 2 and k != 6 and k != 12:
                    status+=('<p class="status">%s</p>'%l)
        legdesc = ["""<p class="area">Policy Area: %s</p>
        <p class="date">Introduced: %s</p>
        <div id="sponsors">"""%(leginfo[3], leginfo[4]),
        """<p class="com">Committees: %s</p>
        <p id="action">Latest action: %s - %s</p>
        <div class="statuscontainer">
            <p class="statustitle">Status: </p>
            %s
        </div>"""%(leginfo[7], lastdate, lastaction, status)]
        legblocks += """
        <div class="leg show">
            <p class="name"><a href="/projects/legislativetracker/%s/%s.html" class="leglink">%s - %s</a></p>
        """ %(people[pol][2], legname, leginfo[1], leginfo[0])
        if pol == "harder" or pol == "mcnerney":
            legblocks += legdesc[0]+('<p class="sponsors">Sponsor: %s | <a target="_blank" href="%s">view cosponsors</a></p></div>'%(leginfo[5], leginfo[6]))+legdesc[1]+"</div>"
            legdesc[0] += '<p id="sponsors">Sponsor: %s | <a target="_blank" href="%s">view cosponsors</a></p></div>'%(leginfo[5], leginfo[6])
        else:
            legblocks += legdesc[0]+('<p class="sponsors">Sponsor: %s | <a target="_blank" href="/projects/legislativetracker/%s/%s.html">view cosponsors</a></p>'%(leginfo[5], people[pol][2], legname))+legdesc[1]+"</div></div>"
            legdesc[0] += collabhtml+'</div><p id="togglesponsors" onclick="sponsortoggle();"></p>'
        leghtml = open("/home/miriamwaldvogel/209politics/projects/legislativetracker/%s/%s.html"%(people[pol][2], legname), "w")
        leghtml.write("""<!DOCTYPE html>
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
              <div id="backbutton"><a href="/projects/legislativetracker/people/%s.html" id="backurl">BACK</a></div>
              <h1 id="title">%s</h1>
              <p id="legtext"><b>%s</b> - %s</p>
            </div>
            <div id="firstleginfo">
                %s
              """%(leginfo[0], people[pol][0], leginfo[0], leginfo[1], leginfo[2], legdesc[0]))
        leghtml.write(legdesc[1])
        leghtml.write("""<div id="fulllinkcontainer">
            <a href="%s" target="_blank" id="fulllink">View legislation text</a>
        </div>
      </div>
      <div id="legdesc">
        %s
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
  </html>"""%(leginfo[8], desc, actions))
        leghtml.close()
    f.close()
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
        <p id="legtitle">Sponsored legislation</p>
        <div id="legislation">"""+legblocks)
    f.write('</div>\n</div>'+'<div id="footer">'+g[1].split('<div id="footer">')[1])
    f.close()

legislation("mcnerney")
legislation("harder")
f = open('/home/miriamwaldvogel/209politics/projects/legislativetracker/js/member.js', 'r')
g = f.read()
f.close()
f = open('/home/miriamwaldvogel/209politics/projects/legislativetracker/js/member.js', 'w')
f.write("var para = %s;\n" % filter)
f.write("window.onscroll"+g.split("window.onscroll", 1)[1])
f.close()
