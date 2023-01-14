from tkinter import *
from urllib import request  
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk
import sv_ttk as sv
import os 
import requests
from ctypes import windll

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
        
    global close_button 
    global expand_button 
    global minimize_button

    main = Toplevel()
    s= ttk.Style()
    s.configure('.', font=('Segoe UI Variable', 10))
    mainsplash.withdraw()
    screenwidth = main.winfo_screenwidth()
    screenheight = main.winfo_screenheight()
    app_height = int(screenheight) - 48
    main.geometry(f'{screenwidth}x{app_height}+0+0')
    main.title("Softhub")
    main.tk.call('wm', 'iconphoto', main._w, ImageTk.PhotoImage(file='images\softhub.ico'))
    main.attributes("-alpha", 0.96)
    main.overrideredirect(True)
    main.minimized = False 
    main.maximized = False    
    LGRAY = '#3e4042' # button color 
    RGRAY = '#1c1c1c' # title bar color  
    DGRAY = '#1c1c1c' # window background color 
    title_bar = Frame(main, bg=RGRAY, relief='raised', bd=0,highlightthickness=0)

    def set_appwindow(mainWindow): # to display the window icon on the taskbar, 
                               # even when using main.overrideredirect(True
    # Some WindowsOS styles, required for task bar integration
        GWL_EXSTYLE = -20
        WS_EX_APPWINDOW = 0x00040000
        WS_EX_TOOLWINDOW = 0x00000080
        # Magic
        hwnd = windll.user32.GetParent(mainWindow.winfo_id())
        stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
        stylew = stylew & ~WS_EX_TOOLWINDOW
        stylew = stylew | WS_EX_APPWINDOW
        res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)
    
        mainWindow.wm_withdraw()
        mainWindow.after(10, lambda: mainWindow.wm_deiconify())
        

    def minimize_me():
        main.attributes("-alpha",0) # so you can't see the window when its minimized
        main.minimized = True       


    def deminimize(event):

        main.focus() 
        main.attributes("-alpha",1) # so you can see the window when is not minimized
        if main.minimized == True:
            main.minimized = False                              
        

    def maximize_me():

        if main.maximized == False: # if the window was not maximized
            main.normal_size = main.geometry()
            expand_button.config(text="  🗗  ")
            main.geometry(f"{main.winfo_screenwidth()}x{main.winfo_screenheight()}+0+0")
            main.maximized = not main.maximized 
            #maximized
        
        else: # if the window was maximized
            expand_button.config(text="  ◻  ")
            main.geometry(main.normal_size)
            main.maximized = not main.maximized
            #not maximized
    
    close_button = Button(title_bar, text='  ✕  ', command=main.destroy,bg=RGRAY,padx=2,pady=2,font=("calibri", 13),bd=0,fg='white',highlightthickness=0)
    expand_button = Button(title_bar, text='  ◻  ', command=maximize_me,bg=RGRAY,padx=2,pady=2,bd=0,fg='white',font=("calibri", 13),highlightthickness=0)
    minimize_button = Button(title_bar, text='  —  ',command=minimize_me,bg=RGRAY,padx=2,pady=2,bd=0,fg='white',font=("calibri", 13),highlightthickness=0)
    title_bar_title = Label(title_bar, text="Softhub", bg=RGRAY,bd=0,fg='white',font=("helvetica", 10),highlightthickness=0)

    # main frame
    window = Frame(main, bg=DGRAY,highlightthickness=0)

    # pack the widgets
    title_bar.pack(fill=X)
    close_button.pack(side=RIGHT,ipadx=7,ipady=1)
    expand_button.pack(side=RIGHT,ipadx=7,ipady=1)
    minimize_button.pack(side=RIGHT,ipadx=7,ipady=1)
    appicon= PhotoImage(file = r"images\softhuḃicon.png")
    appicon = appicon.subsample(6,6)
    label = Label(title_bar,image=appicon)
    label.pack(side=LEFT)
    title_bar_title.pack(side=LEFT, padx=10)
    window.pack(expand=1, fill=BOTH) 
    searchentry= ttk.Entry(title_bar,width=30)
    searchentry.place(relx=0.41,rely=0.24)
    searchicon= PhotoImage(file = r"images\search.png")
    searchimage = searchicon.subsample(40,40)
    searchbutton =ttk.Button(title_bar,image=searchimage)
    searchbutton.place(relx=0.605,rely=0.24)

    # binding title bar motion to the move window fn.

    def changex_on_hovering(event):
        global close_button
        close_button['bg']='red' 
        
    def returnx_to_normalstate(event):
        global close_button
        close_button['bg']=RGRAY
        
    def change_size_on_hovering(event):
        global expand_button
        expand_button['bg']=LGRAY
        
    def return_size_on_hovering(event):
        global expand_button
        expand_button['bg']=RGRAY
        
    def changem_size_on_hovering(event):
        global minimize_button
        minimize_button['bg']=LGRAY
        
    def returnm_size_on_hovering(event):
        global minimize_button
        minimize_button['bg']=RGRAY
    
    def get_pos(event): # this is executed when the title bar is clicked to move the window
        if main.maximized == False:
            xwin = main.winfo_x()
            ywin = main.winfo_y()
            startx = event.x_root
            starty = event.y_root
            ywin = ywin - starty
            xwin = xwin - startx

            def move_window(event): # runs when window is dragged
                main.config(cursor="fleur")
                main.geometry(f'+{event.x_root + xwin}+{event.y_root + ywin}')

            def release_window(event): # runs when window is released
                main.config(cursor="arrow")
                
            title_bar.bind('<B1-Motion>', move_window)
            title_bar.bind('<ButtonRelease-1>', release_window)
            title_bar_title.bind('<B1-Motion>', move_window)
            title_bar_title.bind('<ButtonRelease-1>', release_window)
        else:
            expand_button.config(text="  ◻  ")
            main.maximized = not main.maximized

    title_bar.bind('<Button-1>', get_pos) # so you can drag the window from the title bar
    title_bar_title.bind('<Button-1>', get_pos) # so you can drag the window from the title 

    # button effects in the title bar when hovering over buttons
    close_button.bind('<Enter>',changex_on_hovering)
    close_button.bind('<Leave>',returnx_to_normalstate)
    expand_button.bind('<Enter>', change_size_on_hovering)
    expand_button.bind('<Leave>', return_size_on_hovering)
    minimize_button.bind('<Enter>', changem_size_on_hovering)
    minimize_button.bind('<Leave>', returnm_size_on_hovering)

    # resize the window width
    resizex_widget = Frame(window,bg=DGRAY,cursor='sb_h_double_arrow')
    resizex_widget.pack(side=RIGHT,ipadx=2,fill=Y)

    def resizex(event):
        xwin = main.winfo_x()
        difference = (event.x_root - xwin) - main.winfo_width()
        
        if main.winfo_width() > 1024 : # 150 is the minimum width for the window
            try:
                main.geometry(f"{ main.winfo_width() + difference }x{ main.winfo_height() }")
            except:
                pass
        else:
            if difference > 0: # so the window can't be too small (150x150)
                try:
                    main.geometry(f"{ main.winfo_width() + difference }x{ main.winfo_height() }")
                except:
                    pass
                
        resizex_widget.config(bg=DGRAY)

    resizex_widget.bind("<B1-Motion>",resizex)

    # resize the window height
    resizey_widget = Frame(window,bg=DGRAY,cursor='sb_v_double_arrow')
    resizey_widget.pack(side=BOTTOM,ipadx=2,fill=X)

    def resizey(event):
        ywin = main.winfo_y()
        difference = (event.y_root - ywin) - main.winfo_height()

        if main.winfo_height() > 512: # 150 is the minimum height for the window
            try:
                main.geometry(f"{ main.winfo_width()  }x{ main.winfo_height() + difference}")
            except:
                pass
        else:
            if difference > 0: # so the window can't be too small (150x150)
                try:
                    main.geometry(f"{ main.winfo_width()  }x{ main.winfo_height() + difference}")
                except:
                    pass

        resizex_widget.config(bg=DGRAY)

    resizey_widget.bind("<B1-Motion>",resizey)

    # some settings
    main.bind("<FocusIn>",deminimize) # to view the window by clicking on the window icon on the taskbar
    main.after(10, lambda: set_appwindow(main)) # to see the icon on the task bar

    # Create Frame for X Scrollbar
    sec = Frame(window)
    sec.pack(fill=X,side=BOTTOM)

    # Create A Canvas
    my_canvas = Canvas(window)      
    my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

    # Add A Scrollbars to Canvas
    x_scrollbar = ttk.Scrollbar(sec,orient=HORIZONTAL,command=my_canvas.xview)
    x_scrollbar.pack(side=BOTTOM,fill=X)
    y_scrollbar = ttk.Scrollbar(window,orient=VERTICAL,command=my_canvas.yview)
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
    braveimage = braveicon.subsample(21,21)
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
    vivaldiimage = vivaldiicon.subsample(15,15)
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

    utilities_frame = Frame(second_frame)
    utilities_frame.grid(row=3 ,column=0,sticky=E+W)

    utilities_frame2 = Frame(utilities_frame)
    utilities_frame2.pack(fill=X,side=BOTTOM)

    utilitiescanvas = Canvas(utilities_frame)
    utilitiescanvas.pack(side=LEFT,fill=X,expand=1)

    x_scrollbar = ttk.Scrollbar(utilities_frame2,orient=HORIZONTAL,command=utilitiescanvas.xview)
    x_scrollbar.pack(side=BOTTOM,fill=X)
    utilitiescanvas.configure(xscrollcommand=x_scrollbar.set)
    utilitiescanvas.bind("<Configure>",lambda e: utilitiescanvas.config(scrollregion= utilitiescanvas.bbox(ALL)))
    utilities_frame3 = Frame(utilitiescanvas)
    utilitiescanvas.create_window((100,100),window= utilities_frame3, anchor="nw")
    #############################################################utilities##################################################
    utilitiessectionframe= Frame(utilities_frame3)
    utilitiessectionframe.grid(row=0,column=0,pady=15,padx=15)

    utilitiessection=ttk.Label(utilitiessectionframe,text="Utilities",font=("Segou UI variable",18))
    utilitiessection.grid(row=0,column=0,pady=15,padx=15)

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
    spacing.grid(row=0,column=13)
    spacing=ttk.Label(utilitiessectionframe,text="         ")
    spacing.grid(row=0,column=15)
    spacing=ttk.Label(utilitiessectionframe,text="         ")
    spacing.grid(row=0,column=17)
    spacing=ttk.Label(utilitiessectionframe,text="         ")
    spacing.grid(row=0,column=19)
    spacing=ttk.Label(utilitiessectionframe,text="         ")
    spacing.grid(row=0,column=21)
    spacing=ttk.Label(utilitiessectionframe,text="         ")
    spacing.grid(row=0,column=23)
    spacing=ttk.Label(utilitiessectionframe,text="         ")
    spacing.grid(row=0,column=25)
    spacing=ttk.Label(utilitiessectionframe,text="         ")
    spacing.grid(row=0,column=27)

    ##############################hwinfo########################
    hwinfoicon= PhotoImage(file = r"images\hwinfo-icon-512x512-8ybzko3v.png")
    hwinfoimage = hwinfoicon.subsample(8,8)
    hwinfourl="https://download.fosshub.com/Protected/expiretime=1673420828;badurl=aHR0cHM6Ly93d3cuZm9zc2h1Yi5jb20vSFdpTkZPLmh0bWw=/5f861ee14a1074acf7d825c276f32ba624ec19341942bd9c155fef16d2305d85/5b969867e5c78775cb187a52/639055157bcd531cda461531/hwi_734.exe"
    hwinfopath="downloads//hwinfo.exe"
    hwinfofile="downloads\\hwinfo.exe"
    hwinfo=ttk.Button(utilitiessectionframe,image=hwinfoimage,text="     HW Info \n\n ★★★★☆ 4",width=10,compound=LEFT,command=lambda: [intcheck(),install(hwinfourl,hwinfopath,hwinfofile,"hwinfo")])
    hwinfo.grid(row=0,column=2,ipady=30, ipadx=15)

    ##############################coretemp########################
    coretempicon= PhotoImage(file = r"images\34454443.png")
    coretempimage = coretempicon.subsample(5,5)
    coretempurl="https://files01.tchspt.com/temp/Core-Temp-setup.exe"
    coretemppath="downloads//coretemp.exe"
    coretempfile="downloads\\coretemp.exe"
    coretemp=ttk.Button(utilitiessectionframe,image=coretempimage,text="    Core Temp \n\n ★★★★☆ 4",width=10,compound=LEFT,command=lambda: [intcheck(),install(coretempurl,coretemppath,coretempfile,"coretemp")])
    coretemp.grid(row=0,column=4,ipady=30, ipadx=15)

    ##############################sevenzip########################
    sevenzipicon= PhotoImage(file = r"images\1280px-7-Zip_Icon.svg.png")
    sevenzipimage = sevenzipicon.subsample(17,17)
    sevenzipurl="https://www.7-zip.org/a/7z2201-x64.exe"
    sevenzippath="downloads//7zip.exe"
    sevenzipfile="downloads\\7zip.exe"
    sevenzip=ttk.Button(utilitiessectionframe,image=sevenzipimage,text="         7Zip \n\n ★★★★☆ 4.3",width=10,compound=LEFT,command=lambda: [intcheck(),install(sevenzipurl,sevenzippath,sevenzipfile,"sevenzip")])
    sevenzip.grid(row=0,column=6,ipady=30, ipadx=15)

    ##############################anydesk########################
    anydeskicon= PhotoImage(file = r"images\unnamed.png")
    anydeskimage = anydeskicon.subsample(9,9)
    anydeskurl="https://download.anydesk.com/AnyDesk.exe"
    anydeskpath="downloads//anydesk.exe"
    anydeskfile="downloads\\anydesk.exe"
    anydesk=ttk.Button(utilitiessectionframe,image=anydeskimage,text="      Anydesk \n\n ★★★★☆ 4.4",width=10,compound=LEFT,command=lambda: [intcheck(),install(anydeskurl,anydeskpath,anydeskfile,"anydesk")])
    anydesk.grid(row=0,column=8,ipady=30, ipadx=15)
    
    ##############################cpuz########################
    cpuzicon= PhotoImage(file = r"images\CPU-Z_Icon.svg.png")
    cpuzimage = cpuzicon.subsample(2,2)
    cpuzurl="https://download.cpuid.com/cpu-z/cpu-z_2.03-en.exe"
    cpuzpath="downloads//cpuz.exe"
    cpuzfile="downloads\\cpuz.exe"
    cpuz=ttk.Button(utilitiessectionframe,image=cpuzimage,text="        CPU-Z \n\n ★★★★☆ 4.5",width=10,compound=LEFT,command=lambda: [intcheck(),install(cpuzurl,cpuzpath,cpuzfile,"cpuz")])
    cpuz.grid(row=0,column=10,ipady=30, ipadx=15)

    ##############################etcher########################
    etchericon= PhotoImage(file = r"images\avatar.png")
    etcherimage = etchericon.subsample(4,4)
    etcherurl="https://github.com/balena-io/etcher/releases/download/v1.13.1/balenaEtcher-Setup-1.13.1.exe"
    etcherpath="downloads//etcher.exe"
    etcherfile="downloads\\etcher.exe"
    etcher=ttk.Button(utilitiessectionframe,image=etcherimage,text="Balena Etcher \n\n ★★★★☆ 4",width=10,compound=LEFT,command=lambda: [intcheck(),install(etcherurl,etcherpath,etcherfile,"etcher")])
    etcher.grid(row=0,column=12,ipady=30, ipadx=15)
    
    ##############################gpuz########################
    gpuzicon= PhotoImage(file = r"images\gpu_z_icon_by_pitmankeks_de0lyld-fullview.png")
    gpuzimage = gpuzicon.subsample(9,9)
    gpuzurl="https://files1.majorgeeks.com/10afebdbffcd4742c81a3cb0f6ce4092156b4375/video/GPU-Z.2.52.0.exe"
    gpuzpath="downloads//gpuz.exe"
    gpuzfile="downloads\\gpuz.exe"
    gpuz=ttk.Button(utilitiessectionframe,image=gpuzimage,text="      GPU-Z \n\n ★★★☆☆ 3.6",width=10,compound=LEFT,command=lambda: [intcheck(),install(gpuzurl,gpuzpath,gpuzfile,"gpuz")])
    gpuz.grid(row=0,column=14,ipady=30, ipadx=15)

    ##############################revouninstaller########################
    revouninstallericon= PhotoImage(file = r"images\Revouninstallerpro_icon.png")
    revouninstallerimage = revouninstallericon.subsample(9,9)
    revouninstallerurl="https://www.revouninstaller.com/start-freeware-download/"
    revouninstallerpath="downloads//revouninstaller.exe"
    revouninstallerfile="downloads\\revouninstaller.exe"
    revouninstaller=ttk.Button(utilitiessectionframe,image=revouninstallerimage,text=" Revo Uninstaller \n\n ★★★☆☆ 3.5",width=12,compound=LEFT,command=lambda: [intcheck(),install(revouninstallerurl,revouninstallerpath,revouninstallerfile,"revouninstaller")])
    revouninstaller.grid(row=0,column=16,ipady=30, ipadx=15)

    ##############################powertoys########################
    powertoysicon= PhotoImage(file = r"images\2020_PowerToys_Icon.svg.png")
    powertoysimage = powertoysicon.subsample(36,36)
    powertoysurl="https://github.com/microsoft/PowerToys/releases/download/v0.66.0/PowerToysSetup-0.66.0-x64.exe"
    powertoyspath="downloads//powertoys.exe"
    powertoysfile="downloads\\powertoys.exe"
    powertoys=ttk.Button(utilitiessectionframe,image=powertoysimage,text="      Powertoys \n\n ★★★★☆ 4.5",width=12,compound=LEFT,command=lambda: [intcheck(),install(powertoysurl,powertoyspath,powertoysfile,"powertoys")])
    powertoys.grid(row=0,column=18,ipady=30, ipadx=15)

    ##############################autohotkey########################
    autohotkeyicon= PhotoImage(file = r"images\sBnPQRG.png")
    autohotkeyimage = autohotkeyicon.subsample(5,5)
    autohotkeyurl="https://www.autohotkey.com/download/ahk-v2.exe"
    autohotkeypath="downloads//autohotkey.exe"
    autohotkeyfile="downloads\\autohotkey.exe"
    autohotkey=ttk.Button(utilitiessectionframe,image=autohotkeyimage,text="    Autohotkey \n\n ★★★★☆ 4.4",width=12,compound=LEFT,command=lambda: [intcheck(),install(autohotkeyurl,autohotkeypath,autohotkeyfile,"autohotkey")])
    autohotkey.grid(row=0,column=20,ipady=30, ipadx=15)

    ##############################bitwarden########################
    bitwardenicon= PhotoImage(file = r"images\1200x630bb.png")
    bitwardenimage = bitwardenicon.subsample(11,11)
    bitwardenurl="https://objects.githubusercontent.com/github-production-release-asset-2e65be/53538899/97993fce-af92-400b-b5c8-c77f2382da49?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20230110%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230110T182412Z&X-Amz-Expires=300&X-Amz-Signature=838086e218d4425ad8ddc247822e0a0b6d6c37230c36f91a9d96444bdef95bf8&X-Amz-SignedHeaders=host&actor_id=112751363&key_id=0&repo_id=53538899&response-content-disposition=attachment%3B%20filename%3DBitwarden-Installer-2022.12.0.exe&response-content-type=application%2Foctet-stream"
    bitwardenpath="downloads//bitwarden.exe"
    bitwardenfile="downloads\\bitwarden.exe"
    bitwarden=ttk.Button(utilitiessectionframe,image=bitwardenimage,text="     Bitwarden \n\n ★★★★☆ 4",width=12,compound=LEFT,command=lambda: [intcheck(),install(bitwardenurl,bitwardenpath,bitwardenfile,"bitwarden")])
    bitwarden.grid(row=0,column=22,ipady=30, ipadx=15)

    ##############################everythingsearch########################
    everythingsearchicon= PhotoImage(file = r"images\dbc1fc0d2b9e238f5863eb19ef214629.png")
    everythingsearchimage = everythingsearchicon.subsample(5,5)
    everythingsearchurl="https://www.voidtools.com/Everything-1.4.1.1022.x86-Setup.exe"
    everythingsearchpath="downloads//everythingsearch.exe"
    everythingsearchfile="downloads\\everythingsearch.exe"
    everythingsearch=ttk.Button(utilitiessectionframe,image=everythingsearchimage,text="Everything search \n\n ★★★★☆ 4",width=14,compound=LEFT,command=lambda: [intcheck(),install(everythingsearchurl,everythingsearchpath,everythingsearchfile,"everythingsearch")])
    everythingsearch.grid(row=0,column=24,ipady=30, ipadx=15)

    ################passwordmanager###########
    passwordmanagericon= PhotoImage(file = r"images\b8ac5e46-1a16-448b-9a12-bf597a95d173.png")
    passwordmanagerimage = passwordmanagericon.subsample(11,11)
    passwordmanagerurl="https://github.com/VarunAdhityaGB/Password-Manager-GUI/releases/download/v.1.2/Password_Manager_v.1.2_Setup.exe"
    passwordmanagerpath="downloads//passwordmanager.exe"
    passwordmanagerfile="downloads\\passwordmanager.exe"
    passwordmanagerutility=ttk.Button(utilitiessectionframe,image=passwordmanagerimage,text="Password Manager \n\n ★★★★☆ 4",width=15,compound=LEFT,command=lambda: [intcheck(),install(passwordmanagerurl,passwordmanagerpath,passwordmanagerfile,"passwordmanager")])
    passwordmanagerutility.grid(row=0,column=26,ipady=30, ipadx=15)

    ################flux###########
    fluxicon= PhotoImage(file = r"images\flux-icon-big.png")
    fluximage = fluxicon.subsample(5,5)
    fluxurl="https://justgetflux.com/dlwin.html"
    fluxpath="downloads//flux.exe"
    fluxfile="downloads\\flux.exe"
    fluxutility=ttk.Button(utilitiessectionframe,image=fluximage,text="        Flux \n\n ★★★★☆ 4.8",width=12,compound=LEFT,command=lambda: [intcheck(),install(fluxurl,fluxpath,fluxfile,"flux")])
    fluxutility.grid(row=0,column=28,ipady=30, ipadx=15)

    spacing=ttk.Label(second_frame,text="                                                                                                                                                                                                                                                                                                                                            ")
    spacing.grid(row=100,column=0)
    
    main.mainloop()

mainsplash.after(3000, mainwindow)
mainsplash.mainloop()