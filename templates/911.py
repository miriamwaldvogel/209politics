import csv
from os import system
f = open('/home/miriamwaldvogel/209politics/projects/crimemaps/data/stockton.csv', 'r')
r = csv.reader(f)
next(r)
s = ''
filter = []
types = {
"Vehicle/traffic": ["Traffic fatality", "Stolen vehicle arrest", "Vehicle pursuit arrest", "Traffic pursuit", "Pursuit arrest", "Carjacking", "Hit and run", "Vehicle pursuit", "Traffic injury", "Auto theft arrest"],
"Homicide": ["Homicide"],
"Theft/robbery": ["Robbery", "Attempted robbery", "Strong-arm robbery", "Armed robbery", "Auto burglaries", "Robbery arrest"],
"Residential": ["Residential robbery", "Home invasion", "Burglary", "Home invasion robbery", "Burglary"],
"Assault": ["Person stabbed", "Assault with a deadly weapon", "Felony assault", "Disturbance"],
"Arrest": ["Resisting arrest", "Battery on an officer", "Assault on an officer"],
"Arson": ["Arson", "Arson arrest"],
"Shooting/weapons": ["Shooting into a dwelling", "Person shot", "Weapon arrest", "Shooting into a vehicle", "Shooting into a building", "People shot", "Negligent discharge of a firearm", "Residence struck by gunfire", "Vehicle struck by gunfire", "Shooting into dwellings", "Brandishing"],
"Officer shooting": ["Officer shooting"],
"Kidnapping": ["Kidnapping", "Kidnapping arrest"],
"Mental health call": ["Mental health call"],
"Other": ["Attempted murder arrest", "Attempted murder", "Suspicious package", "Laser strike arrest", "Criminal threats arrest", "Explosive materials arrest", "Warrant service", "Attempted homicide arrest"],
"Vandalism": ["Vandalism arrest", "Vandalism"],
"Train": ["Train", "Train vs. pedestrian"],
"Drowning": ["Drowning"]
}
reversetypes = {}
for i in types:
    for j in types[i]:
        reversetypes[j] = i
allused = True
unmarked = []
coords = []
for i in r:
    if " " in str(i[4]):
        a = str(i[4]).split(", ")
    else:
        a = str(i[4]).split(",")
    if i[0] in reversetypes:
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
    elif i[0] not in unmarked:
        unmarked.append(i[0])
        allused = False
    if i[4] not in coords:
        coords.append(i[4])
    else:
        print(i[4])
for i in unmarked:
    print(i)
if allused:
    for i in sorted(types):
        s += """<div class="filterbox">
    <input type="checkbox" id="%s" class="checkbox" onchange="filter('%s');" checked="true">
    <div class="filtericoncontainer">
<img src="images/%s.png" alt="%s" class="filtericon">
</div>
    <label for="%s" class="filter">%s</label>
    </div>"""%(i.replace(" ", "-"), i, i.replace(" ", "-").lower().replace("/", "-"), i, i.replace(" ", "-"), i)
    s += "</div>"
    f.close()
    l = '<script type="text/javascript">'
    f = open('/home/miriamwaldvogel/209politics/projects/crimemaps/data/stockton.geojson', 'w')
    f.write("var markers = %s;\n"%filter)
    f.write("var types = %s;" % types)
    f.write("var reversetypes = %s;" % reversetypes)
    f.close()
    f = open('/home/miriamwaldvogel/209politics/projects/crimemaps/stockton.html', 'r')
    l = '<p id="unselect" onclick="unselectall();">Unselect all</p>'
    g = f.read().split(l)
    f.close()
    f = open('/home/miriamwaldvogel/209politics/projects/crimemaps/stockton.html', 'w')
    f.write(g[0]+l+s)
    l = '<input type="reset"'
    f.write(l+g[1].split(l, 1)[1])
    f.close()
    system('aws s3 sync /home/miriamwaldvogel/209politics/ s3://209politics.com --exclude "/home/miriamwaldvogel/209politics/.git/*" --exclude "/home/miriamwaldvogel/209politics/templates/*" --exclude "/home/miriamwaldvogel/209politics/opinion/*" --exclude "/home/miriamwaldvogel/209politics/projects/legislativetracker/*";')
