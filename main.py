from tkinter import *
from urllib import request  
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk
import sv_ttk as sv
import os 
import requests

def confirm(appname):
    def internet_stat(url="https://www.google.com/", timeout=3):
        try:
            r = requests.head(url=url, timeout=timeout)
            return True
        except requests.exceptions.ConnectionError as e:
            return False
            
    net_stat = internet_stat()

    while net_stat==False:
        x=messagebox.askretrycancel("no internet connection.","no internet connection please try later.")
        if x==1:
            net_stat=internet_stat()
            if net_stat==True:
                break
        elif x==0:
            break

        if net_stat==True:
            text="do you want to install "+appname+"?"
            x = messagebox.askyesno("do you want to install this application?",text )
            if x == 1:
                continue

def install(url,path,file):
    response = request.urlretrieve(url, path)
    os.system(file)

mainsplash = Tk()
sv.set_theme("dark")
mainsplash.overrideredirect(True)
app_width = 1024
app_height = 512
screenwidth = mainsplash.winfo_screenwidth()
screenheight = mainsplash.winfo_screenheight()

x = (screenwidth / 2) - (app_width / 2)
y = (screenheight / 2) - (app_height / 2)

mainsplash.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
bg_image = ImageTk.PhotoImage(Image.open(r"images\softhub load.png"))
label1 = Label(mainsplash, image=bg_image)
label1.pack()

def mainwindow():
    main = Toplevel()
    mainsplash.withdraw()
    app_width = 1024
    app_height = 512
    screenwidth = main.winfo_screenwidth()
    screenheight = main.winfo_screenheight()

    x = (screenwidth / 2) - (app_width / 2)
    y = (screenheight / 2) - (app_height / 2)

    main.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    main.title("softhub")
    main.tk.call('wm', 'iconphoto', main._w, ImageTk.PhotoImage(file='images\softhub.ico'))
    main.resizable(0, 0)
    
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
    braveurl="https://laptop-updates.brave.com/latest/winx64"
    bravepath="downloads//brave.exe"
    bravefile="downloads\\brave.exe"
    bravebrowser=ttk.Button(browsersectionframe,image=braveimage,text="Brave",width=10,compound=LEFT,command=lambda: [confirm("brave browser"),install(braveurl,bravepath,bravefile)])
    bravebrowser.grid(row=0,column=0)

    #############chromium##############

    chromiumicon= PhotoImage(file = r"images\Chromium_Logo.svg.png")
    chromiumimage = chromiumicon.subsample(45,45)
    chromiumurl="https://download-chromium.appspot.com/dl/Win_x64?type=snapshots"
    chromiumpath="downloads//chromium.exe"
    chromiumfile="downloads\\chromium.exe"
    chromiumbrowser=ttk.Button(browsersectionframe,image=chromiumimage,text="Chromium",width=10,compound=LEFT,command=lambda: [confirm("chromium browser"),install(chromiumurl,chromiumpath,chromiumfile)])
    chromiumbrowser.grid(row=0,column=2)

    ##############firefox###############

    firefoxicon= PhotoImage(file = r"images\Firefox_logo,_2017.svg.png")
    firefoximage = firefoxicon.subsample(27,27)
    firefoxurl="https://download.mozilla.org/?product=firefox-stub&os=win&lang=en-US&attribution_code=c291cmNlPXd3dy5nb29nbGUuY29tJm1lZGl1bT1yZWZlcnJhbCZjYW1wYWlnbj0obm90IHNldCkmY29udGVudD0obm90IHNldCkmZXhwZXJpbWVudD0obm90IHNldCkmdmFyaWF0aW9uPShub3Qgc2V0KSZ1YT1jaHJvbWUmdmlzaXRfaWQ9KG5vdCBzZXQp&attribution_sig=3466763a646381f4d23891a79de5b2c5da57cff9698bd5c185e938b48ed303e6"
    firefoxpath="downloads//firefox.exe"
    firefoxfile="downloads\\firefox.exe"
    firefoxbrowser=ttk.Button(browsersectionframe,image=firefoximage,text="Firefox",width=10,compound=LEFT,command=lambda: [confirm("firefox browser"),install(firefoxurl,firefoxpath,firefoxfile)])
    firefoxbrowser.grid(row=0,column=4)

    ##############librewolf###############

    librewolficon= PhotoImage(file = r"images\LibreWolf_icon.svg.png")
    librewolfimage = librewolficon.subsample(47,47)
    librewolfurl="https://gitlab.com/librewolf-community/browser/windows/uploads/8ca22cbdb72aebdb6e1dc7f096fcf65b/librewolf-108.0.1-1.en-US.win64-setup.exe"
    librewolfpath="downloads//librewolf.exe"
    librewolffile="downloads\\librewolf.exe"
    librewolfbrowser=ttk.Button(browsersectionframe,image=librewolfimage,text="Librewolf",width=10,compound=LEFT,command=lambda: [confirm("librewolf browser"),install(librewolfurl,librewolfpath,librewolffile)])
    librewolfbrowser.grid(row=0,column=6)

    #############################################################utilities##################################################

    utilitiessection=ttk.Label(main,text="Utilities",font=("Segou UI variable",15))
    utilitiessection.place(relx=0.05,rely=0.5)

    utilitiessectionframe= Frame(main)
    utilitiessectionframe.place(relx=0.05,rely=0.6)

    ################passwordmanager###########
    passwordmanagerurl="https://github.com/VarunAdhityaGB/Password-Manager-GUI/releases/download/v.1.2/Password_Manager_v.1.2_Setup.exe"
    passwordmanagerpath="downloads//passwordmanager.exe"
    passwordmanagerfile="downloads\\passwordmanager.exe"
    passwordmanagerutility=ttk.Button(utilitiessectionframe,text="passwordmanager",width=15,compound=LEFT,command=lambda: [confirm("passwordmanager"),install(passwordmanagerurl,passwordmanagerpath,passwordmanagerfile)])
    passwordmanagerutility.grid(row=0,column=0)

    main.mainloop()

mainsplash.after(3000, mainwindow)
mainsplash.mainloop()