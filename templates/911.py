import csv
f = open('/home/miriamwaldvogel/209politics/projects/crimemaps/data/stockton.csv', 'r')
r = csv.reader(f)
next(r)
s = ''
filter = []
types = {
"Vehicle/traffic": ["Traffic fatality", "Stolen vehicle arrest", "Vehicle pursuit arrest", "Traffic pursuit"],
"Homicide": ["Homicide"],
"Theft/robbery": ["Robbery", "Carjacking", "Attempted robbery", "Strong-arm robbery"],
"Assault": ["Person shot", "Person stabbed", "Assault with a deadly weapon", "Felony assault"],
"Weapon": ["Weapon arrest"],
"Other": ["Resisting arrest"]
}
alltypes = []
for i in types:
    alltypes += types[i]
allused = True
for i in r:
    if " " in str(i[4]):
        a = str(i[4]).split(", ")
    else:
        a = str(i[4]).split(",")
    filter.append({
      "type": "Feature",
      "properties": {
          "type": i[0],
          "date": i[1],
          "time": i[2].lower(),
          "location": i[3],
          "desc": i[5],
          "appear": 1
      },
      "geometry": {
          "type": "Point",
          "coordinates": [float(a[1]), float(a[0])]
      }
    })
    if i[0] not in alltypes:
        print(i[0])
        allused = False
if allused:
    for i in types:
        s += """<div class="filterbox">
    <input type="checkbox" id="%s" class="checkbox" onchange="filter('%s');" checked="true">
    <label for="%s" class="filter">%s</label>
    </div>"""%(i.replace(" ", "-"), i, i.replace(" ", "-"), i)
    f.close()
    l = '<script type="text/javascript">'
    f = open('/home/miriamwaldvogel/209politics/projects/crimemaps/data/stockton.geojson', 'w')
    f.write("var markers = %s;\n"%filter)
    f.write("var types = %s;" % types)
    f.close()
    f = open('/home/miriamwaldvogel/209politics/projects/crimemaps/stockton.html', 'r')
    l = '<p class="filtertitle">Type</p>'
    g = f.read().split(l)
    f.close()
    f = open('/home/miriamwaldvogel/209politics/projects/crimemaps/stockton.html', 'w')
    f.write(g[0]+l+s+"""\n</div>
    </div>""")
    f.write('<div id="footer">'+g[1].split('<div id="footer">')[1])
    f.close()
