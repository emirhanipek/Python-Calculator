from tkinter import *

b=[]

def clear_text():
   del b[:]
   giris.delete(0, END)


def Close():
    pencere.destroy()


eski=""
def alan_guncelle(sayi):
    icerik = giris.get() + sayi
    giris.delete(0, END)
    giris.insert(0, icerik)
    return icerik


def islem_yap(islem):
    icerik = giris.get()

    if len(b) == 0:
        b.append(alan_guncelle(""))
        b.append(islem)
        giris.delete(0, END)
    elif icerik == "" and len(b) == 2 and (islem == "+" or islem == "*" or islem == "-" or islem == "/"):
        b[1]=islem
        giris.delete(0, END)
    elif icerik != "" and len(b) == 2 and (islem == "+" or islem == "*" or islem == "-" or islem == "/"):
        sayi1, sayi2 = float(b[0]),float(icerik)
        if islem == "+":
            sonuc = sayi1 + sayi2
        elif islem == "-":
            sonuc = sayi1 - sayi2
        elif islem == "*":
            sonuc = sayi1 * sayi2
        elif islem == "/":
            sonuc = sayi1 / sayi2
        b[0], b[1] = str(sayi2), islem
        giris.delete(0, END)
        giris.insert(0, sonuc)
        return sonuc
    if islem == "=":
        return sonuc_goster(islem_yap(b[1]))
def sonuc_goster(sayi):
    giris.delete(0, END)
    giris.insert(0, sayi)





pencere = Tk(className="Calculator")

pencere.title("Hesap Makinası")

pencere.geometry("600x320")

giris = Entry(font="Verdana 14 bold",width=16,justify=RIGHT)

giris.place(x=20,y=20,width=560,height=40)





#1 SATIR
buton_cls = Button(pencere,text="CLS",command=clear_text)
buton_cls.place(x=25,y=70,width=130,height=40,)

buton_back = Button(pencere,text="BACK",)
buton_back.place(x=165,y=70,width=130,height=40,)

buton_ = Button(pencere,text="",)
buton_.place(x=305,y=70,width=130,height=40,)

buton_close = Button(pencere,text="CLOSE",command=Close)
buton_close.place(x=445,y=70,width=130,height=40,)

#2 SATIR

buton_7 = Button(pencere,text="7", command= lambda:alan_guncelle(str(7)))
buton_7.place(x=25,y=120,width=130,height=40,)

buton_8 = Button(pencere,text="8",command= lambda:alan_guncelle(str(8)))
buton_8.place(x=165,y=120,width=130,height=40, )

buton_9 = Button(pencere,text="9",command= lambda:alan_guncelle(str(9)))
buton_9.place(x=305,y=120,width=130,height=40,)

buton_bolum = Button(pencere,text="/",command= lambda: islem_yap(str("/")))
buton_bolum.place(x=445,y=120,width=130,height=40,)

#3 SATIR

buton_4 = Button(pencere,text="4",command=lambda:alan_guncelle(str(4)))
buton_4.place(x=25,y=170,width=130,height=40,)

buton_5 = Button(pencere,text="5",command=lambda:alan_guncelle(str(5)))
buton_5.place(x=165,y=170,width=130,height=40,)

buton_6 = Button(pencere,text="6",command=lambda:alan_guncelle(str(6)))
buton_6.place(x=305,y=170,width=130,height=40,)

buton_carpma = Button(pencere,text="*",command= lambda: islem_yap(str("*")))
buton_carpma.place(x=445,y=170,width=130,height=40,)


#4 SATIR

buton_1 = Button(pencere,text="1",command=lambda:alan_guncelle(str(1)))
buton_1.place(x=25,y=220,width=130,height=40,)

buton_2 = Button(pencere,text="2",command=lambda:alan_guncelle(str(2)))
buton_2.place(x=165,y=220,width=130,height=40,)

buton_3 = Button(pencere,text="3",command=lambda:alan_guncelle(str(3)))
buton_3.place(x=305,y=220,width=130,height=40,)

buton_cıkar = Button(pencere,text="-",command= lambda: islem_yap(str("-")))
buton_cıkar.place(x=445,y=220,width=130,height=40,)

#5 SATIR

buton_0 = Button(pencere,text="0",)
buton_0.place(x=25,y=270,width=130,height=40,)

buton_nokta= Button(pencere,text=".",)
buton_nokta.place(x=165,y=270,width=130,height=40,)

buton_esit = Button(pencere,text="=",command= lambda: islem_yap(str("=")))
buton_esit.place(x=305,y=270,width=130,height=40,)

buton_artı = Button(pencere,text="+",command= lambda: islem_yap(str("+")))
buton_artı.place(x=445,y=270,width=130,height=40,)

pencere.mainloop()
