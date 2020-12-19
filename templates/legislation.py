import csv
f = open('/home/miriamwaldvogel/209politics/projects/legislativetracker/data/harder-leg.csv', 'r')
r = csv.reader(f)
header = next(r)
p = ''
filter = {'role':{
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
}}
k = list(filter['status'].keys())
sl = 9
tl = len(header)
for j, i in enumerate(r):
    s = ''
    legstatus = i[tl-1:tl-sl-1:-1].index('TRUE')
    filter['status'][k[legstatus]].append(j)
    if tl-sl-6 < legstatus < tl-sl:
        for l in range(tl-sl-1, tl-sl-6, -1):
            if l == legstatus:
                s = ('<p class="status current">%s</p>\n' % header[tl-1-l])
            else:
                s = ('<p class="status">%s</p>\n' % header[tl-1-l])
    else:
        if legstatus == 0:
            s = """<p class="status">Introduced</p>
                    <p class="status">Passed House</p>
                    <p class="status current">Failed Senate</p>"""
        elif legstatus == 1:
            s = """<p class="status current">Introduced</p>
                    <p class="status current">Failed House</p>"""
        elif legstatus == 2:
            s = """<p class="status current">Introduced</p>
                    <p class="status">Passed House</p>
                    <p class="status">Passed Senate</p>
                    <p class="status">To President</p>
                    <p class="status current">Vetoed</p>"""
        else:
            s = """<p class="status current">Introduced</p>
                    <p class="status">Passed House</p>
                    <p class="status">Passed Senate</p>
                    <p class="status">Resolving Differences</p>
                    <p class="status">To President</p>
                    <p class="status">Became Law</p>"""

    if "Harder" in i[5]:
        filter['role']['sponsor'].append(j)
    else:
        filter['role']['cosponsor'].append(j)
    p += """
    <div class="leg show">
        <p class="name"><a href="/projects/legislativetracker/%s/%s.html" class="leglink">%s - %s</a></p>
        <p class="desc">%s</p>
        <p class="date">Introduced: %s</p>
        <p class="sponsor">Sponsor: %s | <a href="%s" class="cosponsorlink" target="_blank">view cosponsors</a></p>
        <p class="com">Committees: %s</p>
        <p class="action">Latest action: %s</p>
        <div class="statuscontainer">
            <p class="statustitle">Status: </p>
            %s
        </div>
    </div>""" % (i[1].lower(), i[0].replace('.', '', 2).lower().replace(' ', '-', 1), i[1], i[0], i[2], i[3], i[4], i[5], i[6], i[7], s)
f.close()
f = open('/home/miriamwaldvogel/209politics/projects/legislativetracker/people/josh-harder.html', 'r')
g = f.read().split('<div id="legislation">')
f.close()
f = open('/home/miriamwaldvogel/209politics/projects/legislativetracker/people/josh-harder.html', 'w')
f.write(g[0]+'<div id="legislation">')
f.write(s)
f.write('</div>\n</div>'+'<div id="footer">'+g[1].split('<div id="footer">')[1])
f.close()
f = open('/home/miriamwaldvogel/209politics/projects/legislativetracker/js/member.js', 'r')
g = f.read()
f.close()
f = open('/home/miriamwaldvogel/209politics/projects/legislativetracker/js/member.js', 'w')
f.write("var para = %s;\n" % filter)
f.write("window.onscroll"+g.split("window.onscroll", 1)[1])
f.close()
