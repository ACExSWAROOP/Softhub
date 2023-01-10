from tkinter import *
from urllib import request  
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk
import sv_ttk as sv
import os 
import requests

class AppURLopener(request.FancyURLopener):
    version = "Mozilla/5.0"

def intcheck():
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
            continue

def install(url,path,file,appname):
    text="do you want to install "+appname+"?"
    x = messagebox.askyesno("do you want to install this application?",text )
    while x == 1:
        response = request.urlretrieve(url,path)
        os.system(file)
        break

mainsplash = Tk()
sv.set_theme("dark")
mainsplash.overrideredirect(True)
app_width = 1024
app_height = 512
screenwidth = mainsplash.winfo_screenwidth()
screenheight = mainsplash.winfo_screenheight()
mainsplash.attributes("-alpha", 0.95)
x = (screenwidth / 2) - (app_width / 2)
y = (screenheight / 2) - (app_height / 2)

mainsplash.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
bg_image = ImageTk.PhotoImage(Image.open(r"images\softhub load.png"))
label1 = Label(mainsplash, image=bg_image)
label1.pack()

def mainwindow():
    main = Toplevel()
    mainsplash.withdraw()
    main.state('zoomed')
    screenwidth = main.winfo_screenwidth()
    screenheight = main.winfo_screenheight()
    app_width = screenwidth
    app_height = screenheight
    main.geometry(f'{app_width}x{app_height}')
    main.title("Softhub")
    main.tk.call('wm', 'iconphoto', main._w, ImageTk.PhotoImage(file='images\softhub.ico'))
    main.attributes("-alpha", 0.9)

    
    main_frame = Frame(main)
    main_frame.pack(fill=BOTH,expand=1)

    # Create Frame for X Scrollbar
    sec = Frame(main_frame)
    sec.pack(fill=X,side=BOTTOM)

    # Create A Canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

    # Add A Scrollbars to Canvas
    x_scrollbar = ttk.Scrollbar(sec,orient=HORIZONTAL,command=my_canvas.xview)
    x_scrollbar.pack(side=BOTTOM,fill=X)
    y_scrollbar = ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
    y_scrollbar.pack(side=RIGHT,fill=Y)

    # Configure the canvas
    my_canvas.configure(xscrollcommand=x_scrollbar.set)
    my_canvas.configure(yscrollcommand=y_scrollbar.set)
    my_canvas.bind("<Configure>",lambda e: my_canvas.config(scrollregion= my_canvas.bbox(ALL))) 

    # Create Another Frame INSIDE the Canvas
    second_frame = Frame(my_canvas)

    # Add that New Frame a Window In The Canvas
    my_canvas.create_window((0,0),window= second_frame, anchor="nw")

    ########################################################browsers#######################################################

    browsersection=ttk.Label(second_frame,text="Browsers",font=("Segou UI variable",15))
    browsersection.grid(row=0,column=0,pady=15,padx=15)

    browsersectionframe= Frame(second_frame)
    browsersectionframe.grid(row=1,column=0,pady=15,padx=15)

    #############################spacing between each app##############################

    spacing=ttk.Label(browsersectionframe,text="         ")
    spacing.grid(row=0,column=1)
    spacing=ttk.Label(browsersectionframe,text="         ")
    spacing.grid(row=0,column=3)
    spacing=ttk.Label(browsersectionframe,text="         ")
    spacing.grid(row=0,column=5)
    spacing=ttk.Label(browsersectionframe,text="         ")
    spacing.grid(row=0,column=0)
    spacing=ttk.Label(browsersectionframe,text="         ")
    spacing.grid(row=0,column=7)
    spacing=ttk.Label(browsersectionframe,text="         ")
    spacing.grid(row=0,column=9)
    spacing=ttk.Label(browsersectionframe,text="         ")
    spacing.grid(row=0,column=11)

    ##############brave###############

    braveicon= PhotoImage(file = r"images\Brave_lion_icon.svg.png")
    braveimage = braveicon.subsample(30,30)
    braveurl="https://laptop-updates.brave.com/latest/winx64"
    bravepath="downloads//brave.exe"
    bravefile="downloads\\brave.exe"
    bravebrowser=ttk.Button(browsersectionframe,image=braveimage,text="Brave",width=10,compound=LEFT,command=lambda: [intcheck(),install(braveurl,bravepath,bravefile,"brave browser")])
    bravebrowser.grid(row=0,column=0)

    ##############firefox###############

    firefoxicon= PhotoImage(file = r"images\Firefox_logo,_2017.svg.png")
    firefoximage = firefoxicon.subsample(27,27)
    firefoxurl="https://download.mozilla.org/?product=firefox-stub&os=win&lang=en-US&attribution_code=c291cmNlPXd3dy5nb29nbGUuY29tJm1lZGl1bT1yZWZlcnJhbCZjYW1wYWlnbj0obm90IHNldCkmY29udGVudD0obm90IHNldCkmZXhwZXJpbWVudD0obm90IHNldCkmdmFyaWF0aW9uPShub3Qgc2V0KSZ1YT1jaHJvbWUmdmlzaXRfaWQ9KG5vdCBzZXQp&attribution_sig=3466763a646381f4d23891a79de5b2c5da57cff9698bd5c185e938b48ed303e6"
    firefoxpath="downloads//firefox.exe"
    firefoxfile="downloads\\firefox.exe"
    firefoxbrowser=ttk.Button(browsersectionframe,image=firefoximage,text="Firefox",width=10,compound=LEFT,command=lambda: [intcheck(),install(firefoxurl,firefoxpath,firefoxfile,"firefox browser")])
    firefoxbrowser.grid(row=0,column=2)

    ##############librewolf###############

    librewolficon= PhotoImage(file = r"images\LibreWolf_icon.svg.png")
    librewolfimage = librewolficon.subsample(47,47)
    librewolfurl="https://gitlab.com/librewolf-community/browser/windows/uploads/8ca22cbdb72aebdb6e1dc7f096fcf65b/librewolf-108.0.1-1.en-US.win64-setup.exe"
    librewolfpath="downloads//librewolf.exe"
    librewolffile="downloads\\librewolf.exe"
    librewolfbrowser=ttk.Button(browsersectionframe,image=librewolfimage,text="Librewolf",width=10,compound=LEFT,command=lambda: [intcheck(),install(librewolfurl,librewolfpath,librewolffile,"librewolf browser")])
    librewolfbrowser.grid(row=0,column=4)

    ##############tor browser###############

    toricon= PhotoImage(file = r"images\Tor_Browser_icon.svg.png")
    torimage = toricon.subsample(27,27)
    torurl="https://www.torproject.org/dist/torbrowser/12.0.1/torbrowser-install-win64-12.0.1_ALL.exe"
    torpath="downloads//tor.exe"
    torfile="downloads\\tor.exe"
    torbrowser=ttk.Button(browsersectionframe,image=torimage,text="Tor",width=10,compound=LEFT,command=lambda: [intcheck(),install(torurl,torpath,torfile,"tor browser")])
    torbrowser.grid(row=0,column=6)

    ##############vivaldi browser###############

    vivaldiicon= PhotoImage(file = r"images\Vivaldi_web_browser_logo.svg.png")
    vivaldiimage = vivaldiicon.subsample(24,24)
    vivaldiurl="https://downloads.vivaldi.com/stable/Vivaldi.5.6.2867.50.x64.exe"
    vivaldipath="downloads//vivaldi.exe"
    vivaldifile="downloads\\vivaldi.exe"
    vivaldibrowser=ttk.Button(browsersectionframe,image=vivaldiimage,text="Vivaldi",width=10,compound=LEFT,command=lambda: [intcheck(),install(vivaldiurl,vivaldipath,vivaldifile,"vivaldi browser")])
    vivaldibrowser.grid(row=0,column=8)

    #############chrome##############

    chromeicon= PhotoImage(file = r"images\Google_Chrome_icon_(February_2022).svg.png")
    chromeimage = chromeicon.subsample(45,45)
    chromeurl="https://www.google.com/intl/en_in/chrome/thank-you.html?statcb=1&installdataindex=empty&defaultbrowser=0#"
    chromepath="downloads//chrome.exe"
    chromefile="downloads\\chrome.exe"
    chromebrowser=ttk.Button(browsersectionframe,image=chromeimage,text="Chrome",width=10,compound=LEFT,command=lambda: [intcheck(),install(chromeurl,chromepath,chromefile,"chrome browser")])
    chromebrowser.grid(row=0,column=10)

    #############msedge##############

    msedgeicon= PhotoImage(file = r"images\Microsoft_Edge_logo_(2019).svg.png")
    msedgeimage = msedgeicon.subsample(11,11)
    msedgeurl="https://microsoft-edge.en.softonic.com/download"
    msedgepath="downloads//msedge.exe"
    msedgefile="downloads\\msedge.exe"
    msedgebrowser=ttk.Button(browsersectionframe,image=msedgeimage,text="MS Edge",width=10,compound=LEFT,command=lambda: [intcheck(),install(msedgeurl,msedgepath,msedgefile,"msedge browser")])
    msedgebrowser.grid(row=0,column=12)

    #############################################################communication##################################################
    communicationsection=ttk.Label(second_frame,text="Communication",font=("Segou UI variable",15))
    communicationsection.grid(row=2,column=0,pady=15,padx=15)

    communicationsectionframe= Frame(second_frame)
    communicationsectionframe.grid(row=3,column=0,pady=15,padx=15)

    spacing=ttk.Label(communicationsectionframe,text="         ")
    spacing.grid(row=0,column=1)
    spacing=ttk.Label(communicationsectionframe,text="         ")
    spacing.grid(row=0,column=3)
    spacing=ttk.Label(communicationsectionframe,text="         ")
    spacing.grid(row=0,column=5)
    spacing=ttk.Label(communicationsectionframe,text="         ")
    spacing.grid(row=0,column=7)
    spacing=ttk.Label(communicationsectionframe,text="         ")
    spacing.grid(row=0,column=9)
    spacing=ttk.Label(communicationsectionframe,text="         ")
    spacing.grid(row=0,column=11)
    spacing=ttk.Label(communicationsectionframe,text="         ")
    spacing.grid(row=1,column=0)

    ##############discord###############

    discordicon= PhotoImage(file = r"images\636e0a6a49cf127bf92de1e2_icon_clyde_blurple_RGB.png")
    discordimage = discordicon.subsample(12,12)
    discordurl="https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x86" 
    discordpath="downloads//discord.exe"
    discordfile="downloads\\discord.exe"
    discord=ttk.Button(communicationsectionframe,image=discordimage,text="Discord",width=9,compound=LEFT,command=lambda: [intcheck(),install(discordurl,discordpath,discordfile,"discord")])
    discord.grid(row=0,column=0)

    ##############teams###############

    teamsicon= PhotoImage(file = r"images\Microsoft_Office_Teams_(2018–present).svg.png")
    teamsimage = teamsicon.subsample(50,50)
    teamsurl="https://go.microsoft.com/fwlink/p/?LinkID=2187327&clcid=0x409&culture=en-us&country=US"
    teamspath="downloads//teams.exe"
    teamsfile="downloads\\teams.exe"
    teams=ttk.Button(communicationsectionframe,image=teamsimage,text="Teams",width=10,compound=LEFT,command=lambda: [intcheck(),install(teamsurl,teamspath,teamsfile,"teams")])
    teams.grid(row=0,column=2)

    ##############skype###############

    skypeicon= PhotoImage(file = r"images\174869.png")
    skypeimage = skypeicon.subsample(12,12)
    skypeurl="https://go.skype.com/windows.desktop.download"
    skypepath="downloads//skype.exe"
    skypefile="downloads\\skype.exe"
    skype=ttk.Button(communicationsectionframe,image=skypeimage,text="Skype",width=10,compound=LEFT,command=lambda: [intcheck(),install(skypeurl,skypepath,skypefile,"skype")])
    skype.grid(row=0,column=4)

    ##############zoom###############

    zoomicon= PhotoImage(file = r"images\5e8ce423664eae0004085465.png")
    zoomimage = zoomicon.subsample(7,7)
    zoomurl="https://zoom.us/client/5.13.3.11494/ZoomInstallerFull.exe?archType=x64"
    zoompath="downloads//zoom.exe"
    zoomfile="downloads\\zoom.exe"
    zoom=ttk.Button(communicationsectionframe,image=zoomimage,text="Zoom",width=10,compound=LEFT,command=lambda: [intcheck(),install(zoomurl,zoompath,zoomfile,"zoom")])
    zoom.grid(row=0,column=6)

    ##############signal###############

    signalicon= PhotoImage(file = r"images\4423638.png")
    signalimage = signalicon.subsample(12,12)
    signalurl="https://updates.signal.org/desktop/signal-desktop-win-6.1.0.exe" 
    signalpath="downloads//signal.exe"
    signalfile="downloads\\signal.exe"
    signal=ttk.Button(communicationsectionframe,image=signalimage,text="Signal",width=10,compound=LEFT,command=lambda: [intcheck(),install(signalurl,signalpath,signalfile,"signal")])
    signal.grid(row=0,column=8)

    ##############slack###############

    slackicon= PhotoImage(file = r"images\2111615.png")
    slackimage = slackicon.subsample(12,12)
    slackurl="https://slack.com/intl/en-in/downloads/instructions/windows"
    slackpath="downloads//slack.exe"
    slackfile="downloads\\slack.exe"
    slack=ttk.Button(communicationsectionframe,image=slackimage,text="Slack",width=10,compound=LEFT,command=lambda: [intcheck(),install(slackurl,slackpath,slackfile,"slack")])
    slack.grid(row=0,column=10)

    ##############whatsapp###############

    whatsappicon= PhotoImage(file = r"images\1753788.png")
    whatsappimage = whatsappicon.subsample(12,12)
    whatsappurl="https://www.whatsapp.com/download"
    whatsapppath="downloads//whatsapp.exe"
    whatsappfile="downloads\\whatsapp.exe"
    whatsapp=ttk.Button(communicationsectionframe,image=whatsappimage,text="Whatsapp",width=10,compound=LEFT,command=lambda: [intcheck(),install(whatsappurl,whatsapppath,whatsappfile,"whatsapp")])
    whatsapp.grid(row=0,column=12)

    ##############telegram###############

    telegramicon= PhotoImage(file = r"images\telegram-logo-AD3D08A014-seeklogo.com.png")
    telegramimage = telegramicon.subsample(7,7)
    telegramurl="https://telegram.org/dl/desktop/win64"
    telegrampath="downloads//telegram.exe"
    telegramfile="downloads\\telegram.exe"
    telegram=ttk.Button(communicationsectionframe,image=telegramimage,text="Telegram",width=10,compound=LEFT,command=lambda: [intcheck(),install(telegramurl,telegrampath,telegramfile,"telegram")])
    telegram.grid(row=2,column=0)

    ##############viber###############

    vibericon= PhotoImage(file = r"images\2111705.png")
    viberimage = vibericon.subsample(12,12)
    viberurl="https://www.viber.com/download/"
    viberpath="downloads//viber.exe"
    viberfile="downloads\\viber.exe"
    viber=ttk.Button(communicationsectionframe,image=viberimage,text="Viber",width=10,compound=LEFT,command=lambda: [intcheck(),install(viberurl,viberpath,viberfile,"viber")])
    viber.grid(row=2,column=2)
    
    #############################################################development##################################################
    developmentsection=ttk.Label(second_frame,text="Development",font=("Segou UI variable",15))
    developmentsection.grid(row=4,column=0,pady=15,padx=15)

    developmentsectionframe= Frame(second_frame)
    developmentsectionframe.grid(row=5,column=0,pady=15,padx=15)

    spacing=ttk.Label(developmentsectionframe,text="         ")
    spacing.grid(row=0,column=1)
    spacing=ttk.Label(developmentsectionframe,text="         ")
    spacing.grid(row=0,column=3)
    spacing=ttk.Label(developmentsectionframe,text="         ")
    spacing.grid(row=0,column=5)
    spacing=ttk.Label(developmentsectionframe,text="         ")
    spacing.grid(row=0,column=7)
    spacing=ttk.Label(developmentsectionframe,text="         ")
    spacing.grid(row=0,column=9)
    spacing=ttk.Label(developmentsectionframe,text="         ")
    spacing.grid(row=0,column=11)
    spacing=ttk.Label(developmentsectionframe,text="         ")
    spacing.grid(row=1,column=0)

    ##############git###############

    giticon= PhotoImage(file = r"images\Git-Icon-1788C.png")
    gitimage = giticon.subsample(9,9)
    giturl="https://git-scm.com/download/win"
    gitpath="downloads//git.exe"
    gitfile="downloads\\git.exe"
    git=ttk.Button(developmentsectionframe,image=gitimage,text="Git",width=10,compound=LEFT,command=lambda: [intcheck(),install(giturl,gitpath,gitfile,"git")])
    git.grid(row=1,column=0)

    ##############githubdesktop###############

    githubdesktopicon= PhotoImage(file = r"images\768px-Github-desktop-logo-symbol.svg.png")
    githubdesktopimage = githubdesktopicon.subsample(18,18)
    githubdesktopurl="https://central.github.com/deployments/desktop/desktop/latest/win32"
    githubdesktoppath="downloads//githubdesktop.exe"
    githubdesktopfile="downloads\\githubdesktop.exe"
    githubdesktop=ttk.Button(developmentsectionframe,image=githubdesktopimage,text="Github Desktop",width=12,compound=LEFT,command=lambda: [intcheck(),install(githubdesktopurl,githubdesktoppath,githubdesktopfile,"githubdesktop")])
    githubdesktop.grid(row=1,column=2)

    ##############jetbrainstoolbox###############

    jetbrainstoolboxicon= PhotoImage(file = r"images\toolbox_logo_300x300.png")
    jetbrainstoolboximage = jetbrainstoolboxicon.subsample(7,7)
    jetbrainstoolboxurl="https://www.jetbrains.com/toolbox-app/download/download-thanks.html?platform=windows"
    jetbrainstoolboxpath="downloads//jetbrainstoolbox.exe"
    jetbrainstoolboxfile="downloads\\jetbrainstoolbox.exe"
    jetbrainstoolbox=ttk.Button(developmentsectionframe,image=jetbrainstoolboximage,text="Jetbrains Toolbox",width=13,compound=LEFT,command=lambda: [intcheck(),install(jetbrainstoolboxurl,jetbrainstoolboxpath,jetbrainstoolboxfile,"jetbrainstoolbox")])
    jetbrainstoolbox.grid(row=1,column=4)

    ##############python###############

    pythonicon= PhotoImage(file = r"images\5968350.png")
    pythonimage = pythonicon.subsample(12,12)
    pythonurl="https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe"
    pythonpath="downloads//python.exe"
    pythonfile="downloads\\python.exe"
    python=ttk.Button(developmentsectionframe,image=pythonimage,text="Python",width=10,compound=LEFT,command=lambda: [intcheck(),install(pythonurl,pythonpath,pythonfile,"python")])
    python.grid(row=1,column=6)

    ##############vscode###############

    vscodeicon= PhotoImage(file = r"images\Visual_Studio_Code_1.35_icon.svg.png")
    vscodeimage = vscodeicon.subsample(48,48)
    vscodeurl="https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user"
    vscodepath="downloads//vscode.exe"
    vscodefile="downloads\\vscode.exe"
    vscode=ttk.Button(developmentsectionframe,image=vscodeimage,text="VS Code",width=10,compound=LEFT,command=lambda: [intcheck(),install(vscodeurl,vscodepath,vscodefile,"vscode")])
    vscode.grid(row=1,column=8)

    ##############vscodium###############

    vscodiumicon= PhotoImage(file = r"images\i7zov9ca3ts71.png")
    vscodiumimage = vscodiumicon.subsample(24,24)
    vscodiumurl="https://github.com/VSCodium/vscodium/releases/download/1.74.2.22355/VSCodiumSetup-x64-1.74.2.22355.exe"
    vscodiumpath="downloads//vscodium.exe"
    vscodiumfile="downloads\\vscodium.exe"
    vscodium=ttk.Button(developmentsectionframe,image=vscodiumimage,text="VS Codium",width=10,compound=LEFT,command=lambda: [intcheck(),install(vscodiumurl,vscodiumpath,vscodiumfile,"vscodium")])
    vscodium.grid(row=1,column=10)

    ##############nodejs###############

    nodejsicon= PhotoImage(file = r"images\5968322.png")
    nodejsimage = nodejsicon.subsample(12,12)
    nodejsurl="https://nodejs.org/dist/v18.13.0/node-v18.13.0-x64.msi"
    nodejspath="downloads//nodejs.msi"
    nodejsfile="downloads\\nodejs.msi"
    nodejs=ttk.Button(developmentsectionframe,image=nodejsimage,text="Node JS",width=10,compound=LEFT,command=lambda: [intcheck(),install(nodejsurl,nodejspath,nodejsfile,"nodejs")])
    nodejs.grid(row=1,column=12)

    #############################################################utilities##################################################

    utilitiessection=ttk.Label(second_frame,text="Utilities",font=("Segou UI variable",15))
    utilitiessection.grid(row=6,column=0,pady=15,padx=15)

    utilitiessectionframe= Frame(second_frame)
    utilitiessectionframe.grid(row=7,column=0,pady=15,padx=15)

    spacing=ttk.Label(utilitiessectionframe,text="         ")
    spacing.grid(row=0,column=1)
    spacing=ttk.Label(utilitiessectionframe,text="         ")
    spacing.grid(row=0,column=3)
    spacing=ttk.Label(utilitiessectionframe,text="         ")
    spacing.grid(row=0,column=5)
    spacing=ttk.Label(utilitiessectionframe,text="         ")
    spacing.grid(row=0,column=7)
    spacing=ttk.Label(utilitiessectionframe,text="         ")
    spacing.grid(row=0,column=9)
    spacing=ttk.Label(utilitiessectionframe,text="         ")
    spacing.grid(row=0,column=11)
    spacing=ttk.Label(utilitiessectionframe,text="         ")
    spacing.grid(row=1,column=0)

    ##############################hwinfo########################
    hwinfoicon= PhotoImage(file = r"images\hwinfo-icon-512x512-8ybzko3v.png")
    hwinfoimage = hwinfoicon.subsample(12,12)
    hwinfourl="https://www.hwinfo.com/download/"
    hwinfopath="downloads//hwinfo.exe"
    hwinfofile="downloads\\hwinfoxe"
    hwinfo=ttk.Button(utilitiessectionframe,image=hwinfoimage,text="HW Info",width=10,compound=LEFT,command=lambda: [intcheck(),install(hwinfourl,hwinfopath,hwinfofile,"hwinfo")])
    hwinfo.grid(row=0,column=0)

    ##############################coretemp########################
    coretempicon= PhotoImage(file = r"images\34454443.png")
    coretempimage = coretempicon.subsample(7,7)
    coretempurl="https://www.alcpu.com/CoreTemp/Core-Temp-setup.exe"
    coretemppath="downloads//coretemp.exe"
    coretempfile="downloads\\coretemp.exe"
    coretemp=ttk.Button(utilitiessectionframe,image=coretempimage,text="Core Temp",width=10,compound=LEFT,command=lambda: [intcheck(),install(coretempurl,coretemppath,coretempfile,"coretemp")])
    coretemp.grid(row=0,column=2)

    ##############################sevenzip########################
    sevenzipicon= PhotoImage(file = r"images\png-clipart-logos-01-icons-and-7zip-512-7zip-icon-thumbnail.png")
    sevenzipimage = sevenzipicon.subsample(8,8)
    sevenzipurl="https://www.7-zip.org/a/7z2201-x64.exe"
    sevenzippath="downloads//sevenzip.exe"
    sevenzipfile="downloads\\sevenzip.exe"
    sevenzip=ttk.Button(utilitiessectionframe,image=sevenzipimage,text="7Zip",width=10,compound=LEFT,command=lambda: [intcheck(),install(sevenzipurl,sevenzippath,sevenzipfile,"sevenzip")])
    sevenzip.grid(row=0,column=4)

    ##############################anydesk########################
    anydeskicon= PhotoImage(file = r"images\unnamed.png")
    anydeskimage = anydeskicon.subsample(12,12)
    anydeskurl="https://anydesk.com/en/downloads/thank-you?dv=win_exe"
    anydeskpath="downloads//anydesk.exe"
    anydeskfile="downloads\\anydesk.exe"
    anydesk=ttk.Button(utilitiessectionframe,image=anydeskimage,text="Anydesk",width=10,compound=LEFT,command=lambda: [intcheck(),install(anydeskurl,anydeskpath,anydeskfile,"anydesk")])
    anydesk.grid(row=0,column=6)
    
    ##############################cpuz########################
    cpuzicon= PhotoImage(file = r"images\CPU-Z_Icon.svg.png")
    cpuzimage = cpuzicon.subsample(3,3)
    cpuzurl="https://download.cpuid.com/cpu-z/cpu-z_2.03-en.exe"
    cpuzpath="downloads//cpuz.exe"
    cpuzfile="downloads\\cpuz.exe"
    cpuz=ttk.Button(utilitiessectionframe,image=cpuzimage,text="CPU-Z",width=10,compound=LEFT,command=lambda: [intcheck(),install(cpuzurl,cpuzpath,cpuzfile,"cpuz")])
    cpuz.grid(row=0,column=8)

    ##############################etcher########################
    etchericon= PhotoImage(file = r"images\avatar.png")
    etcherimage = etchericon.subsample(6,6)
    etcherurl="https://github.com/balena-io/etcher/releases/download/v1.13.1/balenaEtcher-Setup-1.13.1.exe"
    etcherpath="downloads//etcher.exe"
    etcherfile="downloads\\etcher.exe"
    etcher=ttk.Button(utilitiessectionframe,image=etcherimage,text="Balena Etcher",width=10,compound=LEFT,command=lambda: [intcheck(),install(etcherurl,etcherpath,etcherfile,"etcher")])
    etcher.grid(row=0,column=10)
    
    ##############################gpuz########################
    gpuzicon= PhotoImage(file = r"images\gpu_z_icon_by_pitmankeks_de0lyld-fullview.png")
    gpuzimage = gpuzicon.subsample(12,12)
    gpuzurl="https://www.techspot.com/downloads/downloadnow/4452/?evp=ab945c9425fa6218cc4d5fadc33ecb42&file=4665"
    gpuzpath="downloads//gpuz.exe"
    gpuzfile="downloads\\gpuz.exe"
    gpuz=ttk.Button(utilitiessectionframe,image=gpuzimage,text="GPU-Z",width=10,compound=LEFT,command=lambda: [intcheck(),install(gpuzurl,gpuzpath,gpuzfile,"gpuz")])
    gpuz.grid(row=0,column=12)

    ################passwordmanager###########
    """
    passwordmanagericon= PhotoImage(file = r"images\1.png")
    passwordmanagerimage = passwordmanagericon.subsample(7,7)
    """
    passwordmanagerurl="https://github.com/VarunAdhityaGB/Password-Manager-GUI/releases/download/v.1.2/Password_Manager_v.1.2_Setup.exe"
    passwordmanagerpath="downloads//passwordmanager.exe"
    passwordmanagerfile="downloads\\passwordmanager.exe"
    passwordmanagerutility=ttk.Button(utilitiessectionframe,text="Password Manager",width=15,compound=LEFT,command=lambda: [intcheck(),install(passwordmanagerurl,passwordmanagerpath,passwordmanagerfile,"passwordmanager")])
    passwordmanagerutility.grid(row=2,column=0)

    ##############################revouninstaller########################
    revouninstallericon= PhotoImage(file = r"images\Revouninstallerpro_icon.png")
    revouninstallerimage = revouninstallericon.subsample(12,12)
    revouninstallerurl="https://www.revouninstaller.com/start-freeware-download/"
    revouninstallerpath="downloads//revouninstaller.exe"
    revouninstallerfile="downloads\\revouninstaller.exe"
    revouninstaller=ttk.Button(utilitiessectionframe,image=revouninstallerimage,text="Revo Uninstaller",width=12,compound=LEFT,command=lambda: [intcheck(),install(revouninstallerurl,revouninstallerpath,revouninstallerfile,"revouninstaller")])
    revouninstaller.grid(row=2,column=2)

    main.mainloop()

mainsplash.after(3000, mainwindow)
mainsplash.mainloop()