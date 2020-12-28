import csv
from tkinter import Tk, Checkbutton, IntVar, Button, Label
w = Tk()
polvars = [IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar()]
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
def leg(pol):
    global filter
    f = open('/home/miriamwaldvogel/209politics/projects/legislativetracker/data/%s-leg.csv'%pol, 'r')
    filter[pol] = {'role':{
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
        s = ''
        legstatus = i.index('TRUE')
        if header[legstatus] in filter[pol]['status']:
            filter[pol]['status'][header[legstatus]].append(j)
        else:
            filter[pol]['status'][header[legstatus]] = [j]
        if legstatus % 2 == 1:
            for k, l in enumerate(header[o:]):
                if k+o == legstatus:
                    s+=('<p class="status current">%s</p>'%l)
                elif k % 2 == 0 and k != 2 and k != 6:
                    s+=('<p class="status">%s</p>'%l)
        else:
            for k, l in enumerate(header[o:]):
                if k+o == legstatus:
                    s+=('<p class="status current">%s</p>'%l)
                    if k != 9:
                        break
                elif k % 2 == 0 and k != 2 and k != 6:
                    s+=('<p class="status">%s</p>'%l)
        p += """
        <div class="leg show">
            <p class="name"><a href="/projects/legislativetracker/%s/%s.html" class="leglink">%s - %s</a></p>
            <p class="desc">%s</p>
            <p class="are">Policy Area: %s</p>
            <p class="date">Introduced: %s</p>
            <p class="sponsor">Sponsor: %s | <a href="%s" class="cosponsorlink" target="_blank">view cosponsors</a></p>
            <p class="com">Committees: %s</p>
            <p class="action">Latest action: %s</p>
            <div class="statuscontainer">
                <p class="statustitle">Status: </p>
                %s
            </div>
        </div>""" % (people[pol][2], i[0].replace('.', '', 2).lower().replace(' ', '-', 1), i[1], i[0], i[2], i[3], i[4], i[5], i[6], i[7], i[8], s)
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
    g = f.read().split('<p class="filtertitle">Status - legislation</p>', 1)
    f.close()
    f = open('/home/miriamwaldvogel/209politics/projects/legislativetracker/people/%s.html' % people[pol][0], 'w')
    f.write(g[0]+'<p class="filtertitle">Status - legislation</p>\n'+statusfilters)
    f.write("""</div>
    <div class="filters">
    <p class="filtertitle">Policy Area</p>"""+areafilters)
    f.write("""</div>
        <input type="reset" id="datereset" value="Reset all" onclick="showall();">
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
def multiplepols():
    pols = [polkeys[i] for i, j in enumerate(polvars) if j.get() == 1]
    global w
    w.destroy()
    for i in pols:
        leg(i)
    f = open('/home/miriamwaldvogel/209politics/projects/legislativetracker/js/member.js', 'r')
    g = f.read()
    f.close()
    f = open('/home/miriamwaldvogel/209politics/projects/legislativetracker/js/member.js', 'w')
    f.write("var para = %s;\n" % filter)
    f.write("window.onscroll"+g.split("window.onscroll", 1)[1])
    f.close()
Label(w, text="Legislation").pack()
polkeys = list(people.keys())
for i, j in enumerate(polvars):
    Checkbutton(w, text=people[polkeys[i]][1], variable=polvars[i]).pack()
Button(w, text="Submit", command=multiplepols).pack()
w.mainloop()
