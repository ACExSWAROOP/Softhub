from tkinter import *
from urllib import request  
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk
import sv_ttk as sv
import requests
import os 
import webbrowser
from tkinter import filedialog
import shutil
from os.path import basename
import sys

def confirm(app,appname):
    text="do you want to install "+appname+"?"
    x = messagebox.askyesno("do you want to install this application?",text )
    if x == 1:
        app()

def brave():
    url="https://laptop-updates.brave.com/latest/winx64"
    response = request.urlretrieve("https://laptop-updates.brave.com/latest/winx64", "downloads//brave.exe")
    os.system(r"downloads\\brave.exe")

def chromium():
    url="https://download-chromium.appspot.com/dl/Win_x64?type=snapshots"
    response = request.urlretrieve("https://download-chromium.appspot.com/dl/Win_x64?type=snapshots", "downloads//chromium.exe")
    os.system(r"downloads\\chromium.exe")

def firefox():
    url="https://download.mozilla.org/?product=firefox-stub&os=win&lang=en-US&attribution_code=c291cmNlPXd3dy5nb29nbGUuY29tJm1lZGl1bT1yZWZlcnJhbCZjYW1wYWlnbj0obm90IHNldCkmY29udGVudD0obm90IHNldCkmZXhwZXJpbWVudD0obm90IHNldCkmdmFyaWF0aW9uPShub3Qgc2V0KSZ1YT1jaHJvbWUmdmlzaXRfaWQ9KG5vdCBzZXQp&attribution_sig=3466763a646381f4d23891a79de5b2c5da57cff9698bd5c185e938b48ed303e6"
    response = request.urlretrieve("https://download.mozilla.org/?product=firefox-stub&os=win&lang=en-US&attribution_code=c291cmNlPXd3dy5nb29nbGUuY29tJm1lZGl1bT1yZWZlcnJhbCZjYW1wYWlnbj0obm90IHNldCkmY29udGVudD0obm90IHNldCkmZXhwZXJpbWVudD0obm90IHNldCkmdmFyaWF0aW9uPShub3Qgc2V0KSZ1YT1jaHJvbWUmdmlzaXRfaWQ9KG5vdCBzZXQp&attribution_sig=3466763a646381f4d23891a79de5b2c5da57cff9698bd5c185e938b48ed303e6", "downloads//firefox.exe")
    os.system(r"downloads\\firefox.exe") 

def librewolf():
    url="https://gitlab.com/librewolf-community/browser/windows/uploads/8ca22cbdb72aebdb6e1dc7f096fcf65b/librewolf-108.0.1-1.en-US.win64-setup.exe"
    response = request.urlretrieve("https://gitlab.com/librewolf-community/browser/windows/uploads/8ca22cbdb72aebdb6e1dc7f096fcf65b/librewolf-108.0.1-1.en-US.win64-setup.exe", "downloads//librewolf.exe")
    os.system(r"downloads\\librewolf.exe")

def passwordmanager():
    url="https://github.com/VarunAdhityaGB/Password-Manager-GUI/releases/download/v.1.2/Password_Manager_v.1.2_Setup.exe"
    response = request.urlretrieve("https://github.com/VarunAdhityaGB/Password-Manager-GUI/releases/download/v.1.2/Password_Manager_v.1.2_Setup.exe", "downloads//passwordmanager.exe")
    os.system(r"downloads\\passwordmanager.exe")
main = Tk()
sv.set_theme("dark")
main.title("softhub")
main.resizable(0, 0)
app_width = 1024
app_height = 512
screenwidth = main.winfo_screenwidth()
screenheight = main.winfo_screenheight()

x = (screenwidth / 2) - (app_width / 2)
y = (screenheight / 2) - (app_height / 2)

main.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
mainheader=ttk.Label(main,text="welcome to softhub.",font=("Segou UI variable",30))
mainheader.place(relx=0.35,rely=0)
########################################################browsers#######################################################
browsersection=ttk.Label(main,text="Browsers",font=("Segou UI variable",15))
browsersection.place(relx=0.05,rely=0.2)

browsersectionframe= Frame(main)
browsersectionframe.place(relx=0.05,rely=0.3)

#############################spacing between each app##############################
spacing=ttk.Label(browsersectionframe,text="     ")
spacing.grid(row=0,column=1)
spacing=ttk.Label(browsersectionframe,text="     ")
spacing.grid(row=0,column=3)
spacing=ttk.Label(browsersectionframe,text="     ")
spacing.grid(row=0,column=5)
spacing=ttk.Label(browsersectionframe,text="     ")
spacing.grid(row=0,column=7)
spacing=ttk.Label(browsersectionframe,text="     ")
spacing.grid(row=0,column=9)

##############brave###############
braveicon= PhotoImage(file = r"images\Brave_lion_icon.svg.png")
braveimage = braveicon.subsample(30,30)
bravebrowser=ttk.Button(browsersectionframe,image=braveimage,text="Brave",width=10,compound=LEFT,command=lambda: confirm(brave,"brave browser"))
bravebrowser.grid(row=0,column=0)

#############chromium##############
chromiumicon= PhotoImage(file = r"images\Chromium_Logo.svg.png")
chromiumimage = chromiumicon.subsample(45,45)
chromiumbrowser=ttk.Button(browsersectionframe,image=chromiumimage,text="Chromium",width=10,compound=LEFT,command=lambda: confirm(chromium,"chromium browser"))
chromiumbrowser.grid(row=0,column=2)

##############firefox###############
firefoxicon= PhotoImage(file = r"images\Firefox_logo,_2017.svg.png")
firefoximage = firefoxicon.subsample(27,27)
firefoxbrowser=ttk.Button(browsersectionframe,image=firefoximage,text="Firefox",width=10,compound=LEFT,command=lambda: confirm(firefox,"firefox browser"))
firefoxbrowser.grid(row=0,column=4)

##############librewolf###############
librewolficon= PhotoImage(file = r"images\LibreWolf_icon.svg.png")
librewolfimage = librewolficon.subsample(47,47)
librewolfbrowser=ttk.Button(browsersectionframe,image=librewolfimage,text="Librewolf",width=10,compound=LEFT,command=lambda: confirm(librewolf,"librewolf browser"))
librewolfbrowser.grid(row=0,column=6)

#############################################################utilities##################################################

utilitiessection=ttk.Label(main,text="Utilities",font=("Segou UI variable",15))
utilitiessection.place(relx=0.05,rely=0.5)

utilitiessectionframe= Frame(main)
utilitiessectionframe.place(relx=0.05,rely=0.6)

################passwordmanager###########
passwordmanagerbrowser=ttk.Button(utilitiessectionframe,text="passwordmanager",width=15,compound=LEFT,command=lambda: confirm(passwordmanager,"passwordmanager"))
passwordmanagerbrowser.grid(row=0,column=0)

main.mainloop()