import csv
f = open('/home/miriamwaldvogel/209politics/projects/crimemaps/data/stockton.csv', 'r')
r = csv.reader(f)
next(r)
s = ''
filter = []
types = {
"Vehicle/traffic": ["Traffic fatality", "Stolen vehicle arrest", "Vehicle pursuit arrest", "Traffic pursuit", "Pursuit arrest"],
"Homicide": ["Homicide"],
"Theft/robbery": ["Robbery", "Carjacking", "Attempted robbery", "Strong-arm robbery", "Armed robbery"],
"Residential robbery": ["Residential robbery"],
"Assault": ["Person stabbed", "Assault with a deadly weapon", "Felony assault"],
"Arrest": ["Resisting arrest", "Battery on an officer", "Assault on an officer"],
"Arson": ["Arson"],
"Shooting/weapons": ["Shooting into a dwelling", "Person shot", "Weapon arrest"],
"Officer shooting": ["Officer shooting"],
"Kidnapping": ["Kidnapping", "Kidnapping arrest"],
"Other": ["Attempted murder arrest", "Attempted murder"],
}
reversetypes = {}
for i in types:
    for j in types[i]:
        reversetypes[j] = i
allused = True
unmarked = []
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
          "appear": 1,
          "icon": "images/%s.png"%reversetypes[i[0]].lower().replace(" ", "-").replace("/", "-")
      },
      "geometry": {
          "type": "Point",
          "coordinates": [float(a[1]), float(a[0])]
      }
    })
    if i[0] not in reversetypes and i[0] not in unmarked:
        unmarked.append(i[0])
        allused = False
for i in unmarked:
    print(i)
if allused:
    for i in types:
        s += """<div class="filterbox">
    <input type="checkbox" id="%s" class="checkbox" onchange="filter('%s');" checked="true">
    <label for="%s" class="filter">%s</label>
    </div>"""%(i.replace(" ", "-"), i, i.replace(" ", "-"), i)
    s += "</div>"
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
    f.write(g[0]+l+s)
    l = '<input type="reset"'
    f.write(l+g[1].split(l, 1)[1])
    f.close()
