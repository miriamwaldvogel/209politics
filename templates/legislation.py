import csv
f = open('/home/miriamwaldvogel/209politics/projects/legislationtracker/data/harder-leg.csv', 'r')
r = csv.reader(f)
next(r, None)
s = ''
for i in r:
    a = ['', '', '', '', '']
    a[i[7:].index('TRUE')] = " current"
    s += """
    <div class="leg">
        <p class="name"><a href="/projects/legislationtracker/%s/%s.html" class="leglink">%s - %s</a></p>
        <p class="desc">%s</p>
        <p class="date">Introduced: %s</p>
        <p class="sponsor">Sponsor: %s | <a href="%s" class="cosponsorlink" target="_blank">view cosponsors</a></p>
        <p class="com">Committees: %s</p>
        <div class="statuscontainer">
            <p class="statustitle">Status: </p>
            <p class="status%s">Introduced</p>
            <p class="status%s">Passed House</p>
            <p class="status%s">Passed Senate</p>
            <p class="status%s">To President</p>
            <p class="status%s">Became Law</p>
        </div>
    </div>
""" % (i[1].lower(), i[0].replace('.', '', 2).lower().replace(' ', '-', 1), i[1], i[0], i[2], i[3], i[4], i[5], i[6], a[0], a[1], a[2], a[3], a[4])
f.close()
f = open('/home/miriamwaldvogel/209politics/projects/legislationtracker/people/josh-harder.html', 'r')
g = f.read().split('<div id="legislation">')
f.close()
f = open('/home/miriamwaldvogel/209politics/projects/legislationtracker/people/josh-harder.html', 'w')
f.write(g[0]+'<div id="legislation">')
f.write(s)
f.write(g[1])
f.close()
