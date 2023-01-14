from tkinter import *
import urllib
from urllib import request  
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk
import sv_ttk as sv
import os 
import requests
from ctypes import windll
import subprocess

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
    global main
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

    def deminimzewhenappinstalled():
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
    status=ttk.Label(title_bar,text="v.0.1.Beta")
    status.place(relx=0.82,rely=0.35)
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

    def intcheck(id,appname):
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
                    wingetcheck(id,appname)  
            elif x==0:
                break

        if net_stat==True:
            wingetcheck(id,appname)   

    def wingetcheck(id,appname):
        try:
            subprocess.run(["winget", "--version"], check=True, capture_output=True)
            print("Winget is already installed.")
            wingetinstall(id,appname)
        except subprocess.CalledProcessError:
            subprocess.run(["powershell", "-Command", "(New-Object Net.WebClient).DownloadFile('https://github.com/microsoft/winget-cli/releases/latest/download/Winget.exe', 'winget.exe')"], check=True)
            subprocess.run(["winget", "install","--id", "Winget"], check=True)
            print("Winget has been installed.")

    def wingetinstall(id,appname):
        print(id)
        text="do you want to install "+appname+"?"
        x = messagebox.askyesno("do you want to install this application?",text )
        while x == 1:
            try:
                minimize_me()
                messagebox.showinfo("have patience","app is being installed.please wait until the installation is finished.")
                subprocess.run(["winget", "install", "--id", id ], check=True)
                completetext=appname+" has been installed successfully"
                messagebox.showinfo("installation complete", completetext)
                deminimzewhenappinstalled()
                break
            except subprocess.CalledProcessError:
                messagebox.showinfo("app already installed.","app already installed.")
                deminimzewhenappinstalled()
                break

    def urlinstall(url,path,file,appname):
        text="do you want to install "+appname+"?"
        x = messagebox.askyesno("do you want to install this application?",text )
        while x == 1:
            try:
                req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64)',
                'Accept-Language': 'en-US,en;q=0.8',
                'Accept-Encoding': 'gzip,deflate,sdch',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Connection': 'keep-alive'
                })
                x = messagebox.showinfo("Downloading","wait until the app is downloaded")
                request.urlretrieve(req.full_url, path)
                os.system(file)
                break
            except urllib.error.HTTPError:
                print(appname)
                x = messagebox.showinfo("sorry for the inconvenience","sorry for the technical problem.please try again later. :(")
            except requests.exceptions.ConnectionError:
                x=messagebox.askretrycancel("no internet connection.","no internet connection please try later.")

    sec = Frame(window)
    sec.pack(fill=X,side=BOTTOM)

    my_canvas = Canvas(window)      
    my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

    x_scrollbar = ttk.Scrollbar(sec,orient=HORIZONTAL,command=my_canvas.xview)
    x_scrollbar.pack(side=BOTTOM,fill=X)
    y_scrollbar = ttk.Scrollbar(window,orient=VERTICAL,command=my_canvas.yview)
    y_scrollbar.pack(side=RIGHT,fill=Y)

    my_canvas.configure(xscrollcommand=x_scrollbar.set)
    my_canvas.configure(yscrollcommand=y_scrollbar.set)
    my_canvas.bind("<Configure>",lambda e: my_canvas.config(scrollregion= my_canvas.bbox(ALL))) 

    second_frame = Frame(my_canvas)

    my_canvas.create_window((0,0),window= second_frame, anchor="nw")


    ########################################################browsers#######################################################

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
    
    browser_frame3 = Frame(browsercanvas)
    browsercanvas.create_window((100,100),window= browser_frame3, anchor="nw")

    browsersectionframe= Frame(browser_frame3)
    browsersectionframe.grid(row=0,column=0)

    browsersection=ttk.Label(browsersectionframe,text="  Browsers",font=("Segou UI variable",18))
    browsersection.grid(row=0,column=0,ipady=15,ipadx=15)

    #############################spacing between each app##############################

    for i in range(1, 20, 2):
        spacing = ttk.Label(browsersectionframe, text="       ")
        spacing.grid(row=0, column=i)

    ##############brave###############
    braveicon= PhotoImage(file = r"images\Brave_lion_icon.svg.png")
    braveimage = braveicon.subsample(21,21)
    bravebrowser=ttk.Button(browsersectionframe,image=braveimage,text="        Brave\n\n ★★★★☆ 4.2 ",width=15,compound=LEFT,command=lambda: [intcheck("Brave.Brave","Brave Browser")])
    ##############firefox###############
    firefoxicon= PhotoImage(file = r"images\Firefox_logo,_2017.svg.png")
    firefoximage = firefoxicon.subsample(17,17)
    firefoxbrowser=ttk.Button(browsersectionframe,image=firefoximage,text="       Firefox\n\n ★★★★☆ 4",width=10,compound=LEFT,command=lambda: [intcheck("Mozilla.Firefox","firefox Browser")])
    ##############librewolf###############
    librewolficon= PhotoImage(file = r"images\LibreWolf_icon.svg.png")
    librewolfimage = librewolficon.subsample(30,30)
    librewolfbrowser=ttk.Button(browsersectionframe,image=librewolfimage,text="     Librewolf\n\n ★★★★☆ 4",width=10,compound=LEFT,command=lambda: intcheck("Librewolf.Librewolf","Librewolf Browser"))
    ##############tor browser###############
    toricon= PhotoImage(file = r"images\Tor_Browser_icon.svg.png")
    torimage = toricon.subsample(17,17)
    torbrowser =ttk.Button(browsersectionframe,image=torimage,text="        Tor \n\n ★★★☆☆ 3.5",width=10,compound=LEFT,command=lambda: [intcheck("TorProject.TorBrowser","Tor Browser")])
    ##############vivaldi browser###############
    vivaldiicon= PhotoImage(file = r"images\Vivaldi_web_browser_logo.svg.png")
    vivaldiimage = vivaldiicon.subsample(15,15)
    vivaldibrowser=ttk.Button(browsersectionframe,image=vivaldiimage,text="     Vivaldi \n\n ★★★☆☆ 3.5",width=10,compound=LEFT,command=lambda: [intcheck("VivaldiTechnologies.Vivaldi","Vivaldi Browser")])
    #############chrome##############
    chromeicon= PhotoImage(file = r"images\Google_Chrome_icon_(February_2022).svg.png")
    chromeimage = chromeicon.subsample(30,30)
    chromebrowser=ttk.Button(browsersectionframe,image=chromeimage,text="     Chrome \n\n ★★★★☆ 4",width=10,compound=LEFT,command=lambda: [intcheck("Google.Chrome","Google chrome browser")])
    #############msedge##############
    msedgeicon= PhotoImage(file = r"images\Microsoft_Edge_Dev_Icon_(2019).svg.png")
    msedgeimage = msedgeicon.subsample(32,32)
    msedgebrowser=ttk.Button(browsersectionframe,image=msedgeimage,text="   MS Edge Dev \n\n ★★★☆☆ 3.6",width=10,compound=LEFT,command=lambda: [intcheck("Microsoft.Edge.Dev","Microsoft Edge Dev")])

    #################placements of all browsers################

    browserlists= ["dummy",bravebrowser,firefoxbrowser,librewolfbrowser,torbrowser,vivaldibrowser,chromebrowser,msedgebrowser]

    for i in range(2, len(browserlists)*2, 2):
        if i/2 < len(browserlists):
            button = browserlists[i//2]
            button.grid(row=0, column=i, ipady=30, ipadx=15)
            
    #############################################################communication##################################################
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
    
    communicationsectionframe= Frame(communication_frame3)
    communicationsectionframe.grid(row=1,column=0)

    communicationsection=ttk.Label(communicationsectionframe,text="Communication",font=("Segou UI variable",18))
    communicationsection.grid(row=0,column=0,pady=15,padx=15)

    for i in range(1, 20, 2):
        spacing = ttk.Label(communicationsectionframe, text="       ")
        spacing.grid(row=0, column=i)

    ##############discord###############
    discordicon= PhotoImage(file = r"images\636e0a6a49cf127bf92de1e2_icon_clyde_blurple_RGB.png")
    discordimage = discordicon.subsample(8,8)
    discord=ttk.Button(communicationsectionframe,image=discordimage,text="      Discord \n\n ★★★★☆ 4.5",width=9,compound=LEFT,command=lambda: [intcheck("Discord.Discord","Discord")])
    ##############teams###############
    teamsicon= PhotoImage(file = r"images\Microsoft_Office_Teams_(2018–present).svg.png")
    teamsimage = teamsicon.subsample(35,35)
    teams=ttk.Button(communicationsectionframe,image=teamsimage,text="      Teams \n\n ★★★☆☆ 3.5",width=10,compound=LEFT,command=lambda: [intcheck("Microsoft.Teams","Microsoft Teams")])
    ##############skype###############
    skypeicon= PhotoImage(file = r"images\174869.png")
    skypeimage = skypeicon.subsample(9,9)
    skype=ttk.Button(communicationsectionframe,image=skypeimage,text="      Skype \n\n ★★★★☆ 4.5",width=10,compound=LEFT,command=lambda: [intcheck("Microsoft.Skype", "Microsoft Skype")])
    ##############zoom###############
    zoomicon= PhotoImage(file = r"images\5e8ce423664eae0004085465.png")
    zoomimage = zoomicon.subsample(5,5)
    zoom=ttk.Button(communicationsectionframe,image=zoomimage,text="        Zoom \n\n ★★★★☆ 4.5",width=10,compound=LEFT,command=lambda: [intcheck("Zoom.Zoom","Zoom")])
    ##############slack###############
    slackicon= PhotoImage(file = r"images\2111615.png")
    slackimage = slackicon.subsample(9,9)
    slack=ttk.Button(communicationsectionframe,image=slackimage,text="      Slack \n\n ★★★★☆ 4.5",width=10,compound=LEFT,command=lambda: [intcheck("SlackTechnologies.Slack","Slack")])
    ##############telegram###############
    telegramicon= PhotoImage(file = r"images\telegram-logo-AD3D08A014-seeklogo.com.png")
    telegramimage = telegramicon.subsample(5,5)
    telegram=ttk.Button(communicationsectionframe,image=telegramimage,text="      Telegram \n\n ★★★☆☆ 3.5",width=10,compound=LEFT,command=lambda: [intcheck("Telegram.TelegramDesktop","Telegram Desktop")])
    ##############viber###############
    vibericon= PhotoImage(file = r"images\2111705.png")
    viberimage = vibericon.subsample(9,9)
    viber=ttk.Button(communicationsectionframe,image=viberimage,text="      Viber \n\n ★★★★☆ 4.5",width=10,compound=LEFT,command=lambda: [intcheck("Viber.Viber","Viber")])

    ##########placement of communication apps##########
    commlists= ["dummy",discord,teams,skype,zoom,slack,telegram,viber]

    for i in range(2, len(commlists)*2, 2):
        if i/2 < len(commlists):
            button = commlists[i//2]
            button.grid(row=0, column=i, ipady=30, ipadx=15)
    
    
    #############################################################development##################################################
    
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
    
    developmentsectionframe= Frame(development_frame3)
    developmentsectionframe.grid(row=2,column=0,pady=15,padx=15)

    developmentsection=ttk.Label(developmentsectionframe,text="Development",font=("Segou UI variable",18))
    developmentsection.grid(row=0,column=0,pady=15,padx=15)

    for i in range(1, 30, 2):
        spacing = ttk.Label(developmentsectionframe, text="       ")
        spacing.grid(row=0, column=i)

    ##############git###############
    giticon= PhotoImage(file = r"images\Git-Icon-1788C.png")
    gitimage = giticon.subsample(6,6)
    git=ttk.Button(developmentsectionframe,image=gitimage,text="      Git",width=10,compound=LEFT,command=lambda: [intcheck("Git.Git","Git")])
    ##############githubdesktop###############
    githubdesktopicon= PhotoImage(file = r"images\768px-Github-desktop-logo-symbol.svg.png")
    githubdesktopimage = githubdesktopicon.subsample(12,12)
    githubdesktop=ttk.Button(developmentsectionframe,image=githubdesktopimage,text="    Github Desktop",width=12,compound=LEFT,command=lambda: [intcheck("GitHub.GitHubDesktop","GitHub Desktop")])
    ##############jetbrainstoolbox###############
    jetbrainstoolboxicon= PhotoImage(file = r"images\toolbox_logo_300x300.png")
    jetbrainstoolboximage = jetbrainstoolboxicon.subsample(5,5)
    jetbrainstoolbox=ttk.Button(developmentsectionframe,image=jetbrainstoolboximage,text="Jetbrains Toolbox",width=13,compound=LEFT,command=lambda: [intcheck("JetBrains.Toolbox","JetBrains Toolbox")])
    ##############python###############
    pythonicon= PhotoImage(file = r"images\5968350.png")
    pythonimage = pythonicon.subsample(9,9)
    python=ttk.Button(developmentsectionframe,image=pythonimage,text="  Python",width=10,compound=LEFT,command=lambda: [intcheck("9PJPW5LDXLZ5","Python")])
    ##############vscode###############
    vscodeicon= PhotoImage(file = r"images\Visual_Studio_Code_1.35_icon.svg.png")
    vscodeimage = vscodeicon.subsample(36,36)
    vscode=ttk.Button(developmentsectionframe,image=vscodeimage,text="  VS Code",width=10,compound=LEFT,command=lambda: [intcheck("Microsoft.VisualStudioCode","Visual Studio Code")])
    ##############vscodium###############
    vscodiumicon= PhotoImage(file = r"images\i7zov9ca3ts71.png")
    vscodiumimage = vscodiumicon.subsample(18,18)
    vscodium=ttk.Button(developmentsectionframe,image=vscodiumimage,text="  VS Codium",width=10,compound=LEFT,command=lambda: [intcheck("VSCodium.VSCodium","VS Codium")])
    ##############nodejs###############
    nodejsicon= PhotoImage(file = r"images\5968322.png")
    nodejsimage = nodejsicon.subsample(9,9)
    nodejs=ttk.Button(developmentsectionframe,image=nodejsimage,text="  Node JS",width=10,compound=LEFT,command=lambda: [intcheck("OpenJS.NodeJS","Node JS")])
    ##############rust###############
    rusticon= PhotoImage(file = r"images\Rust_programming_language_black_logo.svg.png")
    rustimage = rusticon.subsample(36,36)
    rust=ttk.Button(developmentsectionframe,image=rustimage,text="     Rust",width=10,compound=LEFT,command=lambda: [intcheck("Rustlang.Rust.GNU","Rust language")])
    ##############visualstudio###############
    vsstudioicon= PhotoImage(file = r"images\Visual_Studio_Icon_2022.svg.png")
    vsstudioimage = vsstudioicon.subsample(36,36)
    vsstudio=ttk.Button(developmentsectionframe,image=vsstudioimage,text="Visual Studio 2022",width=14,compound=LEFT,command=lambda: [intcheck("Microsoft.VisualStudio.2022.Community-Preview","Microsoft Visual Studio 2022 Community")])
    ##############sublime###############
    sublimeicon= PhotoImage(file = r"images\download.png")
    sublimeimage = sublimeicon.subsample(4,4)
    sublime=ttk.Button(developmentsectionframe,image=sublimeimage,text="    Sublime",width=10,compound=LEFT,command=lambda: [intcheck("SublimeHQ.SublimeText.4","Sublime Text")])

    ##########placement of dev apps##########
    devlists= ["dummy",git,githubdesktop,jetbrainstoolbox,python,vscode,vscodium,nodejs,rust,vsstudio,sublime]

    for i in range(2, len(devlists)*2, 2):
        if i/2 < len(devlists):
            button = devlists[i//2]
            button.grid(row=0, column=i, ipady=30, ipadx=15)

    #############################################################utilities##################################################
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

    utilitiessectionframe= Frame(utilities_frame3)
    utilitiessectionframe.grid(row=0,column=0,pady=15,padx=15)

    utilitiessection=ttk.Label(utilitiessectionframe,text="Utilities",font=("Segou UI variable",18))
    utilitiessection.grid(row=0,column=0,pady=15,padx=15)

    for i in range(1, 30, 2):
        spacing = ttk.Label(utilitiessectionframe, text="       ")
        spacing.grid(row=0, column=i)
    
    ##############################hwinfo########################
    hwinfoicon= PhotoImage(file = r"images\hwinfo-icon-512x512-8ybzko3v.png")
    hwinfoimage = hwinfoicon.subsample(8,8)
    hwinfo=ttk.Button(utilitiessectionframe,image=hwinfoimage,text="     HW Info \n\n ★★★★☆ 4",width=10,compound=LEFT,command=lambda: [intcheck("REALiX.HWiNFO","HWiNFO")])
    ##############################coretemp########################
    coretempicon= PhotoImage(file = r"images\34454443.png")
    coretempimage = coretempicon.subsample(5,5)
    coretemp=ttk.Button(utilitiessectionframe,image=coretempimage,text="    Core Temp \n\n ★★★★☆ 4",width=10,compound=LEFT,command=lambda: [intcheck("ALCPU.CoreTemp","CoreTemp")])
    ##############################sevenzip########################
    sevenzipicon= PhotoImage(file = r"images\1280px-7-Zip_Icon.svg.png")
    sevenzipimage = sevenzipicon.subsample(17,17)
    sevenzip=ttk.Button(utilitiessectionframe,image=sevenzipimage,text="         7Zip \n\n ★★★★☆ 4.3",width=10,compound=LEFT,command=lambda: [intcheck("7zip.7zip","7zip")])
    ##############################anydesk########################
    anydeskicon= PhotoImage(file = r"images\unnamed.png")
    anydeskimage = anydeskicon.subsample(9,9)
    anydesk=ttk.Button(utilitiessectionframe,image=anydeskimage,text="      Anydesk \n\n ★★★★☆ 4.4",width=10,compound=LEFT,command=lambda: [intcheck("AnyDeskSoftwareGmbH.AnyDesk","AnyDesk")])
    ##############################cpuz########################
    cpuzicon= PhotoImage(file = r"images\CPU-Z_Icon.svg.png")
    cpuzimage = cpuzicon.subsample(2,2)
    cpuz=ttk.Button(utilitiessectionframe,image=cpuzimage,text="        CPU-Z \n\n ★★★★☆ 4.5",width=10,compound=LEFT,command=lambda: [intcheck("CPUID.CPU-Z","CPU-Z")])
    ##############################etcher########################
    etchericon= PhotoImage(file = r"images\avatar.png")
    etcherimage = etchericon.subsample(4,4)
    etcher=ttk.Button(utilitiessectionframe,image=etcherimage,text="Balena Etcher \n\n ★★★★☆ 4",width=10,compound=LEFT,command=lambda: [intcheck("Balena.Etcher","Balena Etcher")])
    ##############################gpuz########################
    gpuzicon= PhotoImage(file = r"images\gpu_z_icon_by_pitmankeks_de0lyld-fullview.png")
    gpuzimage = gpuzicon.subsample(9,9)
    gpuz=ttk.Button(utilitiessectionframe,image=gpuzimage,text="      GPU-Z \n\n ★★★☆☆ 3.6",width=10,compound=LEFT,command=lambda: [intcheck("TechPowerUp.GPU-Z","GPU-Z")])
    ##############################revouninstaller########################
    revouninstallericon= PhotoImage(file = r"images\Revouninstallerpro_icon.png")
    revouninstallerimage = revouninstallericon.subsample(9,9)
    revouninstaller=ttk.Button(utilitiessectionframe,image=revouninstallerimage,text=" Revo Uninstaller \n\n ★★★☆☆ 3.5",width=12,compound=LEFT,command=lambda: [intcheck("RevoUninstaller.RevoUninstaller","Revo Uninstaller")])
    ##############################powertoys########################
    powertoysicon= PhotoImage(file = r"images\2020_PowerToys_Icon.svg.png")
    powertoysimage = powertoysicon.subsample(36,36)
    powertoys=ttk.Button(utilitiessectionframe,image=powertoysimage,text="      Powertoys \n\n ★★★★☆ 4.5",width=12,compound=LEFT,command=lambda: [intcheck("Microsoft.PowerToys","Microsoft PowerToys")])
    ##############################autohotkey########################
    autohotkeyicon= PhotoImage(file = r"images\sBnPQRG.png")
    autohotkeyimage = autohotkeyicon.subsample(5,5)
    autohotkey=ttk.Button(utilitiessectionframe,image=autohotkeyimage,text="    Autohotkey \n\n ★★★★☆ 4.4",width=12,compound=LEFT,command=lambda: [intcheck("Lexikos.AutoHotkey","AutoHotkey")])
    ##############################bitwarden########################
    bitwardenicon= PhotoImage(file = r"images\1200x630bb.png")
    bitwardenimage = bitwardenicon.subsample(11,11)
    bitwarden=ttk.Button(utilitiessectionframe,image=bitwardenimage,text="     Bitwarden \n\n ★★★★☆ 4",width=12,compound=LEFT,command=lambda: [intcheck("Bitwarden.Bitwarden","Bitwarden")])
    bitwarden.grid(row=0,column=22,ipady=30, ipadx=15)
    ##############################everythingsearch########################
    everythingsearchicon= PhotoImage(file = r"images\dbc1fc0d2b9e238f5863eb19ef214629.png")
    everythingsearchimage = everythingsearchicon.subsample(5,5)
    everythingsearch=ttk.Button(utilitiessectionframe,image=everythingsearchimage,text="Everything search \n\n ★★★★☆ 4",width=14,compound=LEFT,command=lambda: [intcheck("voidtools.Everything","Everything Search")])
    ################passwordmanager###########
    passwordmanagericon= PhotoImage(file = r"images\b8ac5e46-1a16-448b-9a12-bf597a95d173.png")
    passwordmanagerimage = passwordmanagericon.subsample(11,11)
    passwordmanagerurl="https://github.com/VarunAdhityaGB/Password-Manager-GUI/releases/download/v.1.2/Password_Manager_v.1.2_Setup.exe"
    passwordmanagerpath="downloads//passwordmanager.exe"
    passwordmanagerfile="downloads\\passwordmanager.exe"
    passwordmanager=ttk.Button(utilitiessectionframe,image=passwordmanagerimage,text="Password Manager \n\n ★★★★☆ 4",width=15,compound=LEFT,command=lambda: [intcheck(),urlinstall(passwordmanagerurl,passwordmanagerpath,passwordmanagerfile,"passwordmanager")])
    ################flux###########
    fluxicon= PhotoImage(file = r"images\flux-icon-big.png")
    fluximage = fluxicon.subsample(5,5)
    flux=ttk.Button(utilitiessectionframe,image=fluximage,text="        Flux \n\n ★★★★☆ 4.8",width=12,compound=LEFT,command=lambda: [intcheck("flux.flux","flux")])

    ##########placement of dev apps##########
    utillists= ["dummy",hwinfo,coretemp,sevenzip,anydesk,cpuz,etcher,gpuz,revouninstaller,powertoys,autohotkey,bitwarden,everythingsearch,passwordmanager,flux]

    for i in range(2, len(utillists)*2, 2):
        if i/2 < len(utillists):
            button = utillists[i//2]
            button.grid(row=0, column=i, ipady=30, ipadx=15)

    #####################################spacing for magic :} ##########################################   
    spacing=ttk.Label(second_frame,text="                                                                                                                                                                                                                                                                                                                                            ")
    spacing.grid(row=100,column=0)
    
    main.mainloop()

mainsplash.after(3000, mainwindow)
mainsplash.mainloop()