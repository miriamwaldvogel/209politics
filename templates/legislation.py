import csv
from tkinter import Tk, Checkbutton, IntVar, Button, Label
w = Tk()
polvars = [IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar()]
filter = {}
k = ['fail2', 'fail1', 'veto', 'resdif', 'law', 'topres', 'senate', 'house', 'intro']
sl = 9
tl = 18
people = {'mcnerney': ['jerry-mcnerney', 'McNerney'],
'harder': ['josh-harder', 'Harder'],
'eggman': ['susan-talamantes-eggman', 'Eggman'],
'cooper': ['jim-cooper', 'Cooper'],
'villapudua': ['carlos-villapudua', 'Villapudua'],
'flora': ['heath-flora', 'Flora']
}
def leg(pol):
    global filter
    f = open('/home/miriamwaldvogel/209politics/projects/legislativetracker/data/%s-leg.csv'%pol, 'r')
    filter[pol] = {'role':{
    'sponsor': [],
    'cosponsor': [],
    }, 'status':{
    'fail2': [],
    'fail1': [],
    'veto': [],
    'resdif': [],
    'law': [],
    'topres': [],
    'senate': [],
    'house': [],
    'intro': [],
    }, 'area':{}, 'date':[]}
    r = csv.reader(f)
    header = next(r)
    p = ''
    for j, i in enumerate(r):
        filter[pol]['date'].append(i[4])
        if i[3] not in filter[pol]['area']:
            filter[pol]['area'][i[3]] = [j]
        else:
            filter[pol]['area'][i[3]].append(j)
        s = ''
        legstatus = i[tl-1:tl-sl-1:-1].index('TRUE')
        filter[pol]['status'][k[legstatus]].append(j)
        if tl-sl-6 < legstatus < tl-sl:
            for l in range(tl-sl-1, tl-sl-6, -1):
                if l == legstatus:
                    s += ('<p class="status current">%s</p>\n' % header[tl-1-l])
                else:
                    s += ('<p class="status">%s</p>\n' % header[tl-1-l])
        else:
            if legstatus == 0:
                s = """<p class="status">Introduced</p>
    <p class="status">Passed House</p>
    <p class="status current">Failed Senate</p>"""
            elif legstatus == 1:
                s = """<p class="status">Introduced</p>
    <p class="status current">Failed House</p>"""
            elif legstatus == 2:
                s = """<p class="status">Introduced</p>
    <p class="status">Passed House</p>
    <p class="status">Passed Senate</p>
    <p class="status">To President</p>
    <p class="status current">Vetoed</p>"""
            else:
                s = """<p class="status">Introduced</p>
    <p class="status">Passed House</p>
    <p class="status">Passed Senate</p>
    <p class="status current">Resolving Differences</p>
    <p class="status">To President</p>
    <p class="status">Became Law</p>"""
        if people[pol][1] in i[5]:
            filter[pol]['role']['sponsor'].append(j)
        else:
            filter[pol]['role']['cosponsor'].append(j)
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
        </div>""" % (i[1].lower(), i[0].replace('.', '', 2).lower().replace(' ', '-', 1), i[1], i[0], i[2], i[3], i[4], i[5], i[6], i[7], i[8], s)
    f.close()
    areafilters = ''
    for i in filter[pol]['area']:
        areafilters += """<div class="filterbox">
    <input type="checkbox" id="%s" class="checkbox" onchange="filter('%s', '%s', 'area');" checked="true">
    <label for="%s" class="filter">%s</label>
    </div>\n""" % (i, pol, i, i, i)
    f = open('/home/miriamwaldvogel/209politics/projects/legislativetracker/people/%s.html' % people[pol][0], 'r')
    g = f.read().split('<p class="filtertitle">Policy Area</p>', 1)
    f.close()
    f = open('/home/miriamwaldvogel/209politics/projects/legislativetracker/people/%s.html' % people[pol][0], 'w')
    f.write(g[0]+'<p class="filtertitle">Policy Area</p>\n'+areafilters)
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
