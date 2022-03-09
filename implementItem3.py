import tkinter as tk
from time import sleep
##### BUTTON HANDLER #####
def setInitToken():
    tmp = userEntry.get()
    p1.token = int(tmp)
    p1.frame.config(text=p1.name+"\n"+str(p1.token))
    print(p1.token)

def changeColor(frame, color1, color2):
    frame.config(bg=color1)
    frame.after(500, lambda: frame.config(bg=color2))

def fire(prev,next):
    for i in prev:
        if i.token ==0:
            print("Not enough token to fire")
            changeColor(i.frame,"red","white")
            return
    for i in prev:
        i.token-=1
        i.frame.config(text=i.name+"\n"+str(i.token))
    for i in next:
        i.token+=1
        i.frame.config(text=i.name+"\n"+str(i.token))

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
        self.prev=[]
        self.next=[]
        for i in prev:
            self.prev.append(i)
        for i in next:
            self.next.append(i)
    def makeGUI(self,masterFrame):
            self.frame= tk.Button(master = masterFrame, text=self.name,background="white",command=lambda: fire(self.prev,self.next),activebackground="red",relief=tk.RAISED)
    def setGrid(self,row, col):
        self.frame.grid(row=row, column=col, sticky="nsew")
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
    def Ver(self):
        self.arrow= tk.Canvas(self.frame, width=100, height=100)
        self.arrow.pack()
        self.arrow.create_line(50,0,50,100)
    def Hor(self):
        self.arrow= tk.Canvas(self.frame, width=100, height=100)
        self.arrow.pack()
        self.arrow.create_line(0,50,100,50)
    def Cor3(self):
        self.arrow= tk.Canvas(self.frame, width=100, height=100)
        self.arrow.pack()
        self.arrow.create_line(50,0,50,50)
        self.arrow.create_line(50,50,100,50)
    def Cor2(self):
        self.arrow= tk.Canvas(self.frame, width=100, height=100)
        self.arrow.pack()
        self.arrow.create_line(0,50,50,50)
        self.arrow.create_line(50,50,50,0)
    def setGrid(self,row, col):
        self.frame.grid(row=row, column=col, sticky="nsew")

#### INIT PETRI NET ####
p1=Place("wait")
p2=Place("free",1)
p3=Place("inside/busy")
p5=Place("done",1)
p6=Place("docu")
t1Prev=[]
t1Prev.append(p1)
t1Prev.append(p2)

t1Next=[]
t1Next.append(p3)

t1=Trasition("start",t1Prev,t1Next)

t2Next=[]
t2Next.append(p5)
t2Next.append(p6)

t2=Trasition("doing",t1Next,t2Next)

t3Prev=[]
t3Prev.append(p6)

t3Next=[]
t3Next.append(p2)

t3=Trasition("finish",t3Prev,t3Next)

placeArray=[]
placeArray.append(p1)
placeArray.append(p2)
placeArray.append(p3)

placeArray.append(p5)
placeArray.append(p6)

#### WINDOW SETUP ####
window = tk.Tk()
window.title("Petri Net")

frame = tk.Frame(master = window, padx=5, pady=5)
frame.pack(fill = tk.X,side=tk.LEFT)

frame1 = tk.Frame(master = window)
frame1.pack(fill = tk.Y,side=tk.LEFT)
frame1.columnconfigure([0, 1, 2, 3, 4,5 ,6, 7, 8],weight=1, minsize=100)
frame1.rowconfigure([0, 1, 2, ], minsize=100)


inputFrame = tk.Label(master = frame, text ="Enter number of \n initial token:")
userEntry = tk.Entry(master = frame, width=10)
setButton =  tk.Button(master = frame, text ="Press to set", command=setInitToken, activebackground="red")
resetButton =  tk.Button(master = frame, text ="Press to reset", command=lambda: reset(placeArray), activebackground="red")
inputFrame.grid(column=0, row=0,sticky="ew")
userEntry.grid(column=0, row=1,sticky="ew")
setButton.grid(column=0, row=2,sticky="ew")
resetButton.grid(column=0, row=3,sticky="ew")

p1.makeGUI(frame1)
p1.setGrid(2,0)

p2.makeGUI(frame1)
p2.setGrid(0,2)

p3.makeGUI(frame1)
p3.setGrid(2,4)


p5.makeGUI(frame1)
p5.setGrid(2,8)

p6.makeGUI(frame1)
p6.setGrid(0,6)

t1.makeGUI(frame1)
t1.setGrid(2,2)

t2.makeGUI(frame1)
t2.setGrid(2,6)

t3.makeGUI(frame1)
t3.setGrid(0,4)

a1 = Arrow()
a1.makeGUI(frame1)
a1.LtoR()
a1.setGrid(2,1)

a2 = Arrow()
a2.makeGUI(frame1)
a2.LtoR()
a2.setGrid(2,3)

a3 = Arrow()
a3.makeGUI(frame1)
a3.LtoR()
a3.setGrid(2,5)

a4 = Arrow()
a4.makeGUI(frame1)
a4.LtoR()
a4.setGrid(2,7)

a5 = Arrow()
a5.makeGUI(frame1)
a5.RtoL()
a5.setGrid(0,5)

a6 = Arrow()
a6.makeGUI(frame1)
a6.RtoL()
a6.setGrid(0,3)
''''
a7 = Arrow()
a7.makeGUI(frame1)
a7.Ver()
a7.setGrid(3,2)

a8 = Arrow()
a8.makeGUI(frame1)
a8.Cor3()
a8.setGrid(4,2)

a9 = Arrow()
a9.makeGUI(frame1)
a9.LtoR()
a9.setGrid(4,3)

a10 = Arrow()
a10.makeGUI(frame1)
a10.Hor()
a10.setGrid(4,5)

a11 = Arrow()
a11.makeGUI(frame1)
a11.Cor2()
a11.setGrid(4,6)

a12 = Arrow()
a12.makeGUI(frame1)
a12.BtoT()
a12.setGrid(3,6)
'''
a13 = Arrow()
a13.makeGUI(frame1)
a13.BtoT()
a13.setGrid(1,6)

a14 = Arrow()
a14.makeGUI(frame1)
a14.TtoB()
a14.setGrid(1,2)
window.mainloop()
