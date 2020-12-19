import csv
f = open('/home/miriamwaldvogel/209politics/projects/legislativetracker/data/harder-leg.csv', 'r')
r = csv.reader(f)
next(r, None)
s = ''
filter = {'role':{
'sponsor': [],
'cosponsor': []
}, 'status':{
'intro': [],
'house': [],
'senate': [],
'topres': [],
'law': [],
'resdif': [],
'veto': []
}}
for j, i in enumerate(r):
    a = ['', '', '', '', '']
    legstatus = i[8:].index('TRUE')
    a[legstatus] = " current"
    filter['status'][list(filter['status'].keys())[legstatus]].append(j)
    s += """
    <div class="leg show">
        <p class="name"><a href="/projects/legislativetracker/%s/%s.html" class="leglink">%s - %s</a></p>
        <p class="desc">%s</p>
        <p class="date">Introduced: %s</p>
        <p class="sponsor">Sponsor: %s | <a href="%s" class="cosponsorlink" target="_blank">view cosponsors</a></p>
        <p class="com">Committees: %s</p>
        <p class="action">Latest action: %s</p>
        <div class="statuscontainer">
            <p class="statustitle">Status: </p>
            <p class="status%s">Introduced</p>
            <p class="status%s">Passed House</p>
            <p class="status%s">Passed Senate</p>
            <p class="status%s">To President</p>
            <p class="status%s">Became Law</p>
        </div>
    </div>""" % (i[1].lower(), i[0].replace('.', '', 2).lower().replace(' ', '-', 1), i[1], i[0], i[2], i[3], i[4], i[5], i[6], i[7], a[0], a[1], a[2], a[3], a[4])
    if "Harder" in i[4]:
        filter['role']['sponsor'].append(j)
    else:
        filter['role']['cosponsor'].append(j)
f.close()
f = open('/home/miriamwaldvogel/209politics/projects/legislativetracker/people/josh-harder.html', 'r')
g = f.read().split('<div id="legislation">')
f.close()
f = open('/home/miriamwaldvogel/209politics/projects/legislativetracker/people/josh-harder.html', 'w')
f.write(g[0]+'<div id="legislation">')
f.write(s)
h = g[1].split('<div id="footer">')[1].split('<script type="text/javascript">', 1)
f.write('</div>\n</div>'+'<div id="footer">'+h[0]+'<script type="text/javascript">\n'+'var para = %s' % filter+h[1])
f.close()
