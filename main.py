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
import webbrowser

def shownoint(x):
    if x=="mainsplash":
        mainsplash.withdraw()
    elif x=="main":
        main.withdraw()
    noint=Toplevel()
    noint.overrideredirect(True)
    app_width = 1024
    app_height = 512
    screenwidth = noint.winfo_screenwidth()
    screenheight = noint.winfo_screenheight()
    noint.attributes("-alpha", 1)
    x = (screenwidth / 2) - (app_width / 2)
    y = (screenheight / 2) - (app_height / 2)
    noint.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    bg_image1 = ImageTk.PhotoImage(Image.open(r"images\noconnection.png"))
    label2 = Label(noint, image=bg_image1)
    label2.pack()
    noint.bind("<Button-1>", lambda e: noint.destroy())
    noint.bind("<Button-3>", lambda e: intcheckapp(x))
    noint.mainloop()
    
def intcheckapp(x):
    def internet_stat(url="https://www.google.com/", timeout=3):
        try:
            r = requests.head(url=url, timeout=timeout)
            return True
        except requests.exceptions.ConnectionError as e:
            return False

    net_stat = internet_stat()

    if net_stat == False:
        shownoint(x)

    if net_stat == True:
        if x == "mainsplash":
            mainsplash.withdraw()
        elif x == "main":
            main.withdraw()
        
            
mainsplash = Tk()
sv.set_theme("dark")
mainsplash.overrideredirect(True)
app_width = 1024
app_height = 512
screenwidth = mainsplash.winfo_screenwidth()
screenheight = mainsplash.winfo_screenheight()
mainsplash.attributes("-alpha", 1)
x = (screenwidth / 2) - (app_width / 2)
y = (screenheight / 2) - (app_height / 2)
mainsplash.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
bg_image = ImageTk.PhotoImage(Image.open(r"images\softhub load.png"))
label1 = Label(mainsplash, image=bg_image)
label1.pack()
intcheckapp("mainsplash")


result = str(subprocess.run(["winget", "list", "--source", "winget"], check=True, capture_output=True))
result = result.replace("\\r\\n", "\n")
result = result.split()
result = result[12:]
packages = result[:-3]

def set_appwindow(mainWindow):  # to display the window icon on the taskbar,
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
    main.attributes("-alpha", 0)  # so you can't see the window when its minimized
    main.minimized = True


def deminimize(event):
    main.focus()
    main.attributes("-alpha", 1)  # so you can see the window when is not minimized
    if main.minimized == True:
        main.minimized = False


def deminimzewhenappinstalled():
    main.focus()
    main.attributes("-alpha", 1)  # so you can see the window when is not minimized
    if main.minimized == True:
        main.minimized = False


def maximize_me():
    if main.maximized == False:  # if the window was not maximized
        main.normal_size = main.geometry()
        expand_button.config(text="  🗗  ")
        main.geometry(f"{main.winfo_screenwidth()}x{main.winfo_screenheight()}+0+0")
        main.maximized = not main.maximized
        # maximized

    else:  # if the window was maximized
        expand_button.config(text="  ◻  ")
        main.geometry(main.normal_size)
        main.maximized = not main.maximized
        # not maximized


def mainwindow():
    global close_button
    global expand_button
    global minimize_button
    global main
    main = Toplevel()
    main.tk.call('wm', 'iconphoto', main._w, ImageTk.PhotoImage(file='images\softhub.ico'))
    s = ttk.Style()
    s.configure('.', font=('Segoe UI Variable', 10))
    mainsplash.withdraw()
    screenwidth = main.winfo_screenwidth()
    screenheight = main.winfo_screenheight()
    app_height = int(screenheight) - 48
    main.geometry(f'{screenwidth}x{app_height}+0+0')
    main.title("Softhub")
    main.attributes("-alpha", 1)
    main.overrideredirect(True)
    main.minimized = False
    main.maximized = False
    title_bar = Frame(main,relief='raised', bd=0, highlightthickness=0)
    close_button = Button(title_bar, text='  ✕  ', command=main.destroy, padx=2, pady=2, font=("calibri", 13),
                          bd=0, highlightthickness=0)
    expand_button = Button(title_bar, text='  ◻  ', command=maximize_me,padx=2, pady=2, bd=0,
                           font=("calibri", 13), highlightthickness=0)
    minimize_button = Button(title_bar, text='  —  ', command=minimize_me, padx=2, pady=2, bd=0,
                             font=("calibri", 13), highlightthickness=0)
    title_bar_title = Label(title_bar, text="Softhub", bd=0, font=("helvetica", 14),
                            highlightthickness=0)
    
    # main frame
    window = Frame(main, highlightthickness=0)

    def redirectpsn(x):
        if x == "browser":
            my_canvas.yview("moveto",0)
        elif x == "communication":
            my_canvas.yview("moveto",0.2)
        elif x == "development":
            my_canvas.yview("moveto",0.4)
        elif x == "utilities":
            my_canvas.yview("moveto",0.6)
        elif x == "games":
            my_canvas.yview("moveto",0.8)

    sidebar = ttk.Frame(window, width=45, height=300, relief='sunken')
    sidebar.pack(side='left', fill='both')

    browsericon = PhotoImage(file=r"images\browser.png")
    browsericon = browsericon.subsample(9, 9)
    browser = ttk.Button(sidebar, image=browsericon,padding=0,command=lambda: redirectpsn("browser"))
    browser.place(relx=0.1, rely=0.05)

    communicationicon = PhotoImage(file=r"images\communication.png")
    communicationicon = communicationicon.subsample(9, 9)
    communication = ttk.Button(sidebar, image=communicationicon,padding=0,command=lambda: redirectpsn("communication"))
    communication.place(relx=0.1, rely=0.12)
    
    developmenticon = PhotoImage(file=r"images\development.png")
    developmenticon = developmenticon.subsample(9, 9)
    development = ttk.Button(sidebar, image=developmenticon,padding=0,command=lambda: redirectpsn("development"))
    development.place(relx=0.1, rely=0.19)
    
    utilitiesicon = PhotoImage(file=r"images\utilities.png")
    utilitiesicon = utilitiesicon.subsample(9, 9)
    utilities = ttk.Button(sidebar, image=utilitiesicon,padding=0,command=lambda: redirectpsn("utilities"))
    utilities.place(relx=0.1, rely=0.26)

    gamesicon = PhotoImage(file=r"images\games.png")
    gamesicon = gamesicon.subsample(9, 9)
    games = ttk.Button(sidebar, image=gamesicon,padding=0,command=lambda: redirectpsn("games"))
    games.place(relx=0.1, rely=0.33)

    # pack the widgets
    title_bar.pack(fill=X)

    close_button.pack(side=RIGHT, ipadx=7, ipady=1)
    expand_button.pack(side=RIGHT, ipadx=7, ipady=1)
    minimize_button.pack(side=RIGHT, ipadx=7, ipady=1)
    appicon = PhotoImage(file=r"images\softhuḃicon.png")
    appicon = appicon.subsample(6, 6)
    label = Label(title_bar, image=appicon)
    label.pack(side=LEFT)
    title_bar_title.pack(side=LEFT, padx=10)
    window.pack(expand=1, fill=BOTH)

    on=PhotoImage(file=r"images\darkicon.png")
    on=on.subsample(6, 6)
    off=PhotoImage(file=r"images\lighticon.png")
    off=off.subsample(6, 6)

    global is_on
    is_on = True

    def switch():
        global is_on
        if is_on == True:
            theme.config(image=on)
            is_on = False
            sv.set_theme("dark")
        else:
            theme.config(image=off)
            is_on = True 
            sv.set_theme("light")

    theme=ttk.Button(title_bar,image=on,command=lambda: switch())
    theme.place(relx=0.7,rely=0.1)

    status = ttk.Label(title_bar, text="v.0.2.Alpha")
    status.place(relx=0.77, rely=0.35)

    def openlink():
        webbrowser.open_new("https://github.com/ACExSWAROOP")

    abouticon = PhotoImage(file=r"images\1828885.png")
    abouticon = abouticon.subsample(20, 20)
    aboutbutton = ttk.Button(title_bar, image=abouticon, padding=0, command=lambda: openlink())
    aboutbutton.place(relx=0.84, rely=0.1)

    def changex_on_hovering(event):
        global close_button
        close_button['bg'] = 'red'

    def returnx_to_normalstate(event):
        global close_button

    def change_size_on_hovering(event):
        global expand_button

    def return_size_on_hovering(event):
        global expand_button

    def changem_size_on_hovering(event):
        global minimize_button

    def returnm_size_on_hovering(event):
        global minimize_button

    def get_pos(event):  # this is executed when the title bar is clicked to move the window
        if main.maximized == False:
            xwin = main.winfo_x()
            ywin = main.winfo_y()
            startx = event.x_root
            starty = event.y_root
            ywin = ywin - starty
            xwin = xwin - startx

            def move_window(event):  # runs when window is dragged
                main.config(cursor="fleur")
                main.geometry(f'+{event.x_root + xwin}+{event.y_root + ywin}')

            def release_window(event):  # runs when window is released
                main.config(cursor="arrow")

            title_bar.bind('<B1-Motion>', move_window)
            title_bar.bind('<ButtonRelease-1>', release_window)
            title_bar_title.bind('<B1-Motion>', move_window)
            title_bar_title.bind('<ButtonRelease-1>', release_window)
        else:
            expand_button.config(text="  ◻  ")
            main.maximized = not main.maximized

    title_bar.bind('<Button-1>', get_pos)  # so you can drag the window from the title bar
    title_bar_title.bind('<Button-1>', get_pos)  # so you can drag the window from the title

    # button effects in the title bar when hovering over buttons
    close_button.bind('<Enter>', changex_on_hovering)
    close_button.bind('<Leave>', returnx_to_normalstate)
    expand_button.bind('<Enter>', change_size_on_hovering)
    expand_button.bind('<Leave>', return_size_on_hovering)
    minimize_button.bind('<Enter>', changem_size_on_hovering)
    minimize_button.bind('<Leave>', returnm_size_on_hovering)

    # resize the window width
    resizex_widget = Frame(window, cursor='sb_h_double_arrow')
    resizex_widget.pack(side=RIGHT, ipadx=2, fill=Y)

    def resizex(event):
        xwin = main.winfo_x()
        difference = (event.x_root - xwin) - main.winfo_width()

        if main.winfo_width() > 1024:  # 150 is the minimum width for the window
            try:
                main.geometry(f"{main.winfo_width() + difference}x{main.winfo_height()}")
            except:
                pass
        else:
            if difference > 0:  # so the window can't be too small (150x150)
                try:
                    main.geometry(f"{main.winfo_width() + difference}x{main.winfo_height()}")
                except:
                    pass


    resizex_widget.bind("<B1-Motion>", resizex)

    # resize the window height
    resizey_widget = Frame(window, cursor='sb_v_double_arrow')
    resizey_widget.pack(side=BOTTOM, ipadx=2, fill=X)

    def resizey(event):
        ywin = main.winfo_y()
        difference = (event.y_root - ywin) - main.winfo_height()

        if main.winfo_height() > 512:  # 150 is the minimum height for the window
            try:
                main.geometry(f"{main.winfo_width()}x{main.winfo_height() + difference}")
            except:
                pass
        else:
            if difference > 0:  # so the window can't be too small (150x150)
                try:
                    main.geometry(f"{main.winfo_width()}x{main.winfo_height() + difference}")
                except:
                    pass


    resizey_widget.bind("<B1-Motion>", resizey)

    # some settings
    main.bind("<FocusIn>", deminimize)  # to view the window by clicking on the window icon on the taskbar
    main.after(10, lambda: set_appwindow(main))  # to see the icon on the task bar

    #installappviawinget
    def intcheck(type, id, appname):
        def internet_stat(url="https://www.google.com/", timeout=3):
            try:
                r = requests.head(url=url, timeout=timeout)
                return True
            except requests.exceptions.ConnectionError as e:
                return False

        net_stat = internet_stat()

        if net_stat == False:
                intcheckapp("main")

        if net_stat == True:
            wingetcheck(type, id, appname)

    def wingetcheck(type, id, appname):
        try:
            subprocess.run(["winget", "--version"], check=True, capture_output=True)
            if type == "install":
                wingetinstall(id, appname)
            if type == "update":
                wingetupgrade(id, appname)
            if type == "uninstall":
                wingetuninstall(id, appname)
        except subprocess.CalledProcessError:
            subprocess.run(["powershell", "-Command",
                            "(New-Object Net.WebClient).DownloadFile('https://github.com/microsoft/winget-cli/releases/latest/download/Winget.exe', 'winget.exe')"],
                           check=True)
            subprocess.run(["winget", "install", "--id", "Winget"], check=True)

    def wingetinstall(id, appname):
        text = "do you want to install " + appname + "?"
        installchange.set("Installing...")
        x = messagebox.askyesno("confirmation", text)
        if x == 0:
            installchange.set("Install")
        while x == 1:
            try:
                subprocess.run(["winget", "install", "--id", id], check=True)
                installchange.set("Installed")
                break
            except subprocess.CalledProcessError:
                installchange.set("Installed")
                break

    def wingetupgrade(id, appname):
        updatechange.set("Updating...")
        text = "do you want to update " + appname + "?"
        x = messagebox.askyesno("confirmation", text)
        if x == 0:
            updatechange.set("Update")
        while x == 1:
            try:
                subprocess.run(["winget", "upgrade", "--id", id], check=True)
                updatechange.set("Updated")
                break
            except subprocess.CalledProcessError:
                updatechange.set("Updated")
                break

    def wingetuninstall(id, appname):
        uninstallchange.set("Uninstalling...")
        text = "do you want to uninstall " + appname + "?"
        x = messagebox.askyesno("confirmation", text)
        if x == 0:
            uninstallchange.set("Uninstall")
        while x == 1:
            try:
                subprocess.run(["winget", "uninstall", "--id", id], check=True)
                uninstallchange.set("Uninstalled")
                break
            except subprocess.CalledProcessError:
                uninstallchange.set("Uninstalled")
                break

    ###########installappviaweb##########   if not in winget
    def urlinstall(url, path, file, appname):
        text = "do you want to install " + appname + "?"
        x = messagebox.askyesno("do you want to install this application?", text)
        while x == 1:
            try:
                req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64)',
                                                    'Accept-Language': 'en-US,en;q=0.8',
                                                    'Accept-Encoding': 'gzip,deflate,sdch',
                                                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                                                    'Connection': 'keep-alive'
                                                    })
                x = messagebox.showinfo("Downloading", "wait until the app is downloaded")
                request.urlretrieve(req.full_url, path)
                os.system(file)
                break
            except urllib.error.HTTPError:
                x = messagebox.showinfo("sorry for the inconvenience",
                                        "sorry for the technical problem.please try again later. :(")
            except requests.exceptions.ConnectionError:
                x = messagebox.askretrycancel("no internet connection.", "no internet connection please try later.")

    sec = Frame(window)
    sec.pack(fill=X, side=BOTTOM)

    my_canvas = Canvas(window)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    x_scrollbar = ttk.Scrollbar(sec, orient=HORIZONTAL, command=my_canvas.xview)
    x_scrollbar.pack(side=BOTTOM, fill=X)
    y_scrollbar = ttk.Scrollbar(window, orient=VERTICAL, command=my_canvas.yview)
    y_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(xscrollcommand=x_scrollbar.set)
    my_canvas.configure(yscrollcommand=y_scrollbar.set)
    my_canvas.bind("<Configure>", lambda e: my_canvas.config(scrollregion=my_canvas.bbox(ALL)))

    second_frame = Frame(my_canvas)
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

    global count
    count = 0

    def addapps(type):
        global count
        frame = type + "_frame"
        frame2 = type + "_frame2"
        canvas = type + "_canvas"
        frame3 = type + "_frame3"
        sectionframe = type + "sectionframe"
        section = type + "section"

        frame = Frame(second_frame)
        frame.grid(row=count, column=0, sticky=E + W)

        frame2 = Frame(frame)
        frame2.pack(fill=X, side=BOTTOM)

        canvas = Canvas(frame)
        canvas.pack(side=LEFT, fill=X, expand=1)

        x_scrollbar = ttk.Scrollbar(frame2, orient=HORIZONTAL, command=canvas.xview)
        x_scrollbar.pack(side=BOTTOM, fill=X)

        canvas.configure(xscrollcommand=x_scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.config(scrollregion=canvas.bbox(ALL)))

        frame3 = Frame(canvas)
        canvas.create_window((100, 100), window=frame3, anchor="nw")

        sectionframe = Frame(frame3)
        sectionframe.grid(row=0, column=0, pady=15, padx=15)

        section = ttk.Label(sectionframe, text=type, font=("Segou UI variable", 18))
        section.grid(row=0, column=0, pady=15, padx=15)
        count += 1

        return sectionframe

    def hoverwindow(e, img, name, desc, pack):
        global hoverwin
        hoverwin = Toplevel()
        hoverwin.overrideredirect(True)
        app_width = 640
        app_height = 320
        screenwidth = hoverwin.winfo_screenwidth()
        screenheight = hoverwin.winfo_screenheight()
        x = (screenwidth / 2) - (app_width / 2)
        y = (screenheight / 2) - (app_height / 2)
        hoverwin.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        imglabel = ttk.Label(hoverwin, image=img)
        imglabel.place(relx=0.1, rely=0.1)
        appname = name.splitlines()[0]
        rating = name.splitlines()[2]
        name = appname.replace(" ", "")
        namelabel = ttk.Label(hoverwin, text=name, font=("Segou UI variable", 18))
        namelabel.place(relx=0.31, rely=0.1)
        namelabel1 = ttk.Label(hoverwin, text=rating, font=("Segou UI variable", 18))
        namelabel1.place(relx=0.3, rely=0.2)
        descriptionlbl = ttk.Label(hoverwin, text="Description", font=("Segou UI variable", 18))
        descriptionlbl.place(relx=0.05, rely=0.5)
        desclabel = ttk.Label(hoverwin, text=desc, font=("Segou UI variable", 10))
        desclabel.place(relx=0.05, rely=0.6)
        main.bind("<Button-3>", lambda e: closehover())
        hoverwin.bind("<Button-3>", lambda e: closehover())
        main.bind("<Button-1>", lambda e: closehover())

        global installchange
        installchange = StringVar()
        installbutton = ttk.Button(hoverwin, textvariable=installchange, width=12,
                                   command=lambda: intcheck("install", pack, name))
        installbutton.place(relx=0.28, rely=0.325)
        global updatechange
        updatechange = StringVar()
        updatechange.set("Update")
        updatebutton = ttk.Button(hoverwin, textvariable=updatechange, width=12,
                                  command=lambda: intcheck("update", pack, name))
        updatebutton.place(relx=0.48, rely=0.325)
        global uninstallchange
        uninstallchange = StringVar()
        uninstallchange.set("Uninstall")
        uninstallbutton = ttk.Button(hoverwin, textvariable=uninstallchange, width=12,
                                     command=lambda: intcheck("uninstall", pack, name))
        uninstallbutton.place(relx=0.68, rely=0.325)

        if pack not in packages:
            installchange.set("Install")
            uninstallbutton["state"] = DISABLED
            updatebutton["state"] = DISABLED
        if pack in packages:
            installchange.set("Installed")
            installbutton["state"] = DISABLED

        hoverwin.mainloop()

    def closehover():
        main.attributes("-alpha", 1)
        hoverwin.destroy()

    ########################################################browsers#######################################################

    sectionframe = addapps("Browsers")
    for i in range(1, 18, 2):
            spacing = ttk.Label(sectionframe, text="    ")
            spacing.grid(row=0, column=i)
    ##############brave###############
    braveicon = PhotoImage(file=r"images\Brave_lion_icon.svg.png")
    braveimage = braveicon.subsample(21, 21)
    bravebrowser = ttk.Button(sectionframe, image=braveimage, text="        Brave\n\n ★★★★☆ 4.2 ", width=15,
                              compound=LEFT)
    bravedesc = "Brave is a free and open-source web browser developed by Brave Software, Inc. based on the " \
                "\nChromium web browser. Brave is a privacy-focused browser, which automatically blocks online " \
                "\nadvertisements and website trackers in its default settings. It also provides users the choice " \
                "\nto turn on optional ads that pay users for their attention in the form of Basic Attention Tokens " \
                "\n(BAT) cryptocurrency. "
    bravepack = "Brave.Brave"
    ##############firefox###############
    firefoxicon = PhotoImage(file=r"images\Firefox_logo,_2017.svg.png")
    firefoximage = firefoxicon.subsample(17, 17)
    firefoxbrowser = ttk.Button(sectionframe, image=firefoximage, text="       Firefox\n\n ★★★★☆ 4", width=10,
                                compound=LEFT)
    firefoxdesc = "Mozilla Firefox, or simply Firefox, is a free and open-source web browser developed by the " \
                  "\nMozilla Foundation and its subsidiary, the Mozilla Corporation. It uses the Gecko rendering " \
                  "\nengine to display web pages, which implements current and anticipated web standards. In " \
                  "\nNovember 2017, Firefox began incorporating new technology under the code name Quantum to " \
                  "\npromote parallelism and a more intuitive user interface. "
    firefoxpack = "Mozilla.Firefox"
    ##############librewolf###############
    librewolficon = PhotoImage(file=r"images\LibreWolf_icon.svg.png")
    librewolfimage = librewolficon.subsample(30, 30)
    librewolfbrowser = ttk.Button(sectionframe, image=librewolfimage, text="     Librewolf\n\n ★★★★☆ 4", width=10,
                                  compound=LEFT)
    librewolfdesc = "This project is a custom and independent version of Firefox, with the primary goals of privacy, " \
                    "\nsecurity and user freedom. LibreWolf is designed to increase protection against tracking and " \
                    "\nfingerprinting techniques, while also including a few security improvements. "
    librewolfpack = "Librewolf.Librewolf"
    ##############tor browser###############
    toricon = PhotoImage(file=r"images\Tor_Browser_icon.svg.png")
    torimage = toricon.subsample(17, 17)
    torbrowser = ttk.Button(sectionframe, image=torimage, text="        Tor \n\n ★★★☆☆ 3.5", width=10, compound=LEFT)
    tordesc = "Tor, short for The Onion Router, is free and open-source software for enabling anonymous " \
              "\ncommunication. It directs Internet traffic through a free, worldwide, volunteer overlay network, " \
              "consisting \nof more than seven thousand relays, to conceal a user's location and usage from anyone " \
              "performing \nnetwork surveillance or traffic analysis.Using Tor makes it more difficult to trace a " \
              "user's Internet \nactivity. Tor's intended use is to protect the personal privacy of its users, " \
              "as well as their freedom and \nability to communicate confidentially through IP address anonymity " \
              "using Tor exit nodes. "
    torpack = "TorProject.TorBrowser"
    ##############vivaldi browser###############
    vivaldiicon = PhotoImage(file=r"images\Vivaldi_web_browser_logo.svg.png")
    vivaldiimage = vivaldiicon.subsample(15, 15)
    vivaldibrowser = ttk.Button(sectionframe, image=vivaldiimage, text="     Vivaldi \n\n ★★★☆☆ 3.5", width=10,
                                compound=LEFT)
    vivaldidesc = "Vivaldi is a user-friendly browser designed to provide customizable browsing experiences. With " \
                  "built-in \nnavigation and UI customization tools, users can customize Vivaldi any way they want. "
    vivaldipack = "VivaldiTechnologies.Vivaldi"
    #############chrome##############
    chromeicon = PhotoImage(file=r"images\Google_Chrome_icon_(February_2022).svg.png")
    chromeimage = chromeicon.subsample(30, 30)
    chromebrowser = ttk.Button(sectionframe, image=chromeimage, text="     Chrome \n\n ★★★★☆ 4", width=10,
                               compound=LEFT)
    chromedesc = "Google Chrome is a cross-platform web browser developed by Google. It was first released in 2008 " \
                 "for \nMicrosoft Windows, built with free software components from Apple WebKit and Mozilla Firefox. " \
                 "\nVersions were later released for Linux, macOS, iOS, and also for Android, where it is the default " \
                 "\nbrowser. "
    chromepack = "Google.Chrome"
    #############msedge##############
    msedgeicon = PhotoImage(file=r"images\Microsoft_Edge_Dev_Icon_(2019).svg.png")
    msedgeimage = msedgeicon.subsample(32, 32)
    msedgebrowser = ttk.Button(sectionframe, image=msedgeimage, text="   MS Edge Dev \n\n ★★★★☆ 4", width=10,
                               compound=LEFT)
    msedgedesc = "Microsoft Edge is a proprietary, cross-platform web browser created by Microsoft. It was first " \
                 "released \nin 2015 as part of Windows 10 and Xbox One and later ported to other platforms as a fork " \
                 "of Google's \nChromium open-source project. "
    msedgepack = "Microsoft.Edge.Dev"
    #############opreagx##############
    operagxicon = PhotoImage(file=r"images\Opera_GX_Icon.svg.png")
    operagximage = operagxicon.subsample(18, 18)
    operagxbrowser = ttk.Button(sectionframe, image=operagximage, text="   Opera GX \n\n ★★★★☆ 4", width=10,
                                compound=LEFT)
    operagxdesc = "Opera is a multi-platform web browser developed by its namesake company Opera. The browser is " \
                  "\nbased on Chromium, but distinguishes itself from other Chromium-based browsers (Chrome, Edge, " \
                  "etc.) \nthrough its user interface and other features. "
    operagxpack = "Opera.OperaGX"
    #############chromium##############
    chromiumicon = PhotoImage(file=r"images\Chromium_Logo.svg.png")
    chromiumimage = chromiumicon.subsample(30, 30)
    chromiumbrowser = ttk.Button(sectionframe, image=chromiumimage, text="   Chromium \n\n ★★★★☆ 4", width=10,
                                 compound=LEFT)
    chromiumdesc = "Chromium is a free and open-source web browser project, mainly developed and maintained by " \
                   "\nGoogle. This codebase provides the vast majority of code for the Google Chrome browser, " \
                   "which is \nproprietary software and has some additional features. "
    chromiumpack = "eloston.ungoogled-chromium"
    #################placements of all browsers################
    browserlists = ["dummy", bravebrowser, firefoxbrowser, librewolfbrowser, torbrowser, vivaldibrowser, chromebrowser,
                    msedgebrowser, operagxbrowser, chromiumbrowser]
    browserimgs = ["dummy", braveimage, firefoximage, librewolfimage, torimage, vivaldiimage, chromeimage, msedgeimage,
                   operagximage, chromiumimage]
    browserdescs = ["dummy", bravedesc, firefoxdesc, librewolfdesc, tordesc, vivaldidesc, chromedesc, msedgedesc,
                    operagxdesc, chromiumdesc]
    browserpacknames = ["dummy", bravepack, firefoxpack, librewolfpack, torpack, vivaldipack, chromepack, msedgepack,
                        operagxpack, chromiumpack]
    for i in range(2, len(browserlists) * 2, 2):
        if i / 2 < len(browserlists):
            button = browserlists[i // 2]
            button.grid(row=0, column=i, ipady=30, ipadx=15)
            button.bind("<Button-1>", lambda event, buttonimg=browserimgs[i // 2], buttonname=button.cget('text'),
                                             buttondesc=browserdescs[i // 2],
                                             pckg=browserpacknames[i // 2]: hoverwindow(event, buttonimg, buttonname,
                                                                                        buttondesc, pckg))

    #############################################################communication##################################################

    sectionframe = addapps("Communication")
    for i in range(1, 28, 2):
            spacing = ttk.Label(sectionframe, text="    ")
            spacing.grid(row=0, column=i)
    ##############discord###############
    discordicon = PhotoImage(file=r"images\636e0a6a49cf127bf92de1e2_icon_clyde_blurple_RGB.png")
    discordimage = discordicon.subsample(8, 8)
    discord = ttk.Button(sectionframe, image=discordimage, text="      Discord \n\n ★★★★☆ 4.5", width=9, compound=LEFT)
    discorddesc = "Discord is a free communications app that lets you share voice, video, and text chat with friends, " \
                  "\ngame communities, and developers. It has hundreds of millions of users, making it one of the " \
                  "most \npopular ways to connect with people online. "
    discordpack = "Discord.Discord"
    ##############teams###############
    teamsicon = PhotoImage(file=r"images\Microsoft_Office_Teams_(2018–present).svg.png")
    teamsimage = teamsicon.subsample(35, 35)
    teams = ttk.Button(sectionframe, image=teamsimage, text="      Teams \n\n ★★★☆☆ 3.5", width=10, compound=LEFT)
    teamsdesc = "Microsoft Teams is the ultimate messaging app for your organization—a workspace for real-time " \
                "\ncollaboration and communication, meetings, file and app sharing, and even the occasional emoji! " \
                "\nAll in one place, all in the open, all accessible to everyone. "
    teamspack = "Microsoft.Teams"
    ##############skype###############
    skypeicon = PhotoImage(file=r"images\174869.png")
    skypeimage = skypeicon.subsample(9, 9)
    skype = ttk.Button(sectionframe, image=skypeimage, text="      Skype \n\n ★★★★☆ 4.5", width=10, compound=LEFT)
    skypedesc = "Skype is software that enables the world's conversations. Millions of individuals and businesses " \
                "\nuse Skype to make free video and voice one-to-one and group calls, send instant messages and " \
                "\nshare files with other people on Skype. "
    skypepack = "Microsoft.Skype"
    ##############zoom###############
    zoomicon = PhotoImage(file=r"images\5e8ce423664eae0004085465.png")
    zoomimage = zoomicon.subsample(5, 5)
    zoom = ttk.Button(sectionframe, image=zoomimage, text="        Zoom \n\n ★★★★☆ 4.5", width=10, compound=LEFT)
    zoomdesc = "Zoom is a communications platform that allows users to connect with video, audio, phone, and chat. " \
               "\nUsing Zoom requires an internet connection and a supported device. Most new users will want to " \
               "\nstart by creating an account and downloading the Zoom Client for Meetings. "
    zoompack = "Zoom.Zoom"
    ##############slack###############
    slackicon = PhotoImage(file=r"images\2111615.png")
    slackimage = slackicon.subsample(9, 9)
    slack = ttk.Button(sectionframe, image=slackimage, text="      Slack \n\n ★★★★☆ 4.5", width=10, compound=LEFT)
    slackdesc = "Slack is a messaging app for business that connects people to the information that they need. By " \
                "\nbringing people together to work as one unified team, Slack transforms the way that organisations " \
                "\ncommunicate. "
    slackpack = "SlackTechnologies.Slack"
    ##############telegram###############
    telegramicon = PhotoImage(file=r"images\telegram-logo-AD3D08A014-seeklogo.com.png")
    telegramimage = telegramicon.subsample(5, 5)
    telegram = ttk.Button(sectionframe, image=telegramimage, text="      Telegram \n\n ★★★☆☆ 3.5", width=10,
                          compound=LEFT)
    telegramdesc = "Telegram is a messaging app with a focus on speed and security, it's super-fast, simple and free. " \
                   "\nYou can use Telegram on all your devices at the same time — your messages sync " \
                   "seamlessly\nacross any number of your phones, tablets or computers. "
    telegrampack = "Telegram.TelegramDesktop"
    ##############viber###############
    vibericon = PhotoImage(file=r"images\2111705.png")
    viberimage = vibericon.subsample(8, 8)
    viber = ttk.Button(sectionframe, image=viberimage, text="      Viber \n\n ★★★★☆ 4.5", width=10, compound=LEFT)
    viberdesc = "Viber is a VoIP and instant messaging application with cross-platform capabilities that allows users " \
                "\nto exchange audio and video calls, stickers, group chats, and instant voice and video messages. " \
                "\nIt Is a product of Rakuten Viber, a multinational internet company headquartered in Setagaya-ku, " \
                "\nTokyo, Japan. "
    viberpack = "Viber.Viber"
    ###########whatsapp#############
    whatsappicon = PhotoImage(file=r"images\1753788.png")
    whatsappimage = whatsappicon.subsample(8, 8)
    whatsapp = ttk.Button(sectionframe, image=whatsappimage, text=" Whatsapp Web  \n\n ★★★★☆ 4", width=10,
                          compound=LEFT)
    whatsappdesc = "WhatsApp is a free cross-platform messaging service. It lets users of iPhone and Android " \
                   "smartphones\nand Mac and Windows PC call and exchange text, photo, audio and video messages with " \
                   "others across \nthe globe for free, regardless of the recipient's device. "
    whatsapppack = "WhatsApp.WhatsApp"
    ###########signal#############
    signalicon = PhotoImage(file=r"images\4423638.png")
    signalimage = signalicon.subsample(8, 8)
    signal = ttk.Button(sectionframe, image=signalimage, text="     Signal\n\n ★★★★☆ 4.5", width=10, compound=LEFT)
    signaldesc = "Signal is an end-to-end-encrypted instant messaging and SMS app. Users can send direct or group " \
                 "\nmessages, photos, and voice messages across multiple devices. The key advantage that it offers " \
                 "over \nsimilar apps is a strong focus on security and privacy. "
    signalpack = "OpenWhisperSystems.Signal"
    ###########messenger#############
    messengericon = PhotoImage(file=r"images\Facebook-Messenger-Icon-PNG-Clipart-Background.png")
    messengerimage = messengericon.subsample(18, 18)
    messenger = ttk.Button(sectionframe, image=messengerimage, text="    Messenger\n\n ★★★★☆ 4.8", width=10,
                           compound=LEFT)
    messengerdesc = "Messenger is used to send messages and exchange photos, videos, stickers, audio, and files, " \
                    "and also \nreact to other users' messages and interact with bots. The service also supports " \
                    "voice and video calling. "
    messengerpack = "Facebook.Messenger"
    ###########line#############
    lineicon = PhotoImage(file=r"images\124027.png")
    lineimage = lineicon.subsample(8, 8)
    line = ttk.Button(sectionframe, image=lineimage, text="        Line\n\n ★★★☆☆ 3.5", width=10, compound=LEFT)
    linedesc = "LINE is a communications application for all kinds of devices, including smartphones, PCs, " \
               "and tablets. \nOne can use this app to communicate via texts, images, video, audio, and more. LINE " \
               "also supports \nVoIP calling, and both audio and video conferencing. "
    linepack = "LINE.LINE"
    ###########snapchat#############
    snapchaticon = PhotoImage(file=r"images\snapchat-logo-png-0.png")
    snapchatimage = snapchaticon.subsample(8, 8)
    snapchat = ttk.Button(sectionframe, image=snapchatimage, text="  Snapchat Web\n\n ★★★☆☆ 3.9", width=10,
                          compound=LEFT)
    snapchatdesc = "Snapchat is a mobile app that allows users to send and receive self-destructing photos and videos. " \
                   "\nPhotos and videos taken with the app are called snaps. Snapchat uses the device's camera to " \
                   "capture \nsnaps and Wi-Fi technology to send them. "
    snapchatpack = "9PF9RTKMMQ69"
    ###########imo#############
    imoicon = PhotoImage(file=r"images\1091859.png")
    imoimage = imoicon.subsample(8, 8)
    imo = ttk.Button(sectionframe, image=imoimage, text="        Imo\n\n ★★★☆☆ 3.7", width=10, compound=LEFT)
    imodesc = "imo is a proprietary audio/video calling and instant messaging software service. It allows sending " \
              "music, \nvideo, PDFs and other files, along with various free stickers. It supports encrypted group " \
              "video and \nvoice calls with up to 20 participants. "
    imopack = "9NBLGGH4NZX6"
    ###########jitsi#############
    jitsiicon = PhotoImage(file=r"images\jitsi-icon.png")
    jitsiimage = jitsiicon.subsample(8, 8)
    jitsi = ttk.Button(sectionframe, image=jitsiimage, text="        jitsi\n\n ★★★★☆ 4.5", width=10, compound=LEFT)
    jitsidesc = "Jitsi Meet lets you stay in touch with all your teams, be they family, friends, or colleagues. Instant " \
                "video \nconferences, efficiently adapting to your scale. * Unlimited users: There are no artificial " \
                "restrictions \non the number of users or conference participants. "
    jitsipack = "Jitsi.Meet"
    ##########placement of communication apps##########
    commlists = ["dummy", discord, teams, skype, zoom, slack, telegram, viber, whatsapp, signal, messenger, line,
                 snapchat, imo, jitsi]
    commimgs = ["dummy", discordimage, teamsimage, skypeimage, zoomimage, slackimage, telegramimage, viberimage,
                whatsappimage, signalimage, messengerimage, lineimage, snapchatimage, imoimage, jitsiimage]
    commdescs = ["dummy", discorddesc, teamsdesc, skypedesc, zoomdesc, slackdesc, telegramdesc, viberdesc, whatsappdesc,
                 signaldesc, messengerdesc, linedesc, snapchatdesc, imodesc, jitsidesc]
    commpacknames = ["dummy", discordpack, teamspack, skypepack, zoompack, slackpack, telegrampack, viberpack,
                     whatsapppack, signalpack, messengerpack, linepack, snapchatpack, imopack, jitsipack]
    for i in range(2, len(commlists) * 2, 2):
        if i / 2 < len(commlists):
            button = commlists[i // 2]
            button.grid(row=0, column=i, ipady=30, ipadx=15)
            button.bind("<Button-1>", lambda event, buttonimg=commimgs[i // 2], buttonname=button.cget('text'),
                                             buttondesc=commdescs[i // 2], pckg=commpacknames[i // 2]: hoverwindow(
                event, buttonimg, buttonname, buttondesc, pckg))

    #############################################################development##################################################

    sectionframe = addapps("Development")
    for i in range(1, 38, 2):
            spacing = ttk.Label(sectionframe, text="    ")
            spacing.grid(row=0, column=i)
    ##############git###############
    giticon = PhotoImage(file=r"images\Git-Icon-1788C.png")
    gitimage = giticon.subsample(6, 6)
    git = ttk.Button(sectionframe, image=gitimage, text="      Git \n\n★★★★☆ 4.8", width=10, compound=LEFT)
    gitdesc = "Git is a free and open source distributed code management and Version control system that is \ndistributed under the GNU General Public License version 2. In addition to software version control, \nGit is used for other applications including configuration management and content management."
    gitpack = "Git.Git"
    ##############githubdesktop###############
    githubdesktopicon = PhotoImage(file=r"images\768px-Github-desktop-logo-symbol.svg.png")
    githubdesktopimage = githubdesktopicon.subsample(12, 12)
    githubdesktop = ttk.Button(sectionframe, image=githubdesktopimage, text="    Github Desktop \n\n★★★★☆ 4.5",
                               width=12, compound=LEFT)
    githubdesktopdesc = "GitHub Desktop is an application that enables you to interact with GitHub using a GUI instead of the \ncommand line or a web browser. GitHub Desktop encourages you and your team to collaborate \nusing best practices with Git and GitHub."
    githubdesktoppack = "GitHub.GitHubDesktop"
    ##############jetbrainstoolbox###############
    jetbrainstoolboxicon = PhotoImage(file=r"images\toolbox_logo_300x300.png")
    jetbrainstoolboximage = jetbrainstoolboxicon.subsample(5, 5)
    jetbrainstoolbox = ttk.Button(sectionframe, image=jetbrainstoolboximage, text="Jetbrains Toolbox \n\n★★★★☆ 4.7",
                                  width=13, compound=LEFT)
    jetbrainstoolboxdesc = "It offers free community versions of our popular Python and Java integrated development environments. \nIt provides tools for learning Python, Java, and Kotlin, designed by professional developers"
    jetbrainstoolboxpack = "JetBrains.Toolbox"
    ##############python###############
    pythonicon = PhotoImage(file=r"images\5968350.png")
    pythonimage = pythonicon.subsample(9, 9)
    python = ttk.Button(sectionframe, image=pythonimage, text="  Python \n\n★★★★☆ 4.8", width=10, compound=LEFT)
    pythondesc = "Python is a computer programming language often used to build websites and software, automate tasks, and conduct \ndata analysis. Python is a general-purpose language, meaning it can be used to create a variety of \ndifferent programs and isn't specialized for any specific problems."
    pythonpack = "9PJPW5LDXLZ5"
    ##############vscode###############
    vscodeicon = PhotoImage(file=r"images\Visual_Studio_Code_1.35_icon.svg.png")
    vscodeimage = vscodeicon.subsample(36, 36)
    vscode = ttk.Button(sectionframe, image=vscodeimage, text="  VS Code \n\n★★★★☆ 4.8", width=10, compound=LEFT)
    vscodedesc = "Visual Studio Code is a lightweight but powerful source code editor which runs on your desktop and is \navailable for Windows, macOS and Linux."
    vscodepack = "Microsoft.VisualStudioCode"
    ##############vscodium###############
    vscodiumicon = PhotoImage(file=r"images\i7zov9ca3ts71.png")
    vscodiumimage = vscodiumicon.subsample(18, 18)
    vscodium = ttk.Button(sectionframe, image=vscodiumimage, text="  VS Codium \n\n★★★★☆ 4.8", width=10, compound=LEFT)
    vscodiumdesc = "VSCodium is a community-driven, freely-licensed binary distribution of Microsoft's editor VS Code, a \nmultiplatform and multi langage source code editor."
    vscodiumpack = "VSCodium.VSCodium"
    ##############nodejs###############
    nodejsicon = PhotoImage(file=r"images\5968322.png")
    nodejsimage = nodejsicon.subsample(9, 9)
    nodejs = ttk.Button(sectionframe, image=nodejsimage, text="  Node JS \n\n★★★★☆ 4.5", width=10, compound=LEFT)
    nodejsdesc = "Node. js (Node) is an open source, cross-platform runtime environment for executing JavaScript code. \nNode is used extensively for server-side programming, making it possible for developers to use \nJavaScript for client-side and server-side code without needing to learn an additional language."
    nodejspack = "OpenJS.NodeJS"
    ##############rust###############
    rusticon = PhotoImage(file=r"images\Rust_programming_language_black_logo.svg.png")
    rustimage = rusticon.subsample(36, 36)
    rust = ttk.Button(sectionframe, image=rustimage, text="     Rust \n\n★★★★☆ 4.5", width=10, compound=LEFT)
    rustdesc = "Rust emphasizes performance, type safety, and concurrency. Rust enforces memory safety—that is, \nthat all references point to valid memory—without requiring the use of a garbage collector or reference \ncounting present in other memory-safe languages."
    rustpack = "Rustlang.Rust.GNU"
    ##############visualstudio###############
    vsstudioicon = PhotoImage(file=r"images\Visual_Studio_Icon_2022.svg.png")
    vsstudioimage = vsstudioicon.subsample(36, 36)
    vsstudio = ttk.Button(sectionframe, image=vsstudioimage, text="Visual Studio 2022 \n\n★★★★☆ 4.6", width=14,
                          compound=LEFT)
    vsstudiodesc = "Visual Studio 2022 is the best Visual Studio ever. Our first 64-bit IDE makes it easier to work \nwith even bigger projects and more complex workloads. The stuff you do every day—like typing code \nand switching branches—feels more fluid more responsive."
    vsstudiopack = "Microsoft.VisualStudio.2022.Community-Preview"
    ##############sublime###############
    sublimeicon = PhotoImage(file=r"images\download.png")
    sublimeimage = sublimeicon.subsample(4, 4)
    sublime = ttk.Button(sectionframe, image=sublimeimage, text="    Sublime \n\n★★★★☆ 4.5", width=10, compound=LEFT)
    sublimedesc = "Sublime Text is an application development software that helps businesses manage code refactoring, \ndebugging, multi-monitor editing, syntax highlighting, and more from within a unified platform."
    sublimepack = "SublimeHQ.androidstudioText.4"
    ###########androidstudio############
    androidstudioicon = PhotoImage(file=r"images\android-studio-icon-486x512-zp9um7zl.png")
    androidstudioimage = androidstudioicon.subsample(9, 9)
    androidstudio = ttk.Button(sectionframe, image=androidstudioimage, text="    Android Studio \n\n★★★★☆ 4.9",
                               width=10, compound=LEFT)
    androidstudiodesc = "Android Studio is the official integrated development environment (IDE) for Android application \ndevelopment. It is based on the IntelliJ IDEA, a Java integrated development environment for software, \nand incorporates its code editing and developer tools."
    androidstudiopack = "Google.AndroidStudio"
    #############xamarin##############
    xamarinicon = PhotoImage(file=r"images\download1.png")
    xamarinimage = xamarinicon.subsample(4, 4)
    xamarin = ttk.Button(sectionframe, image=xamarinimage, text="    Xamarin \n\n★★★★☆ 4.4", width=10, compound=LEFT)
    xamarindesc = "Xamarin is an abstraction layer that manages communication of shared code with underlying platform \ncode. Xamarin runs in a managed environment that provides conveniences such as memory allocation \nand garbage collection. Xamarin enables developers to share an average of 90% of their application \nacross platforms."
    xamarinpack = "9NBLGGH0FF9K"
    #############unity##############
    unityicon = PhotoImage(file=r"images\5969294.png")
    unityimage = unityicon.subsample(9, 9)
    unity = ttk.Button(sectionframe, image=unityimage, text="    Unity \n\n★★★★☆ 4.7", width=10, compound=LEFT)
    unitydesc = "Unity gives users the ability to create games and experiences in both 2D and 3D, and the engine \noffers a primary scripting API in C# using Mono, for both the Unity editor in the form of plugins, \nand games themselves, as well as drag and drop functionality."
    unitypack = "Unity.Unity.2022"
    #############blender##############
    blendericon = PhotoImage(file=r"images\7c3abb1e942ffcdb9a64676a0af8c65c0d4b4497.png")
    blenderimage = blendericon.subsample(12, 12)
    blender = ttk.Button(sectionframe, image=blenderimage, text="    Blender \n\n★★★★☆ 4.2", width=10, compound=LEFT)
    blenderdesc = "Blender is the Free and Open Source 3D creation suite. It supports the entirety of the 3D pipeline\n—modeling, sculpting, rigging, 3D and 2D animation, simulation, rendering, compositing, motion \ntracking and video editing."
    blenderpack = "BlenderFoundation.Blender"
    #############atom##############
    atomicon = PhotoImage(file=r"images\21752.png")
    atomimage = atomicon.subsample(9, 9)
    atom = ttk.Button(sectionframe, image=atomimage, text="    Atom \n\n★★★★☆ 4.5", width=10, compound=LEFT)
    atomdesc = "Atom is a free and open-source text and source code editor developed by GitHub (Atom – A \nHackable Text and Source Code Editor for Linux). Its developers call it a hackable text editor for the \n21st Century (Atom 1.0)."
    atompack = "GitHub.Atom"
    #############audacity##############
    audacityicon = PhotoImage(file=r"images\Audacity_Logo_nofilter.svg.png")
    audacityimage = audacityicon.subsample(36, 36)
    audacity = ttk.Button(sectionframe, image=audacityimage, text="    Audacity \n\n★★★★☆ 4.2", width=10, compound=LEFT)
    audacitydesc = "Audacity is a free, easy-to-use, multi-track audio editor and recorder for Windows, \nmacOS, GNU/Linux and other operating systems. The interface is translated into many languages. You \ncan use Audacity to: Record live audio. Record computer playback on any Windows Vista or later \nmachine."
    audacitypack = "Audacity.Audacity"
    #############gimp##############
    gimpicon = PhotoImage(file=r"images\The_GIMP_icon_-_gnome.svg.png")
    gimpimage = gimpicon.subsample(18, 18)
    gimp = ttk.Button(sectionframe, image=gimpimage, text="    GIMP \n\n★★★★☆ 4.9", width=10, compound=LEFT)
    gimpdesc = "GIMP is an acronym for GNU Image Manipulation Program. It is a freely distributed program \nfor such tasks as photo retouching, image composition and image authoring. It has many capabilities."
    gimppack = "GIMP.GIMP"
    #############kdenlive##############
    kdenliveicon = PhotoImage(file=r"images\icon_12.png")
    kdenliveimage = kdenliveicon.subsample(4, 4)
    kdenlive = ttk.Button(sectionframe, image=kdenliveimage, text="    Kdenlive \n\n★★★★☆ 4.2", width=10, compound=LEFT)
    kdenlivedesc = "Kdenlive is an open source video editor. The project was started around 2003. Kdenlive \nis built on Qt and the KDE Frameworks libraries. Most of the video processing is done by the MLT \nFramework, which relies on many other open source projects like FFmpeg, frei0r, movit, ladspa, \nsox, etc…"
    kdenlivepack = "KDE.Kdenlive"
    #############obsstudio##############
    obsstudioicon = PhotoImage(file=r"images\768px-OBS_Studio_Logo.svg.png")
    obsstudioimage = obsstudioicon.subsample(12, 12)
    obsstudio = ttk.Button(sectionframe, image=obsstudioimage, text="   OBS Studio \n\n★★★★☆ 4.5", width=10,
                           compound=LEFT)
    obsstudiodesc = "Open Broadcaster Software, or OBS, is a free and open source solution for offline video \nrecording and live streaming that is Mac and Windows compliant. With an open canvas approach to \nvideo creation this tool can mix a variety of audio and video sources to a single output for \ncreative video and broadcast applications."
    obsstudiopack = "OBSProject.OBSStudio"

    # GoLang.Go.1.19
    # Embarcadero.Dev-C++
    # Swift.Toolchain
    # Oracle.JavaRuntimeEnvironment
    ##########placement of dev apps##########
    devlists = ["dummy", git, githubdesktop, jetbrainstoolbox, python, vscode, vscodium, nodejs, rust, vsstudio,
                sublime, androidstudio, xamarin, unity, blender, atom, audacity, gimp, kdenlive, obsstudio]
    devimgs = ["dummy", gitimage, githubdesktopimage, jetbrainstoolboximage, pythonimage, vscodeimage, vscodiumimage,
               nodejsimage, rustimage, vsstudioimage, sublimeimage, androidstudioimage, xamarinimage, unityimage,
               blenderimage, atomimage, audacityimage, gimpimage, kdenliveimage, obsstudioimage]
    devdescs = ["dummy", gitdesc, githubdesktopdesc, jetbrainstoolboxdesc, pythondesc, vscodedesc, vscodiumdesc,
                nodejsdesc, rustdesc, vsstudiodesc, sublimedesc, androidstudiodesc, xamarindesc, unitydesc, blenderdesc,
                atomdesc, audacitydesc, gimpdesc, kdenlivedesc, obsstudiodesc]
    devpacknames = ["dummy", gitpack, githubdesktoppack, jetbrainstoolboxpack, pythonpack, vscodepack, vscodiumpack,
                    nodejspack, rustpack, vsstudiopack, sublimepack, androidstudiopack, xamarinpack, unitypack,
                    blenderpack, atompack, audacitypack, gimppack, kdenlivepack, obsstudiopack]

    for i in range(2, len(devlists) * 2, 2):
        if i / 2 < len(devlists):
            button = devlists[i // 2]
            button.grid(row=0, column=i, ipady=30, ipadx=15)
            button.bind("<Button-1>", lambda event, buttonimg=devimgs[i // 2], buttonname=button.cget('text'),
                                             buttondesc=devdescs[i // 2], pckg=devpacknames[i // 2]: hoverwindow(event,
                                                                                                                 buttonimg,
                                                                                                                 buttonname,
                                                                                                                 buttondesc,
                                                                                                                 pckg))
    #############################################################utilities##################################################

    sectionframe = addapps("Utilities")
    for i in range(1, 26, 2):
            spacing = ttk.Label(sectionframe, text="    ")
            spacing.grid(row=0, column=i)
    ##############################hwinfo########################
    hwinfoicon = PhotoImage(file=r"images\hwinfo-icon-512x512-8ybzko3v.png")
    hwinfoimage = hwinfoicon.subsample(8, 8)
    hwinfo = ttk.Button(sectionframe, image=hwinfoimage, text="     HW Info \n\n ★★★★☆ 4", width=10, compound=LEFT)
    hwinfodesc = "HWiNFO is an all-in-one solution for hardware analysis and monitoring supporting a broad range of \nOSes (DOS, Microsoft Windows 95 - Windows 11, WinPE) and platforms (i8086 - Xeon Platinum). \nLatest components supported."
    hwinfopack = "REALiX.HWiNFO"
    ##############################coretemp########################
    coretempicon = PhotoImage(file=r"images\34454443.png")
    coretempimage = coretempicon.subsample(5, 5)
    coretemp = ttk.Button(sectionframe, image=coretempimage, text="    Core Temp \n\n ★★★★☆ 4", width=10, compound=LEFT)
    coretempdesc = "Core Temp is a compact, no fuss, small footprint, yet powerful program to monitor processor temperature \nand other vital information. What makes Core Temp unique is the way it works. It is capable of \ndisplaying a temperature of each individual core of every processor in your system!"
    coretemppack = "ALCPU.CoreTemp"
    ##############################sevenzip########################
    sevenzipicon = PhotoImage(file=r"images\1280px-7-Zip_Icon.svg.png")
    sevenzipimage = sevenzipicon.subsample(17, 17)
    sevenzip = ttk.Button(sectionframe, image=sevenzipimage, text="         7Zip \n\n ★★★★☆ 4.3", width=10,
                          compound=LEFT)
    sevenzipdesc = "7-Zip is a free and open-source file archiver, a utility used to place groups of files within compressed \ncontainers known as archives. It is developed by Igor Pavlov and was first released in 1999. \n7-Zip has its own archive format called 7z, but can read and write several others."
    sevenzippack = "7zip.7zip"
    ##############################anydesk########################
    anydeskicon = PhotoImage(file=r"images\unnamed.png")
    anydeskimage = anydeskicon.subsample(9, 9)
    anydesk = ttk.Button(sectionframe, image=anydeskimage, text="      Anydesk \n\n ★★★★☆ 4.4", width=10, compound=LEFT)
    anydeskdesc = "AnyDesk's high-performance Remote Desktop Software enables latency-free Desktop Sharing, \nstable Remote Control and fast and secure data transmission between devices."
    anydeskpack = "AnyDeskSoftwareGmbH.AnyDesk"
    ##############################cpuz########################
    cpuzicon = PhotoImage(file=r"images\CPU-Z_Icon.svg.png")
    cpuzimage = cpuzicon.subsample(2, 2)
    cpuz = ttk.Button(sectionframe, image=cpuzimage, text="        CPU-Z \n\n ★★★★☆ 4.5", width=10, compound=LEFT)
    cpuzdesc = "CPU-Z is a freeware that gathers information on some of the main devices of your system : \nProcessor name and number, codename, process, package, cache levels. Mainboard and chipset. \nMemory type, size, timings, and module specifications (SPD). Real time measurement of each core's \ninternal frequency, memory frequency."
    cpuzpack = "CPUID.CPU-Z"
    ##############################etcher########################
    etchericon = PhotoImage(file=r"images\avatar.png")
    etcherimage = etchericon.subsample(4, 4)
    etcher = ttk.Button(sectionframe, image=etcherimage, text="Balena Etcher \n\n ★★★★☆ 4", width=10, compound=LEFT)
    etcherdesc = "balenaEtcher (commonly referred to and formerly known as Etcher) is a free and open-source \nutility used for writing image files such as . iso and . img files, as well as zipped folders \nonto storage media to create live SD cards and USB flash drives. It is developed by Balena, \nand licensed under Apache License 2.0."
    etcherpack = "Balena.Etcher"
    ##############################gpuz########################
    gpuzicon = PhotoImage(file=r"images\gpu_z_icon_by_pitmankeks_de0lyld-fullview.png")
    gpuzimage = gpuzicon.subsample(9, 9)
    gpuz = ttk.Button(sectionframe, image=gpuzimage, text="      GPU-Z \n\n ★★★☆☆ 3.6", width=10, compound=LEFT)
    gpuzdesc = "TechPowerUp GPU-Z (or just GPU-Z) is a lightweight utility designed to provide information \nabout video cards and GPUs. The program displays the specifications of Graphics Processing Unit \n(often shortened to GPU) and its memory; also displays temperature, core frequency, memory frequency, \nGPU load and fan speeds."
    gpuzpack = "TechPowerUp.GPU-Z"
    ##############################revouninstaller########################
    revouninstallericon = PhotoImage(file=r"images\Revouninstallerpro_icon.png")
    revouninstallerimage = revouninstallericon.subsample(9, 9)
    revouninstaller = ttk.Button(sectionframe, image=revouninstallerimage, text=" Revo Uninstaller \n\n ★★★☆☆ 3.5",
                                 width=12, compound=LEFT)
    revouninstallerdesc = "Revo Uninstaller acts as both a replacement and a supplement to the built-in functionality \nin Windows by first running the built-in uninstaller for the program, and then scanning \nfor leftover data afterwards, making it your best choice when it comes to completely \nremove stubborn programs, temporary files, and other unnecessary program data that is \nleft behind after the standard uninstall process."
    revouninstallerpack = "RevoUninstaller.RevoUninstaller"
    ##############################powertoys########################
    powertoysicon = PhotoImage(file=r"images\2020_PowerToys_Icon.svg.png")
    powertoysimage = powertoysicon.subsample(36, 36)
    powertoys = ttk.Button(sectionframe, image=powertoysimage, text="      Powertoys \n\n ★★★★☆ 4.5", width=12,
                           compound=LEFT)
    powertoysdesc = "Microsoft PowerToys is a set of utilities for power users to tune and streamline their Windows \nexperience for greater productivity."
    powertoyspack = "Microsoft.PowerToys"
    ##############################autohotkey########################
    autohotkeyicon = PhotoImage(file=r"images\sBnPQRG.png")
    autohotkeyimage = autohotkeyicon.subsample(5, 5)
    autohotkey = ttk.Button(sectionframe, image=autohotkeyimage, text="    Autohotkey \n\n ★★★★☆ 4.4", width=12,
                            compound=LEFT)
    autohotkeydesc = "AutoHotkey is a free and open-source custom scripting language for Microsoft Windows, initially \naimed at providing easy keyboard shortcuts or hotkeys, fast macro-creation and software \nautomation that allows users of most levels of computer skill to automate repetitive \ntasks in any Windows application."
    autohotkeypack = "Lexikos.AutoHotkey"
    ##############################bitwarden########################
    bitwardenicon = PhotoImage(file=r"images\1200x630bb.png")
    bitwardenimage = bitwardenicon.subsample(11, 11)
    bitwarden = ttk.Button(sectionframe, image=bitwardenimage, text="     Bitwarden \n\n ★★★★☆ 4", width=12,
                           compound=LEFT)
    bitwardendesc = "Generate, consolidate, and autofill strong and secure passwords for all your accounts. Bitwarden \ngives you power to create and manage unique passwords, so you can strengthen privacy and \nboost productivity online from any device or location."
    bitwardenpack = "Bitwarden.Bitwarden"
    ##############################everythingsearch########################
    everythingsearchicon = PhotoImage(file=r"images\dbc1fc0d2b9e238f5863eb19ef214629.png")
    everythingsearchimage = everythingsearchicon.subsample(5, 5)
    everythingsearch = ttk.Button(sectionframe, image=everythingsearchimage, text="Everything search \n\n ★★★★☆ 4",
                                  width=14, compound=LEFT)
    everythingsearchdesc = "Everything is a search engine for Windows that replaces ordinary Windows search with a \nconsiderably faster one. Unlike Windows search, Everything initially displays every file and \nfolder on your computer. You can type in a search filter to limit what files and folders are displayed."
    everythingsearchpack = "voidtools.Everything"
    ################passwordmanager###########
    '''passwordmanagericon= PhotoImage(file = r"images\b8ac5e46-1a16-448b-9a12-bf597a95d173.png")
    passwordmanagerimage = passwordmanagericon.subsample(11,11)
    passwordmanagerurl="https://github.com/VarunAdhityaGB/Password-Manager-GUI/releases/download/v.1.2/Password_Manager_v.1.2_Setup.exe"
    passwordmanagerpath="downloads//passwordmanager.exe"
    passwordmanagerfile="downloads\\passwordmanager.exe"
    passwordmanager=ttk.Button(utilitiessectionframe,image=passwordmanagerimage,text="Password Manager \n\n ★★★★☆ 4",width=15,compound=LEFT,command=lambda: [urlinstall(passwordmanagerurl,passwordmanagerpath,passwordmanagerfile,"passwordmanager")])
    '''
    ################flux###########
    fluxicon = PhotoImage(file=r"images\flux-icon-big.png")
    fluximage = fluxicon.subsample(5, 5)
    flux = ttk.Button(sectionframe, image=fluximage, text="        Flux \n\n ★★★★☆ 4.8", width=12, compound=LEFT)
    fluxdesc = "lux (pronounced flux) is a cross-platform computer program that adjusts a display's color temperature \naccording to location and time of day, offering functional respite for the eyes. The program \nis designed to reduce eye strain during night-time use, helping to reduce disruption of sleep patterns."
    fluxpack = "flux.flux"
    ##########placement of dev apps##########
    utillists = ["dummy", hwinfo, coretemp, sevenzip, anydesk, cpuz, etcher, gpuz, revouninstaller, powertoys,
                 autohotkey, bitwarden, everythingsearch, flux]
    utilimgs = ["dummy", hwinfoimage, coretempimage, sevenzipimage, anydeskimage, cpuzimage, etcherimage, gpuzimage,
                revouninstallerimage, powertoysimage, autohotkeyimage, bitwardenimage, everythingsearchimage, fluximage]
    utildescs = ["dummy", hwinfodesc, coretempdesc, sevenzipdesc, anydeskdesc, cpuzdesc, etcherdesc, gpuzdesc,
                 revouninstallerdesc, powertoysdesc, autohotkeydesc, bitwardendesc, everythingsearchdesc, fluxdesc]
    utilpacknames = ["dummy", hwinfopack, coretemppack, sevenzippack, anydeskpack, cpuzpack, etcherpack, gpuzpack,
                     revouninstallerpack, powertoyspack, autohotkeypack, bitwardenpack, everythingsearchpack, fluxpack]

    for i in range(2, len(utillists) * 2, 2):
        if i / 2 < len(utillists):
            button = utillists[i // 2]
            button.grid(row=0, column=i, ipady=30, ipadx=15)
            button.bind("<Button-1>", lambda event, buttonimg=utilimgs[i // 2], buttonname=button.cget('text'),
                                             buttondesc=utildescs[i // 2], pckg=utilpacknames[i // 2]: hoverwindow(
                event, buttonimg, buttonname, buttondesc, pckg))

    ##################################################Games###########################################

    sectionframe = addapps("Games")
    for i in range(1, 16, 2):
            spacing = ttk.Label(sectionframe, text="    ")
            spacing.grid(row=0, column=i)
    ###############steam#############
    steamicon = PhotoImage(file=r"images\Steam_icon_logo.svg.png")
    steamimage = steamicon.subsample(36, 36)
    steam = ttk.Button(sectionframe, image=steamimage, text="     Steam \n\n ★★★★☆ 4.3", width=10, compound=LEFT)
    steamdesc = "Steam is a video game digital distribution service and storefront by Valve. It was launched as a software \nclient in September 2003 as a way for Valve to provide automatic updates for their games, and \nexpanded to distributing and offering third-party game publishers' titles in late 2005."
    steampack = "Valve.Steam"
    ###############EpicGames#############
    EpicGamesicon = PhotoImage(file=r"images\epic-games-icon-512x512-7qpmojcd.png")
    EpicGamesimage = EpicGamesicon.subsample(9, 9)
    EpicGames = ttk.Button(sectionframe, image=EpicGamesimage, text="  Epic Games \n\n ★★★★☆ 4", width=10,
                           compound=LEFT)
    EpicGamesdesc = "Founded in 1991, Epic Games is an American company founded by CEO Tim Sweeney. The company \nis headquartered in Cary, North Carolina and has more than 40 offices worldwide. Today Epic is a \nleading interactive entertainment company and provider of 3D engine technology."
    EpicGamespack = "EpicGames.EpicGamesLauncher"
    ###############EA#############
    EAicon = PhotoImage(file=r"images\732012.png")
    EAimage = EAicon.subsample(9, 9)
    EA = ttk.Button(sectionframe, image=EAimage, text=" Electronic Arts \n\n ★★★★☆ 4", width=10, compound=LEFT)
    EAdesc = "The EA app for Windows is Electronic Arts’ all new, enhanced PC platform, where you can easily play \nyour favorite games. The app provides a streamlined and optimized user interface that gets you \ninto your games faster than ever before."
    EApack = "ElectronicArts.EADesktop"
    ############GOG#############
    GOGicon = PhotoImage(file=r"images\gog_galaxy_macos_bigsur_icon_190152.png")
    GOGimage = GOGicon.subsample(9, 9)
    GOG = ttk.Button(sectionframe, image=GOGimage, text="  GOG-Galaxy \n\n ★★★★☆ 4", width=10, compound=LEFT)
    GOGdesc = "GOG.com is a digital distribution platform – an online store with a curated selection of games, an \noptional gaming client giving you freedom of choice, and a vivid community of gamers. Hand-\npicking the best in gaming. Customer-first approach. Gamer-friendly platform."
    GOGpack = "GOG.Galaxy"
    ############playnite#############
    playniteicon = PhotoImage(file=r"images\applogo.png")
    playniteimage = playniteicon.subsample(5, 5)
    playnite = ttk.Button(sectionframe, image=playniteimage, text="    Playnite \n\n ★★★★☆ 4", width=10, compound=LEFT)
    playnitedesc = "Playnite is an open source video game library manager with one simple goal: To provide a unified \ninterface for all of your games. Download. Windows 7 and newer supported Changelog."
    playnitepack = "Playnite.Playnite"
    ############amazongames#############
    amazongamesicon = PhotoImage(file=r"images\games-float.png")
    amazongamesimage = amazongamesicon.subsample(9, 9)
    amazongames = ttk.Button(sectionframe, image=amazongamesimage, text="   AmazonGames\n\n ★★★★☆ 4", width=10,
                             compound=LEFT)
    amazongamesdesc = "Amazon Games (formerly Amazon Game Studios) is an American video game company and division of the \nonline retailing company Amazon that primarily focuses on publishing video games \ndeveloped within the company's development divisions."
    amazongamespack = "Amazon.Games"
    ############GeForce#############
    GeForceicon = PhotoImage(file=r"images\d9yeb7n-e1c9d052-ef39-499a-b23d-6ad146356ed2.png")
    GeForceimage = GeForceicon.subsample(5, 5)
    GeForce = ttk.Button(sectionframe, image=GeForceimage, text="  Nvidea GeForce \n\n ★★★★☆ 4", width=10,
                             compound=LEFT)
    GeForcedesc = "NVIDIA GeForce NOW™ transforms your device into a powerful PC gaming rig. Gamers can play PC titles they \nalready own or purchase new games from popular digital stores like Steam, Epic Games \nStore, Ubisoft Connect, and EA. Access 1500+ games, with more released every GFN Thursday."
    GeForcepack = "Nvidia.GeForceNow"
    ############ubisoftconnect#############
    ubisoftconnecticon = PhotoImage(file=r"images\Ubisoft_logo.svg.png")
    ubisoftconnectimage = ubisoftconnecticon.subsample(11, 11)
    ubisoftconnect = ttk.Button(sectionframe, image=ubisoftconnectimage, text=" Ubisoft Connect \n\n ★★★★☆ 4", width=10,
                             compound=LEFT)
    ubisoftconnectdesc = "Ubisoft Connect is the ecosystem of players services for Ubisoft games across all platforms. \nIt aims at giving the best environment for all players to enjoy their games and connect \nwith each other whatever the device. Ubisoft Connect is a free service available on all devices."
    ubisoftconnectpack = "Ubisoft.Connect"

    ##########placement of game apps##########
    gamelists = ["dummy", steam, EpicGames, EA, GOG, playnite, amazongames,GeForce,ubisoftconnect]
    gameimgs = ["dummy", steamimage, EpicGamesimage, EAimage, GOGimage, playniteimage, amazongamesimage,GeForceimage,ubisoftconnectimage]
    gamedescs = ["dummy", steamdesc, EpicGamesdesc, EAdesc, GOGdesc, playnitedesc, amazongamesdesc,GeForcedesc,ubisoftconnectdesc]
    gamepacknames = ["dummy", steampack, EpicGamespack, EApack, GOGpack, playnitepack, amazongamespack,GeForcepack,ubisoftconnectpack]

    for i in range(2, len(gamelists) * 2, 2):
        if i / 2 < len(gamelists):
            button = gamelists[i // 2]
            button.grid(row=0, column=i, ipady=30, ipadx=15)
            button.bind("<Button-1>", lambda event, buttonimg=gameimgs[i // 2], buttonname=button.cget('text'),
                                             buttondesc=gamedescs[i // 2], pckg=gamepacknames[i // 2]: hoverwindow(
                event, buttonimg, buttonname, buttondesc, pckg))

    #####################################spacing for magic :} ##########################################   
    spacing = ttk.Label(second_frame,
                        text="                                                                                                                                                                                                                                                                                                                                 ")
    spacing.grid(row=100, column=0)

    #################search##############
    search = StringVar()
    searchentry= ttk.Entry(window,textvariable=search,width=30)
    searchentry.config(state='normal')
    searchentry.focus()
    searchentry.insert(0,"Search:-")
    searchentry.place(relx=0.41,rely=0.05)
    searchicon= PhotoImage(file = r"images\search.png")
    searchimage = searchicon.subsample(25,25)
    searchbutton =ttk.Button(window,image=searchimage)
    searchbutton.place(relx=0.605,rely=0.05)
    
    main.mainloop()

mainsplash.after(3000, mainwindow)
mainsplash.mainloop()
