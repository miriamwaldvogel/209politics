from tkinter import Tk, IntVar, Checkbutton, Button
from os import system
w = Tk()
contact = IntVar()
covid = IntVar()
elections = IntVar()
latest = IntVar()
opinion = IntVar()
policy = IntVar()
insta = IntVar()
int = IntVar()
def aws():
    global w
    w.destroy()
    a = ["contact", "covid-19", "elections", "latest", "opinion", "policy", "instagram", "interactives"]
    b = [contact.get(), covid.get(), elections.get(), latest.get(), opinion.get(), policy.get(), insta.get(), int.get()]
    s = 'aws s3 sync /home/miriamwaldvogel/209politics/ s3://209politics.com --exclude "/home/miriamwaldvogel/209politics/.git/*" --exclude "/home/miriamwaldvogel/209politics/templates/*" --exclude "/home/miriamwaldvogel/209politics/opinion/*";'
    for i, j in enumerate(b):
        if j == 1:
            s+='aws s3 cp /home/miriamwaldvogel/209politics/%s1.html s3://209politics.com/%s;' % (a[i], a[i])
    system(s)
Checkbutton(w, text="Contact", variable=contact).pack()
Checkbutton(w, text="COVID", variable=covid).pack()
Checkbutton(w, text="Elections", variable=elections).pack()
Checkbutton(w, text="Instagram", variable=insta).pack()
Checkbutton(w, text="Interactives", variable=int).pack()
Checkbutton(w, text="Latest", variable=latest).pack()
Checkbutton(w, text="Opinion", variable=opinion).pack()
Checkbutton(w, text="Policy", variable=policy).pack()
Button(w, text="Submit", command=aws).pack()
w.mainloop()
