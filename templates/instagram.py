from datetime import datetime
from tkinter import Tk, Entry, Label, Button
from os import system
n = datetime.now()
d = [n.strftime("%Y"), n.strftime("%m"), n.strftime("%d")]
w = Tk()
img = Entry(w)
alt = Entry(w)
htmlname = Entry(w)
def instagram():
    f = open('/home/miriamwaldvogel/209politics/instagram1.html', 'r')
    g = f.read().split('<div id="photoscontainer">')
    f.close()
    f = open('/home/miriamwaldvogel/209politics/instagram1.html', 'w')
    f.write(g[0]+'<div id="photoscontainer">')
    f.write('<div class="photocontainer"><a href="/%s/%s/%s/%s.html"><img src="%s" alt="%s" class="photo"></a></div>' % (d[0], d[1], d[2], htmlname.get(), img.get(), alt.get()))
    f.write(g[1])
    f.close()
    global w
    w.destroy()
    system('aws s3 sync /home/miriamwaldvogel/209politics/ s3://209politics.com --exclude "/home/miriamwaldvogel/209politics/.git/*" --exclude "/home/miriamwaldvogel/209politics/templates/*" --exclude "/home/miriamwaldvogel/209politics/opinion/*"; aws s3 cp /home/miriamwaldvogel/209politics/instagram1.html s3://209politics.com/instagram')

Label(w, text="HTML name").pack()
htmlname.pack()
Label(w, text="Image name").pack()
img.pack()
Label(w, text="Alt").pack()
alt.pack()
Button(w, text="Submit", command=instagram).pack()
w.mainloop()
