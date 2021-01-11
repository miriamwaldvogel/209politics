import csv
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
stateleg = {"Aguiar-Curry": ["D", "Winters", "Cecilia"],
"Bloom": ["D", "Santa Monica", "Richard"],
"Bonta": ["D", "Oakland", "Rob"],
"Borgeas": ["R", "Fresno", "Andreas"],
"Caballero": ["D", "Merced", "Anna"],
"Cooper": ["D", "Elk Grove", "Jim"],
"Cristina Garcia": ["D", "Bell Gardens", ""],
"Eduardo Garcia": ["D", "Coachella", ""],
"Eggman": ["D", "Stockton", "Susan Talamantes"],
"Flora": ["R", "Manteca", "Heath"],
"Low": ["D", "Silicon Valley", "Evan"],
"Petrie-Norris": ["D", "Laguna Beach", "Cottie"],
"Quirk": ["D", "Hayward", "Bill"],
"Quirk-Silva": ["D", "Fullerton", "Sharon"],
"Reyes": ["D", "San Bernardino", "Eloise"],
"Robert Rivas": ["D", "Hollister", ""],
"Santiago": ["D", "Los Angeles", "Miguel"],
"Stone": ["D", "Monterey", "Mark"],
"Weber": ["D", "San Diego", "Shirley"],
"Villapudua": ["D", "Stockton", "Carlos"],
"Wiener": ["D", "San Francisco", "Scott"],
}
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
    global filter
    f = open('/home/miriamwaldvogel/209politics/projects/legislativetracker/data/%s-leg.csv'%pol, 'r')
    filter[pol] = {'type': {}, 'role':{
    'sponsor': [],
    'cosponsor': [],
    }, 'status':{}, 'area':{}, 'date':[]}
    r = csv.reader(f)
    header = next(r)
    o = 9
    p = ''
    for j, i in enumerate(r):
        filter[pol]['date'].append(i[4])
        if i[3] not in filter[pol]['area']:
            filter[pol]['area'][i[3]] = [j]
        else:
            filter[pol]['area'][i[3]].append(j)
        if people[pol][1] in i[5]:
            filter[pol]['role']['sponsor'].append(j)
        else:
            filter[pol]['role']['cosponsor'].append(j)
        if i[1] not in filter[pol]['type']:
            filter[pol]['type'][i[1]] = [j]
        else:
            filter[pol]['type'][i[1]].append(j)
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
        </div>""" % (people[pol][2], i[0].replace('.', '', 2).lower().replace(' ', '-', 1), people[pol][0], i[1], i[0], i[2], i[3], i[4], i[5], a, i[7], i[8], s)
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
    f.write(g[0]+'<!--Python marker-->\n'+makefilters(pol, 'status', 'Status')+makefilters(pol, 'area', 'Policy area')+makefilters(pol, 'type', 'Legislation type'))
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
