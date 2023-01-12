from tkinter import *
from urllib import request  
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk
import sv_ttk as sv
import os 
import requests

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
        req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64)',
           'Accept-Language': 'en-US,en;q=0.8',
           'Accept-Encoding': 'gzip,deflate,sdch',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Connection': 'keep-alive'
          })
        request.urlretrieve(req.full_url, path)
        """response = request.urlretrieve(url,path)
        """
        os.system(file)
        break

mainsplash = Tk()
sv.set_theme("dark")
mainsplash.overrideredirect(True)
app_width = 1024
app_height = 512
screenwidth = mainsplash.winfo_screenwidth()
screenheight = mainsplash.winfo_screenheight()
mainsplash.attributes("-alpha", 0.90)
x = (screenwidth / 2) - (app_width / 2)
y = (screenheight / 2) - (app_height / 2)

mainsplash.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
bg_image = ImageTk.PhotoImage(Image.open(r"images\softhub load.png"))
label1 = Label(mainsplash, image=bg_image)
label1.pack()

def mainwindow():
    main = Toplevel()
    s= ttk.Style()
    s.configure('.', font=('Segoe UI Variable', 10))
    mainsplash.withdraw()
    main.state('zoomed')
    screenwidth = main.winfo_screenwidth()
    screenheight = main.winfo_screenheight()
    app_width = screenwidth
    app_height = screenheight
    main.geometry(f'{app_width}x{app_height}')
    main.title("Softhub")
    main.tk.call('wm', 'iconphoto', main._w, ImageTk.PhotoImage(file='images\softhub.ico'))
    main.attributes("-alpha", 0.96)

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

    browser_frame = Frame(second_frame)
    browser_frame.grid(row=0 ,column=0,sticky=E+W)

    broser_frame2 = Frame(browser_frame)
    broser_frame2.pack(fill=X,side=BOTTOM)

    browsercanvas = Canvas(browser_frame)
    browsercanvas.pack(side=LEFT,fill=X,expand=1)

    x_scrollbar = ttk.Scrollbar(broser_frame2,orient=HORIZONTAL,command=browsercanvas.xview)
    x_scrollbar.pack(side=BOTTOM,fill=X)
    browsercanvas.configure(xscrollcommand=x_scrollbar.set)
    browsercanvas.bind("<Configure>",lambda e: browsercanvas.config(scrollregion= browsercanvas.bbox(ALL)))
    broser_frame3 = Frame(browsercanvas)
    browsercanvas.create_window((100,100),window= broser_frame3, anchor="nw")

    ########################################################browsers#######################################################

    browsersectionframe= Frame(broser_frame3)
    browsersectionframe.grid(row=0,column=0)

    browsersection=ttk.Label(browsersectionframe,text="Browsers",font=("Segou UI variable",18))
    browsersection.grid(row=0,column=1,ipady=15,ipadx=15)

    #############################spacing between each app##############################

    spacing=ttk.Label(browsersectionframe,text="       ")
    spacing.grid(row=0,column=0)
    spacing=ttk.Label(browsersectionframe,text="       ")
    spacing.grid(row=0,column=3)
    spacing=ttk.Label(browsersectionframe,text="       ")
    spacing.grid(row=0,column=5)
    spacing=ttk.Label(browsersectionframe,text="       ")
    spacing.grid(row=0,column=0)
    spacing=ttk.Label(browsersectionframe,text="       ")
    spacing.grid(row=0,column=7)
    spacing=ttk.Label(browsersectionframe,text="       ")
    spacing.grid(row=0,column=9)
    spacing=ttk.Label(browsersectionframe,text="       ")
    spacing.grid(row=0,column=11)
    spacing=ttk.Label(browsersectionframe,text="       ")
    spacing.grid(row=0,column=13)
    spacing=ttk.Label(browsersectionframe,text="       ")
    spacing.grid(row=0,column=15)

    ##############brave###############

    braveicon= PhotoImage(file = r"images\Brave_lion_icon.svg.png")
    braveimage = braveicon.subsample(20,20)
    braveurl="https://laptop-updates.brave.com/latest/winx64"
    bravepath="downloads//brave.exe"
    bravefile="downloads\\brave.exe"
    bravebrowser=ttk.Button(browsersectionframe,image=braveimage,text="        Brave\n\n ★★★★☆ 4.2 ",width=15,compound=LEFT,command=lambda: [intcheck(),install(braveurl,bravepath,bravefile,"brave browser")])
    bravebrowser.grid(row=0,column=2 ,ipady=30, ipadx=15)

    ##############firefox###############

    firefoxicon= PhotoImage(file = r"images\Firefox_logo,_2017.svg.png")
    firefoximage = firefoxicon.subsample(17,17)
    firefoxurl="https://download.mozilla.org/?product=firefox-stub&os=win&lang=en-US&attribution_code=c291cmNlPXd3dy5nb29nbGUuY29tJm1lZGl1bT1yZWZlcnJhbCZjYW1wYWlnbj0obm90IHNldCkmY29udGVudD0obm90IHNldCkmZXhwZXJpbWVudD0obm90IHNldCkmdmFyaWF0aW9uPShub3Qgc2V0KSZ1YT1jaHJvbWUmdmlzaXRfaWQ9KG5vdCBzZXQp&attribution_sig=3466763a646381f4d23891a79de5b2c5da57cff9698bd5c185e938b48ed303e6"
    firefoxpath="downloads//firefox.exe"
    firefoxfile="downloads\\firefox.exe"
    firefoxbrowser=ttk.Button(browsersectionframe,image=firefoximage,text="       Firefox\n\n ★★★★☆ 4",width=10,compound=LEFT,command=lambda: [intcheck(),install(firefoxurl,firefoxpath,firefoxfile,"firefox browser")])
    firefoxbrowser.grid(row=0,column=4,ipady=30, ipadx=15)

    ##############librewolf###############

    librewolficon= PhotoImage(file = r"images\LibreWolf_icon.svg.png")
    librewolfimage = librewolficon.subsample(30,30)
    librewolfurl="https://gitlab.com/librewolf-community/browser/windows/uploads/8ca22cbdb72aebdb6e1dc7f096fcf65b/librewolf-108.0.1-1.en-US.win64-setup.exe"
    librewolfpath="downloads//librewolf.exe"
    librewolffile="downloads\\librewolf.exe"
    librewolfbrowser=ttk.Button(browsersectionframe,image=librewolfimage,text="     Librewolf\n\n ★★★★☆ 4",width=10,compound=LEFT,command=lambda: [intcheck(),install(librewolfurl,librewolfpath,librewolffile,"librewolf browser")])
    librewolfbrowser.grid(row=0,column=6,ipady=30, ipadx=15)

    ##############tor browser###############

    toricon= PhotoImage(file = r"images\Tor_Browser_icon.svg.png")
    torimage = toricon.subsample(17,17)
    torurl="https://www.torproject.org/dist/torbrowser/12.0.1/torbrowser-install-win64-12.0.1_ALL.exe"
    torpath="downloads//tor.exe"
    torfile="downloads\\tor.exe"
    torbrowser=ttk.Button(browsersectionframe,image=torimage,text="        Tor \n\n ★★★☆☆ 3.5",width=10,compound=LEFT,command=lambda: [intcheck(),install(torurl,torpath,torfile,"tor browser")])
    torbrowser.grid(row=0,column=8,ipady=30, ipadx=15)

    ##############vivaldi browser###############

    vivaldiicon= PhotoImage(file = r"images\Vivaldi_web_browser_logo.svg.png")
    vivaldiimage = vivaldiicon.subsample(14,14)
    vivaldiurl="https://downloads.vivaldi.com/stable/Vivaldi.5.6.2867.50.x64.exe"
    vivaldipath="downloads//vivaldi.exe"
    vivaldifile="downloads\\vivaldi.exe"
    vivaldibrowser=ttk.Button(browsersectionframe,image=vivaldiimage,text="     Vivaldi \n\n ★★★☆☆ 3.5",width=10,compound=LEFT,command=lambda: [intcheck(),install(vivaldiurl,vivaldipath,vivaldifile,"vivaldi browser")])
    vivaldibrowser.grid(row=0,column=10,ipady=30, ipadx=15)

    #############chrome##############

    chromeicon= PhotoImage(file = r"images\Google_Chrome_icon_(February_2022).svg.png")
    chromeimage = chromeicon.subsample(30,30)
    chromeurl="https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B6F291CBF-DCB7-0B2B-FC28-010EF4CE0BB3%7D%26lang%3Den%26browser%3D4%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26brand%3DYTUH%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe"
    chromepath="downloads//chrome.exe"
    chromefile="downloads\\chrome.exe"
    chromebrowser=ttk.Button(browsersectionframe,image=chromeimage,text="     Chrome \n\n ★★★★☆ 4",width=10,compound=LEFT,command=lambda: [intcheck(),install(chromeurl,chromepath,chromefile,"chrome browser")])
    chromebrowser.grid(row=0,column=12,ipady=30, ipadx=15)

    #############msedge##############

    msedgeicon= PhotoImage(file = r"images\Microsoft_Edge_logo_(2019).svg.png")
    msedgeimage = msedgeicon.subsample(7,7)
    msedgeurl="https://c2rsetup.officeapps.live.com/c2r/downloadEdge.aspx?platform=Default&source=EdgeStablePage&Channel=Stable&language=en&brand=M100"
    msedgepath="downloads//msedge.exe"
    msedgefile="downloads\\msedge.exe"
    msedgebrowser=ttk.Button(browsersectionframe,image=msedgeimage,text="     MS Edge \n\n ★★★☆☆ 3.6",width=10,compound=LEFT,command=lambda: [intcheck(),install(msedgeurl,msedgepath,msedgefile,"msedge browser")])
    msedgebrowser.grid(row=0,column=14,ipady=30, ipadx=15)


    communication_frame = Frame(second_frame)
    communication_frame.grid(row=1 ,column=0,sticky=E+W)

    communication_frame2 = Frame(communication_frame)
    communication_frame2.pack(fill=X,side=BOTTOM)

    communicationcanvas = Canvas(communication_frame)
    communicationcanvas.pack(side=LEFT,fill=X,expand=1)

    x_scrollbar = ttk.Scrollbar(communication_frame2,orient=HORIZONTAL,command=communicationcanvas.xview)
    x_scrollbar.pack(side=BOTTOM,fill=X)
    communicationcanvas.configure(xscrollcommand=x_scrollbar.set)
    communicationcanvas.bind("<Configure>",lambda e: communicationcanvas.config(scrollregion= communicationcanvas.bbox(ALL)))
    communication_frame3 = Frame(communicationcanvas)
    communicationcanvas.create_window((100,100),window= communication_frame3, anchor="nw")

    #############################################################communication##################################################
    communicationsectionframe= Frame(communication_frame3)
    communicationsectionframe.grid(row=1,column=0)

    communicationsection=ttk.Label(communicationsectionframe,text="Communication",font=("Segou UI variable",18))
    communicationsection.grid(row=0,column=0,pady=15,padx=15)

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
    spacing.grid(row=1,column=13)
    spacing=ttk.Label(communicationsectionframe,text="         ")
    spacing.grid(row=1,column=15)


    ##############discord###############

    discordicon= PhotoImage(file = r"images\636e0a6a49cf127bf92de1e2_icon_clyde_blurple_RGB.png")
    discordimage = discordicon.subsample(8,8)
    discordurl="https://sp-downloads.digitaltrends.com/eca/be8/6b6c0b20c6314a005ffa234ed54d4e2f24/DiscordSetup.exe?signature=c5b5bd3297e936683e09721f070bfb92&expires=1673401556&url=https%3A%2F%2Fdownloads.digitaltrends.com%2Fdiscord%2Fwindows&filename=DiscordSetup.exe" 
    discordpath="downloads//discord.exe"
    discordfile="downloads\\discord.exe"
    discord=ttk.Button(communicationsectionframe,image=discordimage,text="      Discord \n\n ★★★★☆ 4.5",width=9,compound=LEFT,command=lambda: [intcheck(),install(discordurl,discordpath,discordfile,"discord")])
    discord.grid(row=0,column=2,ipady=30, ipadx=15)

    ##############teams###############

    teamsicon= PhotoImage(file = r"images\Microsoft_Office_Teams_(2018–present).svg.png")
    teamsimage = teamsicon.subsample(35,35)
    teamsurl="https://go.microsoft.com/fwlink/p/?LinkID=2187327&clcid=0x409&culture=en-us&country=US"
    teamspath="downloads//teams.exe"
    teamsfile="downloads\\teams.exe"
    teams=ttk.Button(communicationsectionframe,image=teamsimage,text="      Teams \n\n ★★★☆☆ 3.5",width=10,compound=LEFT,command=lambda: [intcheck(),install(teamsurl,teamspath,teamsfile,"teams")])
    teams.grid(row=0,column=4,ipady=30, ipadx=15)

    ##############skype###############

    skypeicon= PhotoImage(file = r"images\174869.png")
    skypeimage = skypeicon.subsample(9,9)
    skypeurl="https://go.skype.com/windows.desktop.download"
    skypepath="downloads//skype.exe"
    skypefile="downloads\\skype.exe"
    skype=ttk.Button(communicationsectionframe,image=skypeimage,text="      Skype \n\n ★★★★☆ 4.5",width=10,compound=LEFT,command=lambda: [intcheck(),install(skypeurl,skypepath,skypefile,"skype")])
    skype.grid(row=0,column=6,ipady=30, ipadx=15)

    ##############zoom###############

    zoomicon= PhotoImage(file = r"images\5e8ce423664eae0004085465.png")
    zoomimage = zoomicon.subsample(5,5)
    zoomurl="https://zoom.us/client/5.13.3.11494/ZoomInstallerFull.exe?archType=x64"
    zoompath="downloads//zoom.exe"
    zoomfile="downloads\\zoom.exe"
    zoom=ttk.Button(communicationsectionframe,image=zoomimage,text="        Zoom \n\n ★★★★☆ 4.5",width=10,compound=LEFT,command=lambda: [intcheck(),install(zoomurl,zoompath,zoomfile,"zoom")])
    zoom.grid(row=0,column=8,ipady=30, ipadx=15)

    ##############slack###############

    slackicon= PhotoImage(file = r"images\2111615.png")
    slackimage = slackicon.subsample(9,9)
    slackurl="https://downloads.slack-edge.com/releases/windows/4.29.149/prod/x64/SlackSetup.exe"
    slackpath="downloads//slack.exe"
    slackfile="downloads\\slack.exe"
    slack=ttk.Button(communicationsectionframe,image=slackimage,text="      Slack \n\n ★★★★☆ 4.5",width=10,compound=LEFT,command=lambda: [intcheck(),install(slackurl,slackpath,slackfile,"slack")])
    slack.grid(row=0,column=10,ipady=30, ipadx=15)

    ##############telegram###############

    telegramicon= PhotoImage(file = r"images\telegram-logo-AD3D08A014-seeklogo.com.png")
    telegramimage = telegramicon.subsample(5,5)
    telegramurl="https://telegram.org/dl/desktop/win64"
    telegrampath="downloads//telegram.exe"
    telegramfile="downloads\\telegram.exe"
    telegram=ttk.Button(communicationsectionframe,image=telegramimage,text="      Telegram \n\n ★★★☆☆ 3.5",width=10,compound=LEFT,command=lambda: [intcheck(),install(telegramurl,telegrampath,telegramfile,"telegram")])
    telegram.grid(row=0,column=12,ipady=30, ipadx=15)

    ##############viber###############

    vibericon= PhotoImage(file = r"images\2111705.png")
    viberimage = vibericon.subsample(9,9)
    viberurl="https://download.cdn.viber.com/desktop/windows/ViberSetup.exe"
    viberpath="downloads//viber.exe"
    viberfile="downloads\\viber.exe"
    viber=ttk.Button(communicationsectionframe,image=viberimage,text="      Viber \n\n ★★★★☆ 4.5",width=10,compound=LEFT,command=lambda: [intcheck(),install(viberurl,viberpath,viberfile,"viber")])
    viber.grid(row=0,column=14,ipady=30, ipadx=15)
    
    development_frame = Frame(second_frame)
    development_frame.grid(row=2 ,column=0,sticky=E+W)

    development_frame2 = Frame(development_frame)
    development_frame2.pack(fill=X,side=BOTTOM)

    developmentcanvas = Canvas(development_frame)
    developmentcanvas.pack(side=LEFT,fill=X,expand=1)

    x_scrollbar = ttk.Scrollbar(development_frame2,orient=HORIZONTAL,command=developmentcanvas.xview)
    x_scrollbar.pack(side=BOTTOM,fill=X)
    developmentcanvas.configure(xscrollcommand=x_scrollbar.set)
    developmentcanvas.bind("<Configure>",lambda e: developmentcanvas.config(scrollregion= developmentcanvas.bbox(ALL)))
    development_frame3 = Frame(developmentcanvas)
    developmentcanvas.create_window((100,100),window= development_frame3, anchor="nw")
    #############################################################development##################################################
    
    developmentsectionframe= Frame(development_frame3)
    developmentsectionframe.grid(row=2,column=0,pady=15,padx=15)

    developmentsection=ttk.Label(developmentsectionframe,text="Development",font=("Segou UI variable",18))
    developmentsection.grid(row=0,column=0,pady=15,padx=15)

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
    spacing.grid(row=0,column=13)
    spacing=ttk.Label(developmentsectionframe,text="         ")
    spacing.grid(row=0,column=15)
    spacing=ttk.Label(developmentsectionframe,text="         ")
    spacing.grid(row=0,column=17)
    spacing=ttk.Label(developmentsectionframe,text="         ")
    spacing.grid(row=0,column=19)
    spacing=ttk.Label(developmentsectionframe,text="         ")
    spacing.grid(row=0,column=21)
    ##############git###############

    giticon= PhotoImage(file = r"images\Git-Icon-1788C.png")
    gitimage = giticon.subsample(6,6)
    giturl="https://objects.githubusercontent.com/github-production-release-asset-2e65be/23216272/937f230c-9f0d-4a46-bba3-22d19dc651c1?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20230110%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230110T170918Z&X-Amz-Expires=300&X-Amz-Signature=963ec20d9e83e42881e97530dce71223100da3a33d9e3ad895dc9cd752ce904f&X-Amz-SignedHeaders=host&actor_id=112751363&key_id=0&repo_id=23216272&response-content-disposition=attachment%3B%20filename%3DGit-2.39.0.2-64-bit.exe&response-content-type=application%2Foctet-stream"
    gitpath="downloads//git.exe"
    gitfile="downloads\\git.exe"
    git=ttk.Button(developmentsectionframe,image=gitimage,text="      Git",width=10,compound=LEFT,command=lambda: [intcheck(),install(giturl,gitpath,gitfile,"git")])
    git.grid(row=0,column=2,ipady=30, ipadx=15)

    ##############githubdesktop###############

    githubdesktopicon= PhotoImage(file = r"images\768px-Github-desktop-logo-symbol.svg.png")
    githubdesktopimage = githubdesktopicon.subsample(12,12)
    githubdesktopurl="https://central.github.com/deployments/desktop/desktop/latest/win32"
    githubdesktoppath="downloads//githubdesktop.exe"
    githubdesktopfile="downloads\\githubdesktop.exe"
    githubdesktop=ttk.Button(developmentsectionframe,image=githubdesktopimage,text="    Github Desktop",width=12,compound=LEFT,command=lambda: [intcheck(),install(githubdesktopurl,githubdesktoppath,githubdesktopfile,"githubdesktop")])
    githubdesktop.grid(row=0,column=4,ipady=30, ipadx=15)

    ##############jetbrainstoolbox###############

    jetbrainstoolboxicon= PhotoImage(file = r"images\toolbox_logo_300x300.png")
    jetbrainstoolboximage = jetbrainstoolboxicon.subsample(5,5)
    jetbrainstoolboxurl="https://download.jetbrains.com/toolbox/jetbrains-toolbox-1.27.2.13801.exe"
    jetbrainstoolboxpath="downloads//jetbrainstoolbox.exe"
    jetbrainstoolboxfile="downloads\\jetbrainstoolbox.exe"
    jetbrainstoolbox=ttk.Button(developmentsectionframe,image=jetbrainstoolboximage,text="Jetbrains Toolbox",width=13,compound=LEFT,command=lambda: [intcheck(),install(jetbrainstoolboxurl,jetbrainstoolboxpath,jetbrainstoolboxfile,"jetbrainstoolbox")])
    jetbrainstoolbox.grid(row=0,column=6,ipady=30, ipadx=15)

    ##############python###############

    pythonicon= PhotoImage(file = r"images\5968350.png")
    pythonimage = pythonicon.subsample(9,9)
    pythonurl="https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe"
    pythonpath="downloads//python.exe"
    pythonfile="downloads\\python.exe"
    python=ttk.Button(developmentsectionframe,image=pythonimage,text="  Python",width=10,compound=LEFT,command=lambda: [intcheck(),install(pythonurl,pythonpath,pythonfile,"python")])
    python.grid(row=0,column=8,ipady=30, ipadx=15)

    ##############vscode###############

    vscodeicon= PhotoImage(file = r"images\Visual_Studio_Code_1.35_icon.svg.png")
    vscodeimage = vscodeicon.subsample(36,36)
    vscodeurl="https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user"
    vscodepath="downloads//vscode.exe"
    vscodefile="downloads\\vscode.exe"
    vscode=ttk.Button(developmentsectionframe,image=vscodeimage,text="  VS Code",width=10,compound=LEFT,command=lambda: [intcheck(),install(vscodeurl,vscodepath,vscodefile,"vscode")])
    vscode.grid(row=0,column=10,ipady=30, ipadx=15)

    ##############vscodium###############

    vscodiumicon= PhotoImage(file = r"images\i7zov9ca3ts71.png")
    vscodiumimage = vscodiumicon.subsample(18,18)
    vscodiumurl="https://github.com/VSCodium/vscodium/releases/download/1.74.2.22355/VSCodiumSetup-x64-1.74.2.22355.exe"
    vscodiumpath="downloads//vscodium.exe"
    vscodiumfile="downloads\\vscodium.exe"
    vscodium=ttk.Button(developmentsectionframe,image=vscodiumimage,text="  VS Codium",width=10,compound=LEFT,command=lambda: [intcheck(),install(vscodiumurl,vscodiumpath,vscodiumfile,"vscodium")])
    vscodium.grid(row=0,column=12,ipady=30, ipadx=15)

    ##############nodejs###############

    nodejsicon= PhotoImage(file = r"images\5968322.png")
    nodejsimage = nodejsicon.subsample(9,9)
    nodejsurl="https://nodejs.org/dist/v18.13.0/node-v18.13.0-x64.msi"
    nodejspath="downloads//nodejs.msi"
    nodejsfile="downloads\\nodejs.msi"
    nodejs=ttk.Button(developmentsectionframe,image=nodejsimage,text="  Node JS",width=10,compound=LEFT,command=lambda: [intcheck(),install(nodejsurl,nodejspath,nodejsfile,"nodejs")])
    nodejs.grid(row=0,column=14,ipady=30, ipadx=15)

    ##############rust###############

    rusticon= PhotoImage(file = r"images\Rust_programming_language_black_logo.svg.png")
    rustimage = rusticon.subsample(36,36)
    rusturl="https://static.rust-lang.org/rustup/dist/x86_64-pc-windows-msvc/rustup-init.exe"
    rustpath="downloads//rust.exe"
    rustfile="downloads\\rust.exe"
    rust=ttk.Button(developmentsectionframe,image=rustimage,text="     Rust",width=10,compound=LEFT,command=lambda: [intcheck(),install(rusturl,rustpath,rustfile,"Rust")])
    rust.grid(row=0,column=16,ipady=30, ipadx=15)

    ##############visualstudio###############

    vsstudioicon= PhotoImage(file = r"images\Visual_Studio_Icon_2022.svg.png")
    vsstudioimage = vsstudioicon.subsample(36,36)
    vsstudiourl=" https://c2rsetup.officeapps.live.com/c2r/downloadVS.aspx?sku=community&channel=Release&version=VS2022&source=VSLandingPage&includeRecommended=true&cid=2030:7c3d140c71b14b52b67aef7b3a3a604c"
    vsstudiopath="downloads//vsstudio.exe"
    vsstudiofile="downloads\\vsstudio.exe"
    vsstudio=ttk.Button(developmentsectionframe,image=vsstudioimage,text="Visual Studio 2022",width=14,compound=LEFT,command=lambda: [intcheck(),install(vsstudiourl,vsstudiopath,vsstudiofile,"vs studio 2022")])
    vsstudio.grid(row=0,column=18,ipady=30, ipadx=15)

    ##############sublime###############

    sublimeicon= PhotoImage(file = r"images\download.png")
    sublimeimage = sublimeicon.subsample(4,4)
    sublimeurl="https://download.sublimetext.com/sublime_text_build_4143_x64_setup.exe"
    sublimepath="downloads//sublime.exe"
    sublimefile="downloads\\sublime.exe"
    sublime=ttk.Button(developmentsectionframe,image=sublimeimage,text="    Sublime",width=10,compound=LEFT,command=lambda: [intcheck(),install(sublimeurl,sublimepath,sublimefile,"sublime")])
    sublime.grid(row=0,column=20,ipady=30, ipadx=15)


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
    hwinfourl="https://download.fosshub.com/Protected/expiretime=1673420828;badurl=aHR0cHM6Ly93d3cuZm9zc2h1Yi5jb20vSFdpTkZPLmh0bWw=/5f861ee14a1074acf7d825c276f32ba624ec19341942bd9c155fef16d2305d85/5b969867e5c78775cb187a52/639055157bcd531cda461531/hwi_734.exe"
    hwinfopath="downloads//hwinfo.exe"
    hwinfofile="downloads\\hwinfo.exe"
    hwinfo=ttk.Button(utilitiessectionframe,image=hwinfoimage,text="HW Info",width=10,compound=LEFT,command=lambda: [intcheck(),install(hwinfourl,hwinfopath,hwinfofile,"hwinfo")])
    hwinfo.grid(row=0,column=0)

    ##############################coretemp########################
    coretempicon= PhotoImage(file = r"images\34454443.png")
    coretempimage = coretempicon.subsample(7,7)
    coretempurl="https://files01.tchspt.com/temp/Core-Temp-setup.exe"
    coretemppath="downloads//coretemp.exe"
    coretempfile="downloads\\coretemp.exe"
    coretemp=ttk.Button(utilitiessectionframe,image=coretempimage,text="Core Temp",width=10,compound=LEFT,command=lambda: [intcheck(),install(coretempurl,coretemppath,coretempfile,"coretemp")])
    coretemp.grid(row=0,column=2)

    ##############################sevenzip########################
    sevenzipicon= PhotoImage(file = r"images\png-clipart-logos-01-icons-and-7zip-512-7zip-icon-thumbnail.png")
    sevenzipimage = sevenzipicon.subsample(8,8)
    sevenzipurl="https://www.7-zip.org/a/7z2201-x64.exe"
    sevenzippath="downloads//7zip.exe"
    sevenzipfile="downloads\\7zip.exe"
    sevenzip=ttk.Button(utilitiessectionframe,image=sevenzipimage,text="7Zip",width=10,compound=LEFT,command=lambda: [intcheck(),install(sevenzipurl,sevenzippath,sevenzipfile,"sevenzip")])
    sevenzip.grid(row=0,column=4)

    ##############################anydesk########################
    anydeskicon= PhotoImage(file = r"images\unnamed.png")
    anydeskimage = anydeskicon.subsample(12,12)
    anydeskurl="https://download.anydesk.com/AnyDesk.exe"
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
    gpuzurl="https://files1.majorgeeks.com/10afebdbffcd4742c81a3cb0f6ce4092156b4375/video/GPU-Z.2.52.0.exe"
    gpuzpath="downloads//gpuz.exe"
    gpuzfile="downloads\\gpuz.exe"
    gpuz=ttk.Button(utilitiessectionframe,image=gpuzimage,text="GPU-Z",width=10,compound=LEFT,command=lambda: [intcheck(),install(gpuzurl,gpuzpath,gpuzfile,"gpuz")])
    gpuz.grid(row=0,column=12)

    ##############################revouninstaller########################
    revouninstallericon= PhotoImage(file = r"images\Revouninstallerpro_icon.png")
    revouninstallerimage = revouninstallericon.subsample(12,12)
    revouninstallerurl="https://www.revouninstaller.com/start-freeware-download/"
    revouninstallerpath="downloads//revouninstaller.exe"
    revouninstallerfile="downloads\\revouninstaller.exe"
    revouninstaller=ttk.Button(utilitiessectionframe,image=revouninstallerimage,text="Revo Uninstaller",width=12,compound=LEFT,command=lambda: [intcheck(),install(revouninstallerurl,revouninstallerpath,revouninstallerfile,"revouninstaller")])
    revouninstaller.grid(row=2,column=0)

    ##############################powertoys########################
    powertoysicon= PhotoImage(file = r"images\2020_PowerToys_Icon.svg.png")
    powertoysimage = powertoysicon.subsample(48,48)
    powertoysurl="https://github.com/microsoft/PowerToys/releases/download/v0.66.0/PowerToysSetup-0.66.0-x64.exe"
    powertoyspath="downloads//powertoys.exe"
    powertoysfile="downloads\\powertoys.exe"
    powertoys=ttk.Button(utilitiessectionframe,image=powertoysimage,text="Powertoys",width=12,compound=LEFT,command=lambda: [intcheck(),install(powertoysurl,powertoyspath,powertoysfile,"powertoys")])
    powertoys.grid(row=2,column=2)

    ##############################autohotkey########################
    autohotkeyicon= PhotoImage(file = r"images\sBnPQRG.png")
    autohotkeyimage = autohotkeyicon.subsample(6,6)
    autohotkeyurl="https://www.autohotkey.com/download/ahk-v2.exe"
    autohotkeypath="downloads//autohotkey.exe"
    autohotkeyfile="downloads\\autohotkey.exe"
    autohotkey=ttk.Button(utilitiessectionframe,image=autohotkeyimage,text="Autohotkey",width=12,compound=LEFT,command=lambda: [intcheck(),install(autohotkeyurl,autohotkeypath,autohotkeyfile,"autohotkey")])
    autohotkey.grid(row=2,column=4)

    ##############################bitwarden########################
    bitwardenicon= PhotoImage(file = r"images\1200x630bb.png")
    bitwardenimage = bitwardenicon.subsample(16,16)
    bitwardenurl="https://objects.githubusercontent.com/github-production-release-asset-2e65be/53538899/97993fce-af92-400b-b5c8-c77f2382da49?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20230110%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230110T182412Z&X-Amz-Expires=300&X-Amz-Signature=838086e218d4425ad8ddc247822e0a0b6d6c37230c36f91a9d96444bdef95bf8&X-Amz-SignedHeaders=host&actor_id=112751363&key_id=0&repo_id=53538899&response-content-disposition=attachment%3B%20filename%3DBitwarden-Installer-2022.12.0.exe&response-content-type=application%2Foctet-stream"
    bitwardenpath="downloads//bitwarden.exe"
    bitwardenfile="downloads\\bitwarden.exe"
    bitwarden=ttk.Button(utilitiessectionframe,image=bitwardenimage,text="Bitwarden",width=12,compound=LEFT,command=lambda: [intcheck(),install(bitwardenurl,bitwardenpath,bitwardenfile,"bitwarden")])
    bitwarden.grid(row=2,column=6)

    ##############################everythingsearch########################
    everythingsearchicon= PhotoImage(file = r"images\dbc1fc0d2b9e238f5863eb19ef214629.png")
    everythingsearchimage = everythingsearchicon.subsample(6,6)
    everythingsearchurl="https://www.voidtools.com/Everything-1.4.1.1022.x86-Setup.exe"
    everythingsearchpath="downloads//everythingsearch.exe"
    everythingsearchfile="downloads\\everythingsearch.exe"
    everythingsearch=ttk.Button(utilitiessectionframe,image=everythingsearchimage,text="Everything search",width=14,compound=LEFT,command=lambda: [intcheck(),install(everythingsearchurl,everythingsearchpath,everythingsearchfile,"everythingsearch")])
    everythingsearch.grid(row=2,column=8)

    ################passwordmanager###########
    passwordmanagericon= PhotoImage(file = r"images\b8ac5e46-1a16-448b-9a12-bf597a95d173.png")
    passwordmanagerimage = passwordmanagericon.subsample(14,14)
    passwordmanagerurl="https://github.com/VarunAdhityaGB/Password-Manager-GUI/releases/download/v.1.2/Password_Manager_v.1.2_Setup.exe"
    passwordmanagerpath="downloads//passwordmanager.exe"
    passwordmanagerfile="downloads\\passwordmanager.exe"
    passwordmanagerutility=ttk.Button(utilitiessectionframe,image=passwordmanagerimage,text="Password Manager",width=15,compound=LEFT,command=lambda: [intcheck(),install(passwordmanagerurl,passwordmanagerpath,passwordmanagerfile,"passwordmanager")])
    passwordmanagerutility.grid(row=2,column=10)

    ################flux###########
    fluxicon= PhotoImage(file = r"images\flux-icon-big.png")
    fluximage = fluxicon.subsample(6,6)
    fluxurl="https://justgetflux.com/dlwin.html"
    fluxpath="downloads//flux.exe"
    fluxfile="downloads\\flux.exe"
    fluxutility=ttk.Button(utilitiessectionframe,image=fluximage,text="Flux",width=12,compound=LEFT,command=lambda: [intcheck(),install(fluxurl,fluxpath,fluxfile,"flux")])
    fluxutility.grid(row=2,column=12)

    main.mainloop()

mainsplash.after(3000, mainwindow)
mainsplash.mainloop()