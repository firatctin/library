import sqlite3
from tk import *
from tkcalendar import DateEntry

from tkinter import *
from tkinter import messagebox
#Veri tabanı işlemlerini yaptığımız kısımlar
con = sqlite3.connect("kitaplık.db")#database bağlantısı
cursor = con.cursor()#imleç oluşturuyoruz

cursor.execute("CREATE TABLE IF NOT EXISTS kitaplar(id INTEGER PRIMARY KEY,isim TEXT, yazarismi TEXT, basımtarihi DATE, sayfasayısı TEXT, durumu BOOLEAN)")#SQL sorgusu
con.commit()#İşlemleri dbye işleme
con.close()

#üyeler tablosunu oluşturuyoruz:
con = sqlite3.connect("kitaplık.db")#database bağlantısı
cursor = con.cursor()#imleç oluşturuyoruz

cursor.execute("CREATE TABLE IF NOT EXISTS üyeler(üyeid INTEGER PRIMARY KEY AUTOINCREMENT, isimsoyisim TEXT, uyeliktarihi DATE)")#SQL sorgusu
con.commit()#İşlemleri dbye işleme
con.close()

#Ödünç verilmiş kitaplar tablosu:
con = sqlite3.connect("kitaplık.db")#database bağlantısı
cursor = con.cursor()#imleç oluşturuyoruz

cursor.execute("CREATE TABLE IF NOT EXISTS oduncverilmis(kitapid INT, kitapisim TEXT, oduncalan TEXT,oduncalanid INT, alınmatarihi DATE)")#SQL sorgusu
con.commit()#İşlemleri dbye işleme
con.close()

#TKINTER OBJESİ
master = Tk()


#Kitap ekleme butonu için tanımladığımız yeni bir pencere açıp aldığı bilgilerle kitabı ekleyecek fonksiyon
def kitapekle():
    #yeni pencere açmak için gerekli olan tkinter işlemleri
    newWindow = Toplevel(master)
    newWindow.title("Kitap Kaydet")
    newWindow.geometry("1000x600")
    frame1 = Frame(newWindow, bg = '#65A8E1')
    frame1.place(relx = 0.1, rely = 0.1 , relheight=0.8, relwidth=0.8)
    sayfabaslik =  Label(frame1, bg = '#65A8E1',text ="Kitap Ekle", font= "15" )
    sayfabaslik.pack(padx=10, pady = 10, anchor = N)
    #Kitabın ismini alacağımız kısım:
    title1 =  Label(frame1, bg = '#65A8E1',text ="Kitabın İsmi:", font= "12" )
    title1.pack(padx=10, pady = 1, anchor = NW)
    ma = Text (frame1, height= 1, width = 50)
    ma.pack(anchor= NW, padx = 10, pady = 1)
    #Yazarın ismini alacağımız kısım:
    title2 =  Label(frame1, bg = '#65A8E1',text ="Yazarın İsmi:", font= "12" )
    title2.pack(padx=10, pady = 1, anchor = NW)
    ma1 = Text (frame1, height= 1, width = 50)
    ma1.pack(anchor= NW, padx = 10, pady = 1)
    #Basım tarihini alacağımız kısım:
    title3 =  Label(frame1, bg = '#65A8E1',text ="Basım Tarihi:", font= "12" )
    title3.pack(padx=10, pady = 1, anchor = NW)
    tarihsecici = DateEntry(frame1, width=20, height = 20, bg = '#65A8E1',borderwidth = 20 , locale = "tr_TR")
    tarihsecici._top_cal.overrideredirect(False)
    tarihsecici.pack(padx = 10, pady= 1, anchor= NW)
    #Sayfa sayısını alacağımız kısım:
    title4 =  Label(frame1, bg = '#65A8E1',text ="Sayfa Sayısı:", font= "12" )
    title4.pack(padx=10, pady = 1, anchor = NW)
    ma2 = Text (frame1, height= 1, width = 50)
    ma2.pack(anchor= NW, padx = 10, pady = 1)

    

    
    
    #yeni açılan pencerede buna yarayacak butona tanımlayacağımız fonksiyonu oluşturuyoruz:

    def veriekle():
        #Verileri alıyoruz:
        ismi = ma.get("1.0",END)
        yazar = ma1.get("1.0",END)
        tarih = tarihsecici.get_date()
        sayfa = ma2.get("1.0",END)
        durumu = True
        #verileri veri tabanına ekliyoruz
        con = sqlite3.connect("kitaplık.db")
        cursor = con.cursor()
        cursor.execute("INSERT INTO kitaplar(isim,yazarismi,basımtarihi,sayfasayısı,durumu) VALUES(?,?,?,?,?)",(ismi,yazar,tarih,sayfa, durumu))
        con.commit()
        cursor.close()
        messagebox.showinfo("İşlem Tamamlandı","Kitap başarıyla kaydedildi")
    #butonu oluşturuyoruz

    verieklemebuton = Button(frame1,text="Kitabı Ekle",command = veriekle)
    verieklemebuton.pack(side= BOTTOM, padx=10, pady=10)
    #üye ekleme butonuna vereceğimiz fonksiyon:
def üyeekle():
    #Butona basılınca açılacak pencereyi oluşturuyoruz:
    newWindow = Toplevel(master)
    newWindow.title("Kitap Kaydet")
    newWindow.geometry("1000x600") 
    frame1 = Frame(newWindow, bg = '#65A8E1')
    frame1.place(relx = 0.1, rely = 0.1 , relheight=0.8, relwidth=0.8)
    sayfabaslik =  Label(frame1, bg = '#65A8E1',text ="Üye Ekle", font= "15" )
    sayfabaslik.pack(padx=10, pady = 10, anchor = N)
    #Üyenin ismini-soyismini alacağımız kısım:
    title1 =  Label(frame1, bg = '#65A8E1',text ="Üyenin İsmi-Soyismi:", font= "12" )
    title1.pack(padx=10, pady = 1, anchor = NW)
    ma = Text (frame1, height= 1, width = 50)
    ma.pack(anchor= NW, padx = 10, pady = 1)
        
    #Üyelik tarihini alacağımız kısım:
    
    title3 =  Label(frame1, bg = '#65A8E1',text ="Üyelik Tarihi:", font= "12" )
    title3.pack(padx=10, pady = 1, anchor = NW)
    tarihsecici = DateEntry(frame1, width=20, height = 20, bg = '#65A8E1',borderwidth = 20 , locale = "tr_TR")
    tarihsecici._top_cal.overrideredirect(False)
    tarihsecici.pack(padx = 10, pady= 1, anchor= NW)

    #üye ekleme fonksiyonunu atacağımız buton için fonksiyon:

    def üyeekleme():
        isim = ma.get("1.0",END)
        tarih = tarihsecici.get_date()

        con = sqlite3.connect("kitaplık.db")

        cursor = con.cursor()

        cursor.execute("INSERT INTO üyeler(isimsoyisim,uyeliktarihi) VALUES(?,?)",(isim,tarih))
        con.commit()
            
        con.close()
        messagebox.showinfo("İşlem Tamamlandı","Üye başarıyla kaydedildi")
    #Sayfanın sonunda gözükecek olan üye ekleme buttonu
    üyeeklemebutonu = Button(frame1,text = "Üye Ekle",command = üyeekleme)
    üyeeklemebutonu.pack(side= BOTTOM, padx=10, pady=10)

#Ödünç alma fonksiyonunu tasarlıyoruz:
def oduncver():
    #Butona basılınca açılacak pencereyi oluşturuyoruz:
    newWindow = Toplevel(master)
    newWindow.title("Ödünç Ver")
    newWindow.geometry("1000x600") 
    frame1 = Frame(newWindow, bg = '#65A8E1')
    frame1.place(relx = 0.1, rely = 0.1 , relheight=0.8, relwidth=0.8)
    sayfabaslik =  Label(frame1, bg = '#65A8E1',text ="Ödünç Ver", font= "15" )
    sayfabaslik.pack(padx=10, pady = 10, anchor = N)

    #kitapların seçim listesini oluşturuyoruz:
    opisyonkitap = StringVar(frame1)
    opisyonkitap.set("Kitabı Seçiniz")#Varsayılan değer...

    #kitap isimlerini alıyoruz:
    
    con = sqlite3.connect("kitaplık.db")
    cursor = con.cursor()
    cursor.execute("SELECT id,isim,durumu FROM kitaplar")

    kitapisimleri = cursor.fetchall()
    seçenekler = []
    for i in kitapisimleri:
            
        if i[2] == 1:
            z = i[1].rstrip()
            a = str(i[0]) +"," +i[1]
            seçenekler.append(a)
            

    con.close()
    Label(frame1,text= "Ödünç Verilecek Kitabı Seçiniz:", bg= "#65A8E1").pack(padx=3,pady=10, anchor=NW)
    #Kullanıcının kitap isimlerini seçmesi için bir açılır menü yazıyoruz
    question_menu = OptionMenu(frame1,opisyonkitap , *seçenekler)
    question_menu.pack(padx=3,pady=10, anchor=NW)

    

    #Hangi üyenin kitabı aldığını seçmek için üye isimlerini alıyoruz:
    con = sqlite3.connect("kitaplık.db")
    cursor = con.cursor()
    cursor.execute("SELECT isimsoyisim,üyeid FROM üyeler")

    üyeisimleri = cursor.fetchall()
    üyeler = []
    #Kitabın "üyeismi,ID" şeklinde görülmesi için bir for döngüsü
    for i in üyeisimleri:
        a = str(i[1]) + ","+ i[0].rstrip()
        üyeler.append(a)

    con.close()
    Label(frame1,text= "Ödünç Verilecek Üyeyi Seçiniz:", bg= "#65A8E1").pack(padx=3,pady=10,anchor=NW)
    opisyonüye = StringVar(frame1)
    opisyonüye.set("Üyeyi Seçiniz")
    #üye açılır menüsü
    question_menu2 = OptionMenu(frame1, opisyonüye , *üyeler)
    question_menu2.pack(padx=3,pady=10,anchor=NW)

    

    #verilme tarihi seçici
    Label(frame1,text= "Ödünç alındığı tarih:", bg= "#65A8E1").pack(padx=3,pady=10, anchor=NW)
    tarihsecici = DateEntry(frame1, width=20, height = 20, bg = '#65A8E1',borderwidth = 20 , locale = "tr_TR")
    tarihsecici._top_cal.overrideredirect(False)
    tarihsecici.pack(padx = 10, pady= 1, anchor=NW)
    
    #Bottonumuza ekleyeceğimiz tetikleyici fonksiyon:  
    def kitabıoduncal():
        
        #üye açılır menüsünden veriyi alıyoruz:
        verilenüye = opisyonüye.get()
        tarih = tarihsecici.get()#tarihi alıyoruz
        verilenüyeliste = verilenüye.split(",")
        #Seçilen kitabın isim bilgisini değişkene atıyoruz:

        verilenkitap = opisyonkitap.get()
        verilenkitapliste = verilenkitap.split(",")

        #ödünç alınan kitap veri tabanına kaydetmek için kitap bilgilerini alıyoruz:
        con = sqlite3.connect("kitaplık.db")
        cursor = con.cursor()
        sorgu = "SELECT id,isim FROM kitaplar WHERE id = {}".format(verilenkitapliste[0])
        cursor.execute(sorgu)
        kitapbilgileri1 = cursor.fetchone()
        kitabınidsi = kitapbilgileri1[0]
        kitabınismi = kitapbilgileri1[1].rstrip()

        con.close()
        
        #ödünç alan üyeyi oduncalınan tablosuna kaydetmek için üye bilgilerini alıyoruz
        con = sqlite3.connect("kitaplık.db")
        cursor = con.cursor()
        sorgu2 = "SELECT üyeid, isimsoyisim FROM üyeler WHERE üyeid = {}".format(verilenüyeliste[0])
        cursor.execute(sorgu2)
        üyebilgileri1 = cursor.fetchone()
        üyeninidsi = üyebilgileri1[0]
        üyeninismi = üyebilgileri1[1].rstrip()
        con.close()

        #bu bilgileri oduncalınan tablosuna ekliyoruz  
        
        con = sqlite3.connect("kitaplık.db")
        cursor = con.cursor()
        cursor.execute("INSERT INTO oduncverilmis(kitapid, oduncalan, kitapisim, oduncalanid, alınmatarihi) VALUES(?,?,?,?,?)",(kitabınidsi, üyeninismi, kitabınismi, üyeninidsi, tarih))
        con.commit()
        con.close()

        #kitaplar tablosundaki kitabın durumunu 'kütüphanede' den 'ödünç alınmış' durumuna getiriyoruz:
        con = sqlite3.connect("kitaplık.db")
        cursor = con.cursor()
        sorgu3 = "UPDATE kitaplar SET durumu = {} WHERE id = {}".format(0, verilenkitapliste[0])
        cursor.execute(sorgu3)
        con.commit()
        con.close()
        messagebox.showinfo("Başarılı İşlem","Kitap başarıyla ödünç verilmiş olarak işaretlendi!")

    #odünç verme işlemini tetikleyici button:
    oduncverbutton = Button(frame1,text = "Onayla", command = kitabıoduncal)
    oduncverbutton.pack( padx=10, pady= 10,anchor= S)


#Teslim al buttonu için fonksiyon:
def teslimal():
    newWindow = Toplevel(master)
    newWindow.title("Teslim Al")
    newWindow.geometry("1000x600") 
    frame1 = Frame(newWindow, bg = '#65A8E1')
    frame1.place(relx = 0.1, rely = 0.1 , relheight=0.8, relwidth=0.8)
    sayfabaslik =  Label(frame1, bg = '#65A8E1',text ="Teslim Alma", font= "15" )
    sayfabaslik.pack(padx=10, pady = 10, anchor = N)
    Label(frame1,text= "Teslim Alınan Kitabın ID'si:", bg= "#65A8E1").pack(padx=3,pady=10,anchor=NW)
    ma = Text (frame1, height= 1, width = 50)
    ma.pack(anchor= NW, padx = 10, pady = 1)
    def tamamlateslim():
        kitapid = ma.get("1.0",END)
        con = sqlite3.connect("kitaplık.db")
        cursor = con.cursor()
        cursor.execute("DELETE FROM oduncverilmis WHERE kitapid = %s" % kitapid )
        con.commit()
        cursor.execute("UPDATE kitaplar SET durumu = 1 WHERE id = %s" % kitapid )
        con.commit()
        con.close()
        messagebox.showinfo("Başarılı İşlem","Kitap başarıyla teslim edildi!")
    teslimalbutton = Button(frame1,text = "Onayla", command = tamamlateslim)
    teslimalbutton.pack(anchor= S, padx=10, pady= 10)





canvas = Canvas(master, height=600 , width= 1000)
canvas.pack()

framekontrol = Frame(master,bg= '#65A8E1')
framekontrol.place(relx = 0.05,rely = 0.05,relwidth = 0.20, relheight=0.90 )

başlık1 = Label(framekontrol,bg='#65A8E1', text = "Kontrol Paneli", font= "12")
başlık1.pack(anchor = N, padx= 10, pady= 10)

#ana ekran kitap ekleme buttonu
button1 = Button(framekontrol, text = "Kitap Ekle", command= kitapekle)
button1.pack(anchor = N,padx=10,pady=10)


#ana ekran üye ekleme buttonu
button2 = Button(framekontrol, text = "Üye Ekle", command= üyeekle)
button2.pack(anchor = N,padx=10,pady=10)

#ana ekran ödünç verme buttonu
button3 = Button(framekontrol, text = "Ödünç Ver", command= oduncver)
button3.pack(anchor = N,padx=10,pady=10)

#ana ekran teslim alma buttonu
button4 = Button(framekontrol, text = "Teslim Al", command= teslimal)
button4.pack(anchor = N,padx=10,pady=10)

#Arama ve genel işlemlerin yapılacağı frame
framegenel = Frame(master,bg= '#65A8E1')
framegenel.place(relx = 0.26,rely = 0.05,relwidth = 0.65, relheight=0.90 )

#Arama işlemleri
başlık1 = Label(framegenel,bg='#65A8E1', text = "Kitap Ara", font= "12")
başlık1.pack(anchor = NW, padx= 10, pady= 10)


başlık3 = Label(framegenel,bg='#65A8E1', text = "Kitabın İsmi:", font= "10")
başlık3.pack(anchor = NW, padx= 10, pady= 10)

maisim = Text (framegenel, height= 1, width = 50)
maisim.pack(anchor= NW, padx = 10, pady = 1)

başlık3 = Label(framegenel,bg='#65A8E1', text = "Kitabın Yazarı:", font= "10")
başlık3.pack(anchor = NW, padx= 10, pady= 10)

mayazar = Text (framegenel, height= 1, width = 50)
mayazar.pack(anchor= NW, padx = 10, pady = 1)


def kitapara():
    
    
    
    
    
    isim = maisim.get("1.0",END)
    
    isim = isim.rstrip()
    
    yazar = mayazar.get("1.0",END)

    yazar = yazar.rstrip()
    
    
    
    con = sqlite3.connect("kitaplık.db")
    cursor = con.cursor()
    sorgu = '''SELECT * FROM kitaplar WHERE isim LIKE "%{}%" or yazarismi LIKE "%{}%"'''.format(isim,yazar)
    
    cursor.execute(sorgu)
    sonuçlar = cursor.fetchall()
    con.close()
    
    
    newWindow = Toplevel(master)
    newWindow.title("Kitap Bilgisi")
    newWindow.geometry("1500x600") 
    
    
    
    
    class Table:
     
        def __init__(self,root):
            
            # code for creating table
            for i in range(total_rows):
                for j in range(total_columns):
                    
                    self.e = Entry(newWindow, width=20, fg='blue',
                                font=('Arial',16,'bold'))
                    
                    self.e.grid(row=i, column=j)
                    self.e.insert(END, sonuçlar[i][j])
    total_rows = len(sonuçlar)
    total_columns = len(sonuçlar[0])
    t = Table(newWindow)
button5 = Button(framegenel, text = "Ara", command= kitapara)
button5.pack(anchor = NW,padx=10,pady=10)


Label(framegenel,bg='#65A8E1', text = "Fırat Çetin tarafından tasarlandı ve programlandı", font= "10").pack(anchor = S,side=BOTTOM ,padx= 10, pady= 10)


    
        


mainloop()