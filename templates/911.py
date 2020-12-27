import csv
f = open('/home/miriamwaldvogel/209politics/projects/crimemaps/data/stockton.csv', 'r')
r = csv.reader(f)
next(r)
s = ''
filter = []
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
          "desc": i[5]
      },
      "geometry": {
          "type": "Point",
          "coordinates": [float(a[1]), float(a[0])]
      }
    })
f.close()
l = '<script type="text/javascript">'
f = open('/home/miriamwaldvogel/209politics/projects/crimemaps/data/stockton.js', 'w')
f.write("var markers = %s;"%filter)
f.close()
