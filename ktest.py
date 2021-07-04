from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import datetime
import threading
import speech_recognition as sr
from PIL import ImageTk
import playsound as ps
import cv2, sys, numpy, os

root = Tk()
root.geometry('800x500')
img=ImageTk.PhotoImage(file=r"C:\Users\Priya\Desktop\Katathon\lockopen.png")
img1=ImageTk.PhotoImage(file=r"C:\Users\Priya\Desktop\Katathon\lockclose.png")
labello = tk.Label(root, image=img)
labello.pack()
#def lock():


def imagecapture():
    datasets = 'datasets'
    sub_data = 'vidya'

    path = os.path.join(datasets, sub_data)
    if not os.path.isdir(path):
        os.mkdir(path)
    webcam = cv2.VideoCapture(0)
    count = 1
    while count <= 30:
        (_, im) = webcam.read()
        cv2.imwrite('% s/% s.png' % (path, count), im)
        count += 1

        cv2.imshow('Image Capturing', im)
        key = cv2.waitKey(10)
        if key == 27:
            break
    webcam = cv2.VideoCapture(0)

    cv2.imshow('Image Capturing', im)

    key = cv2.waitKey(10)
    if key == 27:
        exit()


def voice():
    msg = tk.StringVar()
    msg.set(' ')
    root.issequencematching=False

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)

        try:
#if(root.issequencematching==False):
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
            var1 = format(text)

            if (var1 == "help help help"):
                msg.set(str("Emergency Mode Activated"))
                labello.config(image=img1)
                imagecapture()
                ps.playsound("C:\\Users\\Priya\\Desktop\\Katathon\\ambulance sound.mp3")
                img.config(image=img1)
                root.issequencematching=True
            else:
                #msg.set(str("Not a valid command"))
                root.issequencematching=True

            label3 = tk.Label(root, textvariable=msg,font="none 24 bold")
            #label3.pack()
            label3.place(relx=0.5, rely=0.5, anchor=CENTER)
            '''if(root.issequencematching==True):
                label3.destroy()'''

        except:
            print("Sorry could not recognize what you said")


root.counter=0
root.previousstate=False


def counter1():
    root.counter= root.counter+1
    if(root.previousstate == False):
        root.previousstate = True
    else:
        root.previousstate = False


def resetCounter():
    if((root.counter < 5)):
        root.counter = 0;

timer = threading.Timer(5.0,resetCounter)
timer.start()

timer.cancel()

def start():

    counter1()
    normalmode()

    if(root.counter==5 ) :
        emergencymode()

        root.counter=0
    else:
        print()


def emergencymode():
    msg = tk.StringVar()
    msg.set(' ')
    msg.set(str("Emergency mode activated"))
    labello.config(image=img1)
    label = tk.Label(root, textvariable=msg,font="none 24 bold")
    label.place(relx=0.5, rely=0.5, anchor=CENTER)

    imagecapture()
    ps.playsound("C:\\Users\\Priya\\Desktop\\Katathon\\ambulance sound.mp3")
    #label.pack()


def normalmode():

    if(root.previousstate == True):

        global time1,time2,label,label1
        e = datetime.datetime.now()
        time1 = tk.StringVar()
        time1.set(' ')
        time2 = tk.StringVar()
        time2.set(' ')
        time1.set(str(" %s/%s/%s" % (e.day, e.month, e.year)))
        time2.set(str(" %s:%s:%s " % (e.hour, e.minute, e.second)))
        label = tk.Label(root, textvariable=time1,bg="black",fg="white",font="none 24 bold")
        label.place(relx=0.5,rely=0.5,anchor=CENTER)
        label1 = tk.Label(root, textvariable=time2,bg="black",fg="white",font="none 24 bold")
        label1.place(relx=0.5, rely=0.6, anchor=CENTER)
        #label.pack()
        #label1.pack()

    else:
        label.destroy()
        label1.destroy()




photo = PhotoImage(file=r"C:\Users\Priya\Desktop\Katathon\power.png")
button = tk.Button(root, image=photo, command=start)
button.pack(side=LEFT)

photo1 = PhotoImage(file=r"C:\Users\Priya\Desktop\Katathon\voice.png")
button1 = tk.Button(root, image=photo1, command=voice)
button1.pack(side=RIGHT)


mainloop()

