from tkinter import *
from math import *  
from time import *
from random import *

root = Tk()
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
root.attributes('-fullscreen', True)
s = Canvas(root, width=sw, height=sh, background="light blue")
s.pack()

def var():
    global dhuman, dobject, logo, interfacebg, width, height, runsim, limhuman, scene

    width = sw
    height = sh
    runsim = False
    dhuman = 985
    frame = 0
    g = 9.81
    limhuman = 7094.50
    scene = 1

    logo = PhotoImage(file="interfacetext.gif")
    interfacebg = PhotoImage(file = "interfacebg.gif")

    interface()

def interface():
    global xback, yback, xstart, ystart,logodrawing,interfacebgdrawing, button1, text1

    
    xback = sw/2
    yback = sh/2
    xstart = sw/2-200
    ystart = sh/2-50

    interfacebgdrawing = s.create_image(xback, yback, image = interfacebg)
    logodrawing = s.create_image(xback, yback-300, image = logo)

    button1 = s.create_rectangle(xstart,ystart, xstart + 400, ystart + 100, fill = "gold", outline = "black")
        
    text1 = s.create_text(xback,yback, text = "Start Simulation", anchor=N, font= "Times 25", fill="black")

def start():
    global button1,text1,logodrawing, runsim

    s.delete(button1,text1,logodrawing)

    selection()

def selection():
    global xback, yback, xstart, ystart,button2, button3, text2, text3

    button2 = s.create_rectangle(xstart,ystart-300, xstart + 400, ystart - 200, fill = "light green", outline = "black")
    button3 = s.create_rectangle(xstart,ystart+300, xstart + 400, ystart + 400, fill = "light green", outline = "black")
   

    text2 = s.create_text(xstart+200, ystart-250, text = "Human", anchor=N, font = "Times 25", fill = "black")
    text3 = s.create_text(xstart+200, ystart+350, text = "Object", anchor=N, font = "Times 25", fill = "black")
   

def mouseClickHandler( event ):
    global xstart, ystart, xMouse, yMouse, rungame, death, selectdif, death, gameplayed, runsim, scene

    xMouse = event.x
    yMouse = event.y

    if xstart <= xMouse <= xstart+400 and ystart <= yMouse <= ystart + 100 and scene == 1:
        scene = scene + 1
        start()

    if xstart <= xMouse <= xstart+400 and ystart-300 <= yMouse <= ystart - 200 and scene == 2:
        scene = scene + 1
        Human()

    if xstart <= xMouse <= xstart+400 and ystart+300 <= yMouse <= ystart + 400 and scene == 2 :
        scene = scene + 1
        Object()
        
    if xstart <= xMouse <= xstart+400 and ystart <= yMouse <= ystart + 100 and runsim == True and scene == 3:
        backtostart()


def Human():
    global x1,x3,x4,d,xBack, limhuman, runsim, button2, button3, text, text2, text3, text4, interfacebgdrawing, sky
    runsim=True
    human = PhotoImage(file="scubadiver.gif")
    
    mhuman = 20*float(input("Mass: "))
    den = 1000
    vol = mhuman/den

    x3 = 1880
    x4 = 1920
    y3 = 0
    

    x1 = 960
    y1 = 540
    d = 0
    p = 0
    xBack = 540

    a = (mhuman*9.81 - 997*vol*9.81)/mhuman

    t = float(input("How deep would you like to go: "))
    s.delete(button2, button3, text2, text3,interfacebgdrawing)
    if a > 0:
        
        while d < t:
            sky =s.create_rectangle(0, 0, 1920, xBack, fill="white")
            humandrawing = s.create_image(x1, y1, image = human)
            if y1<=800:
                d=y1-540
                y1 += 30*a
                
            else:
                if xBack>0:
                    xBack-=30*a
                d += 30*a
            p = (99.97/10.06)*d+101.35
            text = s.create_text(1600, 50, text="Displacement:" + str(round(d, 2))+"m", font="Times 20", fill = "black")
            text2 = s.create_text(1600, 100, text="Pressure:" + str(round(p, 2))+"Kpal", font="Times 20", fill = "black")
            text3 = s.create_text(1600, 150, text="Velocity:" + str(round(d, 2))+"m/s", font="Times 20", fill = "black")
            text4 = s.create_text(1600, 200, text="Acceleration:" + str(round(a, 2))+"m/s^2", font="Times 20", fill = "black")
            if p > limhuman:
                break
            s.update()
            sleep(1/60)
            s.delete(humandrawing, sky, text, text2, text3, text4)
        humandrawing = s.create_image(x1, y1, image = human)
        s.delete(text, text2, text3, text4)
        
        if p > limhuman:
            block1 = s.create_rectangle(360, 440, 1560, 640, fill = "red", outline = "black")
            text5 = s.create_text(960, 540, text = "human will die from the extreme pressure!",font="Times 50", fill = "black")
            s.update()
            sleep(2)
            s.delete(block1, text5)
        else:
            block2 = s.create_rectangle(360, 440, 1560, 640, fill = "green", outline = "black")
            text6 = s.create_text(960, 540, text = "Human is safe from the pressure!",font="Times 50", fill = "black")
            s.update()
            sleep(2)
            s.delete(block2, text6)
        s.delete(humandrawing)
        restart()
    else:
        print("The human will float")
        restart()
def Object():
    global x1,x2,x3,x4,d,xBack,runsim, button2, button3, text, text2, text3,text4, interfacebgdrawing, sky
    runsim=True
    mo = 20*float(input("Mass: "))
    oLength = float(input("Length of object: "))
    oWidth = float(input("Width of object: "))
    oHeight = float(input("Height of object: "))

    x3 = 1880
    x4 = 1920
    y3 = 0


    x1 = 960 - (oWidth/2)*50
    x2 = 960 + (oWidth/2)*50
    y1 = 540 - oHeight*50
    d=0
    xBack = 540

    vo = oLength * oWidth * oHeight

    a = (mo*9.81 - 997*vo*9.81)/mo

    t = float(input("How deep would you like to go: "))
    s.delete(button2, button3, text2, text3,interfacebgdrawing)

    if a > 0:

        while d < t:
            sky=s.create_rectangle(0, 0, 1920, xBack, fill="white")
            y2 = y1 + oHeight*50
            obj = s.create_rectangle (x1, y1, x2, y2, fill="grey")
            if y1<=800:
                d=y1-540
                y1 += a
                
            else:
                if xBack>0:
                    xBack-=a
                d += a

            p = (99.97/10.06)*d+101.35
            text = s.create_text(1600, 50, text="Displacement:" + str(round(d, 2))+"m", font="Times 20", fill = "black")
            text2 = s.create_text(1600, 100, text="Pressure:" + str(round(p, 2))+"Kpal", font="Times 20", fill = "black")
            text3 = s.create_text(1600, 150, text="Velocity:" + str(round(d, 2))+"m/s", font="Times 20", fill = "black")
            text4 = s.create_text(1600, 200, text="Acceleration:" + str(round(a, 2))+"m/s^2", font="Times 20", fill = "black")
            s.update()
            sleep(1/60)
            s.delete(obj, sky, text, text2, text3, text4)
        obj = s.create_rectangle (x1, y1, x2, y2, fill="grey")
        s.delete(obj, sky, text, text2, text3, text4)
        restart()
    else:
        print("The object will float")
        restart()


def restart():
    global restartbutton, restarttext
    
    restartbutton=s.create_rectangle( xstart, ystart, xstart+400, ystart+100, fill="yellow")
    restarttext = s.create_text(xback,yback, text = "Restart", anchor=N, font= "Times 25", fill="black")
    
def backtostart():
    global restartbutton, restarttext
    s.delete(restartbutton, restarttext, sky, text, text2, text3, text4)
    var()

root.after( 0, var )

s.bind( "<Button-1>", mouseClickHandler )



s.focus_set()
root.mainloop()

s.delete(selection, Human, start, interface)
