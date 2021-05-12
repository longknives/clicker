import datetime
from threading import Timer
import time
from tkinter.constants import COMMAND, END, FALSE
import urllib.request as urllib2
import tkinter as tk
from tkinter import ttk
import time as t
from tkinter import messagebox
import googlesearch
import webbrowser
from bs4 import BeautifulSoup
import re
from urllib.request import url2pathname
from urllib.request import url2pathname
import urllib
import urllib3
import pyautogui
import requests
import sys
import os
from tkinter import Tk, Label, Button
from pynput import keyboard
import time
from tkinter import *


import keyboard
import pyautogui  


buttonClicked = False


window = tk.Tk()
key1 = ''
sec = 0
window.title("dev-longknives") 
window.minsize(600,400) 

powerful = False;

print("▄▀▀█▄▄   ▄▀▀█▄   ▄▀▀▀▀▄  ▄▀▀▄ ▄▄")
print('█ ▄▀   █ ▐ ▄▀ ▀▄ █ █   ▐ █  █   ▄▀ ')
print("▐ █    █   █▄▄▄█    ▀▄   ▐  █▄▄▄█  ")
print("  █    █  ▄▀   █ ▀▄   █     █   █  ")
print(" ▄▀▄▄▄▄▀ █   ▄▀   █▀▀▀     ▄▀  ▄▀  ")

def gui(key1, sec, powerful):
 time.sleep(5)
 print("LOADED")
 print("LOADED")
 print("LOADED")

 print("if you launch the script twice the script will have insane amounts of power")

 while True: 
    try: 
        if keyboard.is_pressed(name1.get()): 
           time.sleep(name2.get())
          
           pyautogui.click()   



           
    except:
        break 



           




 name = tk.StringVar()
 nameEntered = ttk.Entry(window, width = 15, textvariable = name)
 nameEntered.grid(column = 10, row = 1) 


name1 = tk.StringVar()
nameEntered = ttk.Entry(window, width = 15, textvariable = name1)
nameEntered.grid(column = 10, row = 1) 


name2 = tk.DoubleVar()
nameEntered = ttk.Entry(window, width = 15, textvariable = name2)
nameEntered.grid(column = 10, row = 2) 

button3 = ttk.Button(window, text = "Enter", command=lambda key1 = name1.get():gui(key1, sec, powerful))
             
button3.grid(column= 10, row = 3) 










             


label = ttk.Label(window, text = "Key") 
label.grid(column = 0, row = 1) 

label = ttk.Label(window, text = "Seconds") 
label.grid(column = 0, row = 2) 








window.mainloop()






