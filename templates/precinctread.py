import csv
f = open('/home/miriamwaldvogel/209politics/raw/general-election-2020/stockton-mayor/precincts.csv', 'r')
r = csv.reader(f)
a = 0
b = 0
for i in r:
    if len(i[0]) == 5:
        a += int(i[4].replace(",", ""))
        b += int(i[5].replace(",", ""))
        if int(i[4].replace(",", "")) > int(i[5].replace(",", "")):
            print(i[0])
        #g.write('"%s": [%d, %d],\n' % (i[0], int(i[4].replace(",", "")), int(i[5].replace(",", ""))))
f.close()
print(a, b)
