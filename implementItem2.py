import tkinter as tk
from time import sleep
##### BUTTON HANDLER #####
def setInitToken():
    tmp = userEntry.get()
    s1.token = int(tmp)
    s1.frame.config(text=s1.name+"\n"+str(s1.token))
    print(s1.token)

def changeColor(frame, color1, color2):
    frame.config(bg=color1)
    frame.after(500, lambda: frame.config(bg=color2))

def fire(prev,next):
        if prev.token==0:
            print("No token to fire")
            changeColor(prev.frame,"red","white")
        else:
            prev.token-=1
            next.token+=1
            prev.frame.config(text=prev.name+"\n"+str(prev.token))
            next.frame.config(text=next.name+"\n"+str(next.token))

def reset(list):
    for i in list:
        i.token =0;
        i.frame.config(text=i.name+"\n"+str(i.token))


##### CLASS INIT #####
class Place:
    def __init__(self, name, token = 0):
        self.name = name
        self.token = token
    def getToken(self):
        return self.token
    def getName(self):
        return self.name
    def setToken(self, token):
        self.token = token
    def makeGUI(self,masterFrame):
            self.frame= tk.Label(master = masterFrame, text=self.name+"\n"+str(self.token),background="white", highlightbackground="black", highlightthickness=10)
    def setGrid(self,row, col):
        self.frame.grid(row=row, column=col,padx=5,pady=5, sticky="nsew")
class Trasition:
    def __init__(self,name, prev, next):
        self.name = name
        self.prev = prev
        self.next = next
    def makeGUI(self,masterFrame):
            self.frame= tk.Button(master = masterFrame, text=self.name,background="white",command=lambda: fire(self.prev,self.next),activebackground="red",relief=tk.RAISED)
    def setGrid(self,row, col):
        self.frame.grid(row=row, column=col,padx=5,pady=5, sticky="nsew")
class Arrow:
    def makeGUI(self,masterFrame):
        self.frame= tk.Frame(master=masterFrame, width=100, height=100)
    def LtoR(self):
        self.arrow= tk.Canvas(self.frame, width=100, height=100)
        self.arrow.pack()
        self.arrow.create_line(0,50,100,50,arrow=tk.LAST)
    def RtoL(self):
        self.arrow= tk.Canvas(self.frame, width=100, height=100)
        self.arrow.pack()
        self.arrow.create_line(100,50,0,50,arrow=tk.LAST)
    def TtoB(self):
        self.arrow= tk.Canvas(self.frame, width=100, height=100)
        self.arrow.pack()
        self.arrow.create_line(50,0,50,100,arrow=tk.LAST)
    def BtoT(self):
        self.arrow= tk.Canvas(self.frame, width=100, height=100)
        self.arrow.pack()
        self.arrow.create_line(50,100,50,0,arrow=tk.LAST)
    def setGrid(self,row, col):
        self.frame.grid(row=row, column=col,padx=5,pady=5, sticky="nsew")

#### INIT PETRI NET ####
s1 = Place("waiting")
s2 = Place("inside")
t1 = Trasition("start",s1,s2)
s3 = Place("done")
t2 = Trasition("change",s2,s3)


placeArray=[]
placeArray.append(s1)
placeArray.append(s2)
placeArray.append(s3)

window = tk.Tk()
window.title("Petri Net")

frame = tk.Frame(master = window, padx=5, pady=5)
frame.pack(fill = tk.X,side=tk.LEFT)

frame1 = tk.Frame(master = window)
frame1.pack(fill = tk.Y,side=tk.LEFT)
frame1.columnconfigure([0, 1, 2, 3, 4,5,6,7,8],weight=1, minsize=100)
frame1.rowconfigure([0], minsize=100)


a1 = Arrow()
a1.makeGUI(frame1)
a1.LtoR()
a1.setGrid(0,1)

a2 = Arrow()
a2.makeGUI(frame1)
a2.LtoR()
a2.setGrid(0,3)

a3 = Arrow()
a3.makeGUI(frame1)
a3.LtoR()
a3.setGrid(0,5)

a4 = Arrow()
a4.makeGUI(frame1)
a4.LtoR()
a4.setGrid(0,7)

s1.makeGUI(frame1)
s1.setGrid(0,0)


s2.makeGUI(frame1)
s2.setGrid(0,4)

t1.makeGUI(frame1)
t1.setGrid(0,2)

t2.makeGUI(frame1)
t2.setGrid(0,6)

s3.makeGUI(frame1)
s3.setGrid(0,8)


inputFrame = tk.Label(master = frame, text ="Enter number of \n initial token:")
userEntry = tk.Entry(master = frame, width=10)
setButton =  tk.Button(master = frame, text ="Press to set", command=setInitToken, activebackground="red")
resetButton =  tk.Button(master = frame, text ="Press to reset", command=lambda: reset(placeArray), activebackground="red")
inputFrame.grid(column=0, row=0,sticky="ew")
userEntry.grid(column=0, row=1,sticky="ew")
setButton.grid(column=0, row=2,sticky="ew")
resetButton.grid(column=0, row=3,sticky="ew")

window.mainloop()
