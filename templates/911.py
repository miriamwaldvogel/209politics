import csv
f = open('/home/miriamwaldvogel/209politics/projects/crimemaps/data/stockton.csv', 'r')
r = csv.reader(f)
next(r)
s = ''
for i in r:
    s += """L.marker([%s]).bindPopup("<p class='popuptitle'>%s</p><p class='info'>%s at %s - %s</p><p class='details' onclick='show(event);'>Details</p><p class='desc' style='display: none;'>%s</p><p class='hide' style='display: none;' onclick='hide(event);'>Hide</p>").addTo(markers);\n"""%(i[4], i[0], i[1], i[2].lower(), i[3], i[5])
f.close()
l = "var markers = L.layerGroup();"
f = open('/home/miriamwaldvogel/209politics/projects/crimemaps/stockton.html', 'r')
g = f.read().split(l, 1)
f.close()
f = open('/home/miriamwaldvogel/209politics/projects/crimemaps/stockton.html', 'w')
f.write(g[0]+l+"\n"+s+"var map"+g[1].split("var map", 1)[1])
f.close()
