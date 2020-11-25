from os import system
a = ["contact", "covid-19", "elections", "latest", "opinion", "policy"]
b = [0, 1, 0, 1, 0, 0]
s = 'aws s3 sync /home/miriamwaldvogel/209politics/ s3://209politics.com --exclude "/home/miriamwaldvogel/209politics/.git/*" --exclude "/home/miriamwaldvogel/209politics/templates/*" --exclude "/home/miriamwaldvogel/209politics/opinion/*";'
for i, j in enumerate(b):
    if j == 1:
        s+='aws s3 cp /home/miriamwaldvogel/209politics/%s1.html s3://209politics.com/%s;' % (a[i], a[i])
system(s)
