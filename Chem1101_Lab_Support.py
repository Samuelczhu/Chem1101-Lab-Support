from tkinter import *
import tkinter.messagebox
import math

root = Tk()
root.geometry("500x400")
root.title("Chemistry Lab Helper")
root.iconbitmap("icon.ico")

#************Menu**************
menu = Menu(root)
root.config(menu=menu)

mainmenu = Menu(menu)
menu.add_cascade(label="Main",menu=mainmenu)
mainmenu.add_command(label="Message",command=lambda: message(root))
mainmenu.add_command(label="Periodic Tabel",command=lambda: table(root))
mainmenu.add_command(label="Exit",command=root.quit)

calmenu = Menu(menu)
menu.add_cascade(label="Calorimetry",menu=calmenu)
calmenu.add_command(label="Heat of Solution for Salt",command=lambda: heat(root))
calmenu.add_command(label="Heat Capacity of Calorimeter",command=lambda: heatcap(root))
calmenu.add_command(label="Percent Error",command=lambda: error(root))

gravmenu = Menu(menu)
menu.add_cascade(label="Gravimetric",menu=gravmenu)
gravmenu.add_command(label="AgCl Lost",command=lambda: magcll(root))
gravmenu.add_command(label="Precipitation",command=lambda: precip(root))

specmenu = Menu(menu)
menu.add_cascade(label="Spectrophotometry",menu=specmenu)
specmenu.add_command(label="Dilution Factor",command=lambda: dilfact(root))
specmenu.add_command(label="Diluted Solution needed",command=lambda: voldilution(root))

titratemenu = Menu(menu)
menu.add_cascade(label="Titration",menu=titratemenu)
titratemenu.add_command(label="pH for CH3COONa",command=lambda: ch3coona(root))
titratemenu.add_command(label="Strong Acid-Base",command=lambda: strong(root))
titratemenu.add_command(label="Weak Acid-Strong Base",command=lambda: weak(root))
titratemenu.add_command(label="Percent Error",command=lambda: error(root))

#**********Message************
def message(root):
    eraser = Label(root,width=500,height=350)
    eraser.place(x=250,y=200,anchor=CENTER)

    welcome1 = Label(root,text="Welcome",fg="red",font=("arial",17,"bold"))
    welcome1.place(x=250,y=20,anchor=CENTER)
    welcome2 = Label(root,text="to",fg="red",font=("arial",12,"bold"))
    welcome2.place(x=250,y=50,anchor=CENTER)
    welcome3 = Label(root,text="CHEM 1101 Lab",fg="blue",font=("arial",23,"bold"))
    welcome3.place(x=250,y=80,anchor=CENTER)
    welcome4 = Label(root,text="support",fg="green",font=("arial",15,"bold"))
    welcome4.place(x=250,y=115,anchor=CENTER)

    global image1
    image1 = PhotoImage(file="image1.png")
    imagelabel = Label(root, image=image1)
    imagelabel.place(x=250,y=320,anchor=CENTER)

    text1 = Label(root,text="*This programme meant to help your calculations in Chem 1101 labs.",fg="purple",font=("helvetica",10))
    text1.place(x=50,y=150)
    text2 = Label(root,text="*Do not depend fully on this programme.",fg="purple",font=("helvetica",10))
    text2.place(x=50,y=175)
    text3 = Label(root,text="-This programme may contain some errors.",fg="purple",font=("helvetica",10))
    text3.place(x=100,y=200)
    text4 = Label(root,text="-If you depend too much on this programme,\n    you will probably not learn many things.",fg="purple",font=("helvetica",10))
    text4.place(x=100,y=225)

    quitbutton = Button(root,text="EXIT",fg="brown",command=root.quit)
    quitbutton.place(x=400,y=325)

    statusbar = Label(root,text="Choose the lab calculators in the Menu.",bd=1,relief=SUNKEN,anchor=W,width=500)
    statusbar.place(y=380)
message(root)


#**********Periodic_table***********
def table(root):
    eraser = Label(root,width=500,height=350)
    eraser.place(x=250,y=200,anchor=CENTER)

    global image2
    image2 = PhotoImage(file="image2.png")
    imagelabel = Label(root,image=image2)
    imagelabel.place(x=250,y=200,anchor=CENTER)

    statusbar = Label(root,text="This is the Periodic Table.",bd=1,relief=SUNKEN,anchor=W,width=500)
    statusbar.place(y=380)


#*******Heat_of_solution_for_salt*****
def heat(root):
    eraser = Label(root,width=500,height=350)
    eraser.place(x=250,y=200,anchor=CENTER)

    title = Label(root,text="Heat of Solution for Salts",fg="firebrick",font=("arial",18,"bold"))
    title.place(x=250,y=30,anchor=CENTER)

    mh2olabel = Label(root,text="Mass of Water (g)",fg="blue",font=("helvetica",11))
    mh2olabel.place(x=50,y=72,anchor=W)
    data1 = StringVar()
    mh2o = Entry(root,textvariable=data1)
    mh2o.place(x=230,y=72,anchor=W)

    msaltlabel = Label(root,text="Mass of Salt (g)",fg="blue",font=("helvetica",11))
    msaltlabel.place(x=50,y=103,anchor=W)
    data2 = StringVar()
    msalt = Entry(root,textvariable=data2)
    msalt.place(x=230,y=103,anchor=W)

    hcoclabel = Label(root,text="Heat Capacity of Calorimeter (J/°C)",fg="blue",font=("helvetica",11))
    hcoclabel.place(x=30,y=134,anchor=W)
    data3 = StringVar()
    hcoc = Entry(root,width=10,textvariable=data3)
    hcoc.place(x=300,y=134,anchor=W)

    temperaturelabel = Label(root,text="Temperature (°C)",fg="red",font=("helvetica",15))
    temperaturelabel.place(x=250,y=170,anchor=CENTER)
    inittemp = Label(root,text="Initial",fg="green",font=("helvetica",13))
    inittemp.place(x=130,y=190,anchor=CENTER)
    finaltemp = Label(root,text="Final",fg="green",font=("helvetica",13))
    finaltemp.place(x=370,y=190,anchor=CENTER)
    th2olabel1 = Label(root,text="Water",fg="blue",font=("helvetica",11))
    th2olabel1.place(x=50,y=210)
    data4 = StringVar()
    th2o1 = Entry(root,width=10,textvariable=data4)
    th2o1.place(x=100,y=210)
    th2olabel2 = Label(root,text="Water",fg="blue",font=("helvetica",11))
    th2olabel2.place(x=285,y=210)
    data5 = StringVar()
    th2o2 = Entry(root,width=10,textvariable=data5)
    th2o2.place(x=335,y=210)
    callabel1 = Label(root,text="Calorimeter",fg="blue",font=("helvetica",11))
    callabel1.place(x=15,y=235)
    data6 = StringVar()
    cal1 = Entry(root,width=10,textvariable=data6)
    cal1.place(x=100,y=235)
    callabel2 = Label(root,text="Calorimeter",fg="blue",font=("helvetica",11))
    callabel2.place(x=250,y=235)
    data7 = StringVar()
    cal2 = Entry(root,width=10,textvariable=data7)
    cal2.place(x=335,y=235)

    calculate = Button(root,text="Calculate",fg="orange",font=("arial",13),command=lambda: cal(root))
    calculate.place(x=230,y=280,anchor=CENTER)

    def cal(root):
        eraser = Label(root,width=100,height=4)
        eraser.place(x=250,y=340,anchor=CENTER)

        try:
            ch2o = 4.184
            mh2o = eval(data1.get())
            msalt = eval(data2.get())
            qcal = eval(data3.get())
            tih2o = eval(data4.get())
            tfh2o = eval(data5.get())
            tical = eval(data6.get())
            tfcal = eval(data7.get())

            numkj = (1/1000)*(ch2o*(mh2o+msalt)*(tih2o-tfh2o)+qcal*(tical-tfcal))
            numkj = round(numkj,4)
            ans = Label(root,text=str(numkj)+" "+"KJ",fg="purple",font=("arial",12))
            ans.place(x=235,y=325,anchor=CENTER)
        except:
            ans = Label(root,text="Wrong Input",fg="purple",font=("arial",12))
            ans.place(x=235,y=325,anchor=CENTER)
            tkinter.messagebox.showinfo("Warning","Please enter valid input.")

    statusbar = Label(root,text="Please enter the values above.",bd=1,relief=SUNKEN,anchor=W,width=500)
    statusbar.place(y=380)


#************Percent_Error************
def error(root):
    eraser = Label(root,width=500,height=350)
    eraser.place(x=250,y=200,anchor=CENTER)

    global image3
    image3 = PhotoImage(file="image3.png")
    imagelabel = Label(root, image=image3)
    imagelabel.place(x=240, y=323, anchor=CENTER)

    title = Label(root,text="Percent Error",fg="red",font=("arial",20,"bold"))
    title.place(x=250,y=30,anchor=CENTER)

    explabel = Label(root,text="Experimental value:",fg="blue",font=("helvetica",13))
    explabel.place(x=50,y=100,anchor=W)
    data1 = StringVar()
    exp = Entry(root,textvariable=data1)
    exp.place(x=225,y=100,anchor=W)
    theolabel = Label(root,text="Theoretical value:",fg="blue",font=("helvetica",13))
    theolabel.place(x=50,y=135,anchor=W)
    data2 = StringVar()
    theo = Entry(root,textvariable=data2)
    theo.place(x=225,y=135,anchor=W)

    calculate = Button(root,text="Calculate",fg="orange",font=("arial",13),command=lambda: cal(root))
    calculate.place(x=230,y=185,anchor=CENTER)

    def cal(root):
        eraser = Label(root,width=100,height=3)
        eraser.place(x=250,y=235,anchor=CENTER)

        try:
            numexp = eval(data1.get())
            numtheo = eval(data2.get())

            pererror = abs((numexp-numtheo)/numtheo)*100
            pererror = round(pererror,4)
            ans = Label(root,text="%Error = "+str(pererror),fg="purple",font=("arial",12))
            ans.place(x=230,y=235,anchor=CENTER)
        except:
            ans = Label(root,text="Wrong Input",fg="purple",font=("arial",12))
            ans.place(x=230,y=235,anchor=CENTER)
            tkinter.messagebox.showinfo("Warning", "Please enter valid input.")

    statusbar = Label(root,text="The percent error is calculated by (#experimental-#theoretical) ÷ (#theoretical) × 100.",bd=1,relief=SUNKEN,anchor=W,width=500)
    statusbar.place(y=380)


#***********Heat_Capacity***********
def heatcap(root):
    eraser = Label(root,width=500,height=350)
    eraser.place(x=250,y=200,anchor=CENTER)

    title1 = Label(root,text="Heat Capacity",fg = "orange red",font=("arial",20,"bold"))
    title1.place(x=250,y=30,anchor=CENTER)
    title2 = Label(root,text="of the",fg="green",font=("arial",12))
    title2.place(x=250,y=60,anchor=CENTER)
    title3 = Label(root,text="Calorimeter",fg="dark orchid",font=("arial",17,"bold"))
    title3.place(x=250,y=90,anchor=CENTER)

    original = Label(root,text="Original",fg="snow4",font=("helvetica",15))
    original.place(x=100,y=120,anchor=CENTER)
    mwaterlabel1 = Label(root,text="Mass of water (g)",fg="blue",font=("helvetica",11))
    mwaterlabel1.place(x=50,y=160,anchor=W)
    data1 = StringVar()
    mwater1 = Entry(root,width=7,textvariable=data1)
    mwater1.place(x=175,y=160,anchor=W)
    templabel1 = Label(root,text="Temperature of both (°C)",fg="blue",font=("helvetica",11))
    templabel1.place(x=5,y=200,anchor=W)
    data2 = StringVar()
    temp1 = Entry(root,width=7,textvariable=data2)
    temp1.place(x=175,y=200,anchor=W)

    pour = Label(root,text="Pour In",fg="snow4",font=("helvetica",15))
    pour.place(x=360,y=120,anchor=CENTER)
    mwaterlabel2 = Label(root,text="Mass of water (g)",fg="blue",font=("helvetica",11))
    mwaterlabel2.place(x=300,y=160,anchor=W)
    data3 = StringVar()
    mwater2 = Entry(root,width=7,textvariable=data3)
    mwater2.place(x=430,y=160,anchor=W)
    templabel2 = Label(root,text="Temperature of water (°C)",fg="blue",font=("helvetica",11))
    templabel2.place(x=250,y=200,anchor=W)
    data4 = StringVar()
    temp2 = Entry(root,width=7,textvariable=data4)
    temp2.place(x=430,y=200,anchor=W)

    finaltemplabel = Label(root,text="Final Temperature (°C)",fg="blue",font=("helvetica",11))
    finaltemplabel.place(x=70,y=245,anchor=W)
    data5 = StringVar()
    finaltemp = Entry(root,textvariable=data5)
    finaltemp.place(x=240,y=245,anchor=W)

    calculate = Button(root,text="Calculate",fg="orange",font=("arial",13),command=lambda: cal(root))
    calculate.place(x=250,y=290,anchor=CENTER)

    def cal(root):
        eraser = Label(root,width=100,height=3)
        eraser.place(x=250,y=335,anchor=CENTER)

        try:
            ch2o = 4.186
            omh2o = eval(data1.get())
            ti = eval(data2.get())
            pmh2o = eval(data3.get())
            tp = eval(data4.get())
            tf = eval(data5.get())

            ccal = (ch2o*pmh2o*(tp-tf)-ch2o*omh2o*(tf-ti))/(tf-ti)
            ccal = round(ccal,4)
            ans = Label(root,text=str(ccal)+" J/°C",fg="purple",font=("arial",13))
            ans.place(x=250,y=335,anchor=CENTER)
        except:
            ans = Label(root,text="Wrong Input",fg="purple",font=("arial",13))
            ans.place(x=250,y=335,anchor=CENTER)
            tkinter.messagebox.showinfo("Warning", "Please enter valid input.")

    statusbar = Label(root,text="Please enter the values above.",bd=1,relief=SUNKEN,anchor=W,width=500)
    statusbar.place(y=380)


#************Mass_of_AgCl_Losted**********
def magcll(root):
    eraser = Label(root,width=500,height=350)
    eraser.place(x=250,y=200,anchor=CENTER)

    global image4
    image4 = PhotoImage(file="image4.png")
    imagelabel = Label(root,image=image4)
    imagelabel.place(x=250, y=300, anchor=CENTER)

    title = Label(root,text="Mass of AgCl Lost",fg="cornflower blue",font=("arial",20,"bold"))
    title.place(x=250,y=30,anchor=CENTER)

    volwwlabel = Label(root,text="Volume of washing water (mL)",fg="blue",font=("helvetica",12))
    volwwlabel.place(x=40,y=100,anchor=W)
    data1 = StringVar()
    volww = Entry(root,textvariable=data1)
    volww.place(x=260,y=100,anchor=W)

    calculate = Button(root,text="Calculate",fg="orange",font=("arial",13),command=lambda: cal(root))
    calculate.place(x=250,y=150,anchor=CENTER)

    def cal(root):
        eraser = Label(root,width=100,height=3)
        eraser.place(x=250,y=200,anchor=CENTER)

        try:
            ksp = 1.6*10**(-10)
            mwagcl = 143.2
            vml = eval(data1.get())

            lost = vml/1000 * math.sqrt(ksp)*mwagcl
            ans = Label(root,text=str(lost)+" g",fg="purple",font=("arial",15))
            ans.place(x=250,y=200,anchor=CENTER)
        except:
            ans = Label(root,text="Wrong Input",fg="purple",font=("arial",15))
            ans.place(x=250,y=200,anchor=CENTER)
            tkinter.messagebox.showinfo("Warning", "Please enter valid input.")

    statusbar = Label(root,text="Ksp for silver chloride is 1.60 × 10^-10.",bd=1,relief=SUNKEN,anchor=W,width=500)
    statusbar.place(y=380)


#***************Precipitation***************
def precip(root):
    eraser = Label(root,width=500,height=350)
    eraser.place(x=250,y=200,anchor=CENTER)

    title1 = Label(root,text="Volume of Silver Nitrate",fg="navy",font=("arial",20,"bold"))
    title1.place(x=250,y=30,anchor=CENTER)
    title2 = Label(root,text="needed for",fg="red2",font=("arial",11,"bold"))
    title2.place(x=250,y=60,anchor=CENTER)
    title3 = Label(root,text="Precipitation",fg="slate blue",font=("arial",17,"bold"))
    title3.place(x=250,y=90,anchor=CENTER)

    smlabel = Label(root,text="Sample Mass (g)",fg="blue",font=("helvetica",11))
    smlabel.place(x=170,y=150,anchor=W)
    data1 = StringVar()
    sm = Entry(root,textvariable=data1)
    sm.place(x=290,y=150,anchor=W)
    smpclabel = Label(root,text="Sample Mass of Percent of Chloride (%)",fg="blue",font=("helvetica",11))
    smpclabel.place(x=20,y=180,anchor=W)
    data2 = StringVar()
    smpc = Entry(root,textvariable=data2)
    smpc.place(x=290,y=180,anchor=W)
    msnlabel = Label(root,text="Molarity of Silver Nitrate (M)",fg="blue",font=("helvetica",11))
    msnlabel.place(x=105,y=210,anchor=W)
    data3 = StringVar()
    msn = Entry(root,textvariable=data3)
    msn.place(x=290,y=210,anchor=W)

    calculate = Button(root,text="Calculate",fg="orange",font=("arial",13),command=lambda: cal(root))
    calculate.place(x=250,y=260,anchor=CENTER)

    def cal(root):
        eraser = Label(root,width=100,height=3)
        eraser.place(x=250,y=310,anchor=CENTER)

        try:
            msam = eval(data1.get())
            smpc = eval(data2.get())/100
            molsn = eval(data3.get())

            vml = (smpc*msam/35.45)/molsn * 1000
            vml = round(vml,4)
            ans = Label(root,text=str(vml)+" mL",fg="purple",font=("arial",13))
            ans.place(x=250,y=310,anchor=CENTER)
        except:
            ans = Label(root,text="Wrong Input",fg="purple",font=("arial",13))
            ans.place(x=250,y=310,anchor=CENTER)
            tkinter.messagebox.showinfo("Warning", "Please enter valid input.")

    statusbar = Label(root,text="Please enter the values above.",bd=1,relief=SUNKEN,anchor=W,width=500)
    statusbar.place(y=380)


#**********Dilution_Factor**************
def dilfact(root):
    eraser = Label(root,width=500,height=350)
    eraser.place(x=250,y=200,anchor=CENTER)

    global image5
    image5 = PhotoImage(file="image5.png")
    imagelabel = Label(root,image=image5)
    imagelabel.place(x=250, y=320, anchor=CENTER)


    title = Label(root,text="Dilution Factor",fg="green3",font=("arial",20,"bold"))
    title.place(x=250,y=30,anchor=CENTER)

    pipetlabel = Label(root,text="Pipette Volume (mL)",fg="blue",font=("helvetica",11))
    pipetlabel.place(x=80,y=95,anchor=W)
    data1 = StringVar()
    pipet = Entry(root,textvariable=data1)
    pipet.place(x=230,y=95,anchor=W)
    dilutelabel = Label(root,text="Dilute Volume  (mL)",fg="blue",font=("helvetica",11))
    dilutelabel.place(x=80,y=135,anchor=W)
    data2 = StringVar()
    dilute = Entry(root,textvariable=data2)
    dilute.place(x=230,y=135,anchor=W)

    calculate = Button(root,text="Calculate",fg="orange",font=("arial",13),command=lambda: cal(root))
    calculate.place(x=250,y=180,anchor=CENTER)

    def cal(root):
        eraser = Label(root,width=100,height=3)
        eraser.place(x=250,y=225,anchor=CENTER)

        try:
            vp = eval(data1.get())
            vf = eval(data2.get())

            df = vf/vp
            df = round(df,4)
            ans = Label(root,text=str(df),fg="purple",font=("arial",13))
            ans.place(x=250,y=225,anchor=CENTER)
        except:
            ans = Label(root,text="Wrong Input",fg="purple",font=("arial",13))
            ans.place(x=250,y=225,anchor=CENTER)
            tkinter.messagebox.showinfo("Warning", "Please enter valid input.")

    statusbar = Label(root,text="Times up the dilution factors to get the final dilution factor.",bd=1,relief=SUNKEN,anchor=W,width=500)
    statusbar.place(y=380)


#***********Diluted_Solution_needed**********
def voldilution(root):
    eraser = Label(root,width=500,height=350)
    eraser.place(x=250,y=200,anchor=CENTER)

    title1 = Label(root,text="Volume of Diluted Solution",fg="SpringGreen4",font=("arial",20,"bold"))
    title1.place(x=250,y=30,anchor=CENTER)
    title2 = Label(root,text="needed",fg="orange red",font=("arial",12,"bold"))
    title2.place(x=250,y=60,anchor=CENTER)

    csislabel = Label(root,text="Concentration of Standard Iron Solution (g/L)",fg="blue",font=("helvetica",11))
    csislabel.place(x=30,y=130,anchor=W)
    data1 = StringVar()
    csis = Entry(root,width=15,textvariable=data1)
    csis.place(x=330,y=130,anchor=W)

    pipetlabel1 = Label(root,text="Pipette",fg="blue",font=("helvetica",11))
    pipetlabel1.place(x=50,y=170,anchor=W)
    data2 = StringVar()
    pipet1 = Entry(root,width=7,textvariable=data2)
    pipet1.place(x=105,y=170,anchor=W)
    pipetlabel2 = Label(root,text="mL  into a",fg="blue",font=("helvetica",11))
    pipetlabel2.place(x=160,y=170,anchor=W)
    data3 = StringVar()
    pipet2 = Entry(root,width=7,textvariable=data3)
    pipet2.place(x=240,y=170,anchor=W)
    pipetlabel3 = Label(root,text="mL  volumetric flask",fg="blue",font=("helvetica",11))
    pipetlabel3.place(x=300,y=170,anchor=W)

    masslabel = Label(root,text="Mass of iron needed (mg)",fg="blue",font=("helvetica",11))
    masslabel.place(x=50,y=210,anchor=W)
    data4 = StringVar()
    mass = Entry(root,textvariable=data4)
    mass.place(x=230,y=210,anchor=W)

    calculate = Button(root,text="Calculate",fg="orange",font=("arial",13),command=lambda: cal(root))
    calculate.place(x=250,y=270,anchor=CENTER)

    def cal(root):
        eraser = Label(root,width=100,height=3)
        eraser.place(x=250,y=320,anchor=CENTER)

        try:
            cs = eval(data1.get())
            vp = eval(data2.get())
            vv = eval(data3.get())
            min = eval(data4.get())

            vn = min*vv/(cs*vp)
            vn = round(vn,4)
            ans = Label(root,text="Volume of diluted solution needed: "+str(vn)+" mL",fg="purple",font=("arial",13))
            ans.place(x=250,y=320,anchor=CENTER)
        except:
            ans = Label(root,text="Wrong Input",fg="purple",font=("arial",13))
            ans.place(x=250,y=320,anchor=CENTER)
            tkinter.messagebox.showinfo("Warning", "Please enter valid input.")

    statusbar = Label(root,text="Please enter the values above.",bd=1,relief=SUNKEN,anchor=W,width=500)
    statusbar.place(y=380)


#************PH_for_CH3COOH(aq)************
def ch3coona(root):
    eraser = Label(root,width=500,height=350)
    eraser.place(x=250,y=200,anchor=CENTER)

    global image6
    image6 = PhotoImage(file="image6.png")
    imagelabel = Label(root,image=image6)
    imagelabel.place(x=250,y=320, anchor=CENTER)

    title1 = Label(root,text="pH     CH  COONa",fg="magenta4",font=("arial",20,"bold"))
    title1.place(x=250,y=30,anchor=CENTER)
    title2 = Label(root,text="for",fg="magenta4",font=("arial",15,"bold"))
    title2.place(x=193,y=30,anchor=CENTER)
    title3 = Label(root, text="3", fg="magenta4", font=("arial", 13, "bold"))
    title3.place(x=260, y=33, anchor=CENTER)
    title4 = Label(root,text="aqueous solution",fg="RoyalBlue1",font=("arial",15,"bold"))
    title4.place(x=250,y=65,anchor=CENTER)

    molarlabel = Label(root,text="Molarity of CH3COONa(aq)  (M)",fg="blue",font=("helvetica",11))
    molarlabel.place(x=50,y=120,anchor=W)
    data1 = StringVar()
    molar = Entry(root,textvariable=data1)
    molar.place(x=270,y=120,anchor=W)

    calculate = Button(root,text="Calculate",fg="orange",font=("arial",13),command=lambda: cal(root))
    calculate.place(x=250,y=160,anchor=CENTER)

    def cal(root):
        eraser = Label(root,width=100,height=3)
        eraser.place(x=250,y=210,anchor=CENTER)

        try:
            mola = eval(data1.get())
            ka = 1.8*10**(-5)
            kb = (1*10**(-14)/ka)

            x = (-kb+math.sqrt(kb**2+4*mola*kb))/2
            ph = 14 + math.log10(x)
            ph = round(ph,4)
            ans = Label(root,text="pH = "+str(ph),fg="purple",font=("arial",13))
            ans.place(x=250,y=210,anchor=CENTER)
        except:
            ans = Label(root,text="Wrong Input",fg="purple",font=("arial",13))
            ans.place(x=250,y=210,anchor=CENTER)
            tkinter.messagebox.showinfo("Warning", "Please enter valid input.")

    statusbar = Label(root,text="Ka for CH3COOH = 1.8×10^-5.",bd=1,relief=SUNKEN,anchor=W,width=500)
    statusbar.place(y=380)


#*************Strong_acid-base**************
def strong(root):
    eraser = Label(root,width=500,height=350)
    eraser.place(x=250,y=200,anchor=CENTER)

    title1 = Label(root,text="Strong Acid - Strong base",fg="midnight blue",font=("arial",20,"bold"))
    title1.place(x=250,y=30,anchor=CENTER)
    title2 = Label(root,text="Titration",fg="firebrick",font=("arial",17,"bold"))
    title2.place(x=250,y=65,anchor=CENTER)

    data1 = StringVar()
    e1 = Entry(root,width=7,textvariable=data1)
    e1.place(x=65,y=140,anchor=W)
    l1 = Label(root,text="mL  of",fg="blue",font=("helvetica",11))
    l1.place(x=125,y=140,anchor=W)
    data2 = StringVar()
    e2 = Entry(root,width=7,textvariable=data2)
    e2.place(x=180,y=140,anchor=W)
    l2 = Label(root,text="M  HCl were collected,",fg="blue",font=("helvetica",11))
    l2.place(x=250,y=140,anchor=W)
    l3 = Label(root,text="and diluted to",fg="blue",font=("helvetica",11))
    l3.place(x=65,y=180,anchor=W)
    data3 = StringVar()
    e3 = Entry(root,width=10,textvariable=data3)
    e3.place(x=165,y=180,anchor=W)
    l4 = Label(root,text="mL  with distill water.",fg="blue",font=("helvetica",11))
    l4.place(x=250,y=180,anchor=W)
    l5 = Label(root,text="The buret was filled with",fg="blue",font=("helvetica",11))
    l5.place(x=65,y=220,anchor=W)
    data4 = StringVar()
    e4 = Entry(root,width=10,textvariable=data4)
    e4.place(x=230,y=220,anchor=W)
    l6 = Label(root,text="M  NaOH,",fg="blue",font=("helvetica",11))
    l6.place(x=310,y=220,anchor=W)
    l7 = Label(root,text="and added",fg="blue",font=("helvetica",11))
    l7.place(x=65,y=260,anchor=W)
    data5 = StringVar()
    e5 = Entry(root,width=12,textvariable=data5)
    e5.place(x=150,y=260,anchor=W)
    l8 = Label(root,text="mL  into the acid.",fg="blue",font=("helvetica",11))
    l8.place(x=250,y=260,anchor=W)

    calculate = Button(root,text="Calculate",fg="orange",font=("arial",13),command=lambda: cal(root))
    calculate.place(x=250,y=300,anchor=CENTER)

    def cal(root):
        eraser = Label(root,width=100,height=3)
        eraser.place(x=250,y=350,anchor=CENTER)

        try:
            vc = eval(data1.get())
            cc = eval(data2.get())
            vd = eval(data3.get())
            cnaoh = eval(data4.get())
            vnaoh = eval(data5.get())


            if vc*cc > vnaoh*cnaoh:
                x = (vc*cc-vnaoh*cnaoh)/(vd+vnaoh)
                ph = -math.log10(x)
            elif vc*cc < vnaoh*cnaoh:
                x = (vnaoh*cnaoh-vc*cc)/(vd+vnaoh)
                ph = 14+math.log10(x)
            else:
                x = 1*10**(-7)
                ph = -math.log10(x)

            ph = round(ph,4)
            ans = Label(root,text="pH = "+ str(ph),fg="purple",font=("arial",13))
            ans.place(x=250,y=350,anchor=CENTER)
        except:
            ans = Label(root,text="Wrong Input",fg="purple",font=("arial",13))
            ans.place(x=250,y=350,anchor=CENTER)
            tkinter.messagebox.showinfo("Warning", "Please enter valid input.")

    statusbar = Label(root,text="Strong acid and strong base refer to HCl and NaOH respectively.",bd=1,relief=SUNKEN,anchor=W,width=500)
    statusbar.place(y=380)


#*************Weak_acid-Strong_base************
def weak(root):
    eraser = Label(root,width=500,height=350)
    eraser.place(x=250,y=200,anchor=CENTER)

    title1 = Label(root,text="Weak Acid - Strong Base",fg="DarkOrchid1",font=("arial",20,"bold"))
    title1.place(x=250,y=30,anchor=CENTER)
    title2 = Label(root,text="Titration",fg="VioletRed2",font=("arial",17,"bold"))
    title2.place(x=250,y=60,anchor=CENTER)

    kalabel1 = Label(root,text="Ka for weak acid: ",fg="blue",font=("helvetica",11))
    kalabel1.place(x=50,y=110,anchor=W)
    data6 = StringVar()
    ka = Entry(root,width=15,textvariable=data6)
    ka.place(x=175,y=110,anchor=W)
    kalabel2 = Label(root,text="(* for multiply, ** for power)",fg="green",font=("helvetica",10))
    kalabel2.place(x=300,y=110,anchor=W)

    data1 = StringVar()
    e1 = Entry(root, width=7, textvariable=data1)
    e1.place(x=65, y=150, anchor=W)
    l1 = Label(root, text="mL  of", fg="blue", font=("helvetica", 11))
    l1.place(x=125, y=150, anchor=W)
    data2 = StringVar()
    e2 = Entry(root, width=7, textvariable=data2)
    e2.place(x=180, y=150, anchor=W)
    l2 = Label(root, text="M  HCl were collected,", fg="blue", font=("helvetica", 11))
    l2.place(x=250, y=150, anchor=W)
    l3 = Label(root, text="and diluted to", fg="blue", font=("helvetica", 11))
    l3.place(x=65, y=185, anchor=W)
    data3 = StringVar()
    e3 = Entry(root, width=10, textvariable=data3)
    e3.place(x=165, y=185, anchor=W)
    l4 = Label(root, text="mL  with distill water.", fg="blue", font=("helvetica", 11))
    l4.place(x=250, y=185, anchor=W)
    l5 = Label(root, text="The buret was filled with", fg="blue", font=("helvetica", 11))
    l5.place(x=65, y=220, anchor=W)
    data4 = StringVar()
    e4 = Entry(root, width=10, textvariable=data4)
    e4.place(x=230, y=220, anchor=W)
    l6 = Label(root, text="M  NaOH,", fg="blue", font=("helvetica", 11))
    l6.place(x=310, y=220, anchor=W)
    l7 = Label(root, text="and added", fg="blue", font=("helvetica", 11))
    l7.place(x=65, y=255, anchor=W)
    data5 = StringVar()
    e5 = Entry(root, width=12, textvariable=data5)
    e5.place(x=150, y=255, anchor=W)
    l8 = Label(root, text="mL  into the acid.", fg="blue", font=("helvetica", 11))
    l8.place(x=250, y=255, anchor=W)

    calculate = Button(root,text="Calculate",fg="orange",font=("arial",13),command=lambda: cal(root))
    calculate.place(x=250,y=300,anchor=CENTER)

    def cal(root):
        eraser = Label(root,width=100,height=3)
        eraser.place(x=250,y=350,anchor=CENTER)

        try:
            vc = eval(data1.get())
            cc = eval(data2.get())
            vd = eval(data3.get())
            cnaoh = eval(data4.get())
            vnaoh = eval(data5.get())
            ka = eval(data6.get())
            kb = (1*10**(-14))/ka

            ca = vnaoh * cnaoh / (vd + vnaoh)
            cha = (vc * cc - vnaoh * cnaoh) / (vd + vnaoh)

            if vnaoh*cnaoh == 0:
                x = (-ka+math.sqrt(ka**2+4*ka*cha))/2
                ph = -math.log10(x)
            elif vc*cc > vnaoh*cnaoh:
                ph = -math.log10(ka) + math.log10(ca/cha)
            elif vc*cc == vnaoh*cnaoh:
                x = (-kb+math.sqrt(kb**2+4*ca*kb))/2
                ph = 14 + math.log10(x)
            else:
                coh = (vnaoh*cnaoh-vc*cc)/(vd+vnaoh)
                ph = 14 + math.log10(coh)

            ph = round(ph, 4)
            ans = Label(root,text="pH = "+str(ph),fg="purple",font=("arial",13))
            ans.place(x=250,y=350,anchor=CENTER)
        except:
            ans = Label(root,text="Wrong Input",fg="purple",font=("arial",13))
            ans.place(x=250,y=350,anchor=CENTER)
            tkinter.messagebox.showinfo("Warning", "Please enter valid input.")

    statusbar = Label(root,text="Ka for CH3COOH is 1.8 × 10^(-5). Strong base refers to NaOH.",bd=1,relief=SUNKEN,anchor=W,width=500)
    statusbar.place(y=380)




root.mainloop()