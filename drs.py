import tkinter
import PIL.Image, PIL.ImageTk
import cv2
from functools import partial
import threading
import imutils
import time
# ........................................
stream = cv2.VideoCapture("runout2.mp4")
flag = True
# Functions...
def play(speed):
    global flag
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed,frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    if flag:
        canvas.create_text(135,26,fill="black",font="Times 25 italic bold",text="Decision Pending")
    flag = not flag

def pending(decision):
    # display decision pending image
    frame = cv2.cvtColor(cv2.imread('decision.jpg'),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH,height=SET_HEIGHT)
    frame= PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)

    # wait for some seconds...
    time.sleep(1.5)

    # display sponser image...
    frame = cv2.cvtColor(cv2.imread('sponser.jpg'),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH,height=SET_HEIGHT)
    frame= PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)

    # wait for some seconds...
    time.sleep(2)

    # given decision...
    if decision == 'out':
        decisionImg = "out_pic.jpg"
    else:
        decisionImg = "not_out.jpg"
    frame = cv2.cvtColor(cv2.imread(decisionImg),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH,height=SET_HEIGHT)
    frame= PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
# ....................................................
    # wait for some seconds...
    # time.sleep(1.5)

    # gif = cv2.VideoCapture('happy.gif')

    # ret,frame = gif.read()
    # frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    # frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    # canvas.image = frame
    # canvas.create_image(0,0,image=frame,anchor=tkinter.NW)

    # gif = cv2.VideoCapture('happy.gif')

    # ret,frame = gif.read()
    # frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    # frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    # canvas.image = frame
    # canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    # canvas.after()

    # ret,frame = gif.read() 
    # img = PIL.Image.fromarray(frame)
    # img = img.convert('RGB')
    # canvas.image=frame
    # canvas.create_image(0,0,image=frame,anchor=tkinter.NW)


def out():
    thread = threading.Thread(target=pending,args=("out",))
    thread.daemon=1
    thread.start()
    # print('Player is Out')

def not_out():
    thread = threading.Thread(target=pending,args=("not out",))
    thread.daemon=1
    thread.start()
    # print('Player is Not Out')

def exit_f():
    exit()
# ..........................................
SET_WIDTH = 650
SET_HEIGHT = 370
# ..........................................
window = tkinter.Tk()
window.title("Decision Review System")
# ..........................................
cv_img = cv2.cvtColor(cv2.imread('drs.jpg'),cv2.COLOR_BGR2RGB)
# ..........................................
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0,ancho=tkinter.NW,image=photo)
canvas.pack()
# ..........................................
# Buttons...
btnPfast = tkinter.Button(window,text="<< Previous (fast)",width=50, command=partial(play,-20))
btnPfast.pack()

btnPslow = tkinter.Button(window,text="<< Previous (slow)",width=50, command=partial(play,-2))
btnPslow.pack()

btnNfast = tkinter.Button(window,text="Next (fast) >>",width=50, command=partial(play,20))
btnNfast.pack()

btnNslow = tkinter.Button(window,text="Next (slow) >>",width=50, command=partial(play,2))
btnNslow.pack()

btnOut = tkinter.Button(window,text="Out",width=50,command=out)
btnOut.pack()

btnNotOut = tkinter.Button(window,text="Not Out",width=50,command=not_out)
btnNotOut.pack()

btnExit = tkinter.Button(window,text="Exit",width=50,command=exit_f)
btnExit.pack()

# .......................................
window.mainloop()