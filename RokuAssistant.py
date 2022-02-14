from tkinter import *
from tkinter import messagebox
from threading import Thread
import time
import os
from speak import *
import sys
import subprocess
isik="acik"
def rokuArayuz():
    def sistemDurumu():
        if isik=="acik":
            etiket1["text"]="Asistan Dinlemede"
            etiket1["fg"]="#6a9d51"
        elif isik=="kapali":
            etiket1["text"]="Lütfen Bekleyin.."
            etiket1["fg"]="#666666"
    def hakkimizda():
        messagebox.showinfo("Roku Asistan V1.0 Hakkımızda","Program Üreticisi: Cihat Cebeci\nİletişim: cebecicihat@hotmail.com\nBu program Python ile kodlanmıştır.\n2019 Kasım ROKU ASSISTANT V.1.0")
    def girisRehber():
        messagebox.showinfo("Roku Asistan V1.0 Giriş Rehberi","1)Roku Assistant sesli komutlar ile size hizmet eden bir asistandır.\n2)'Ben Roku, hizmetinizdeyim' cümlesini duyduktan sonra 'ROKU' diyerek beep sesini bekleyin. Sesten sonra komut verebilirsiniz.\n3)Komut verdikten sonra mikrofonun sesini kesmeniz tepki süresini hızlandıracak, yoksa sistem mikrofonu dinlemeye devam edecektir. BKZ:Mikrofon Kullanımı")
    def mikrofonKullanimi():
        messagebox.showinfo("Roku Asistan V1.0 Mikrofon Kullanımı","1)Bu programı kullanmak için önerilen android yazılımı VO Mic'tir.Hem telefona hem de bilgisayarınıza VO Mic'i yükleyerek WiFi üzerinden cihazları birbirine bağlayın.\n2)Wo Mic Android ekranı oldukça basittir, 'Mute' tuşu işaretli iken mikrofon dinlenmeyecek tiki kaldırdığınızda dinlenecektir.\n3)Bir şey söyledikten sonra 'mute' tuşunu tiklemeniz sistem tepki süresini hızlandıracaktır, mutlaka kullanın.Kullanmamanız durumda hem programın tepki vermesi çok uzun sürecek, hemde asistan kendi sesini duyarak döngüye girecektir.")
    def calKomutu():
        messagebox.showinfo("Roku Asistan V1.0 Çal Modülü Kullanımı","1)Sisteme eğer ki giriş yaptıysanız(BKZ:Giriş Rehberi) istediğiniz şarkıyı veya diziyi oynatmak için 'istediğiniz şarkı çal' diyin. Örnekleyecek olursak, 'CEZA SUSPUS ÇAL' derseniz sistem Ceza'nın suspus şarkısını çalacaktır.\n2)Şarkı çalmaya başladıktan sonra 'KAPAT' derseniz sistem şarkıyı kapatacaktır.\n3)Ayrıca sesi arttırıp azatmanız mümkündür. 'SESİ AZALT' ve benzeri şeyler söylerseniz ses azalacak, 'SESİ ARTTIR' ve benzeri şeyler söylerseniz ses artacak, 'SESİ FULLE' ve benzeri şeyler söylerseniz ses %100 düzeyinde olacak, 'SESİ SIFIRLA' ve benzeri şeyler söylerseniz ses %0 düzeyinde olacaktır. Sesin artıp azaldığını duyacağınız beep sesinden anlayabilirsiniz.")
    def arastirmaKomutu():
        messagebox.showinfo("Roku Asistan V1.0 Araştırma Modülü Kullanımı","1)Sisteme eğer ki giriş yaptıysanız(BKZ:Giriş Rehberi) istediğiniz bilgiyi arayabilirsiniz. Arama yapmak için 'arama terimi bilgi' diyin. Örnekleyecek olursak, 'GÜNEŞ SİSTEMİ BİLGİ' derseniz Wikipedia'da güneş sistemi araştırılacak ve asistan sizin için araştırma sonucunu okuyacaktır.\n2)Bilgi komutunu bir kez verdikten sonra dönüş yoktur, asistan araştırma sonucunu okumayı bitirinceye kadar komut vermeniz mümkün değildir.")
    def dovizKomutu():
        messagebox.showinfo("Roku Asistan V1.0 Döviz Modülü Kullanımı","1)Sisteme eğer ki giriş yaptıysanız(BKZ:Giriş Rehberi) istediğiniz dövizin veya kripto paranın güncel durumu öğrenebilirsiniz.\n2)'aradığınız terim kripto' diyerek kripto paraların güncel durumunu öğrenebilirsiniz, örnekleyecek olursak 'BİTCOİN KRİPTO' derseniz sistem bitcoin'in güncel fiyatını söyleyecektir.\n3)'aradığınız terim döviz' diyerek aradığınız dövizin güncel durumunu öğrenebilirsiniz. Örnekleyecek olursak 'DOLAR DÖVİZ' derseniz sistem doların güncel fiyatını size söylecektir.")
    def beklemeKomutu():
        messagebox.showinfo("Roku Asistan V1.0 Bekleme Modu Kullanımı","1)Sisteme eğer ki giriş yaptıysanız(BKZ:Giriş Rehberi) ve programın bir sonraki girişe kadar bekleme moduna girmesini istiyorsanız, 'BEKLE' ve benzeri komutları söylerek Roku'nun bekleme moduna girmesini sağlayabilirsiniz. LOGOUT SESİNİ DUYDUĞUNUZDA SİSTEM BEKLEME MODUNA GEÇMİŞ DEMEKTİR. Bu komuttan sonra tekrar komut verebilmek için tekrar giriş yapmanız gerekir. Yani 'ROKU' diyerek sistemi tekrar devreye sokmalısınız.")
    def saatTarih():
        messagebox.showinfo("Roku Asistan V1.0 Saat ve Tarih Modülü","1)Roku'ya soracağınız 'Saat kaç','Hangi aydayız','Hangi yıldayız' gibi sorulara Roku cevap verebilir.\n2)Roku'ya 'şehir hava' derseniz söylediğiniz şehrin hava durumunu size söyleyecektir. Örnekleyecek olursak 'İZMİR HAVA' derseniz sistem size İzmir'in hava durumunu söyleyecektir.")
    def notAlmaSistemi():
        messagebox.showinfo("Roku Asistan V1.0 Not Modülü Kullanımı","1)Roku sizin için not tutabilir, notlarınızı okuyabilir ve notlarınızı silebilir.\n2)'Söyleceğiniz sözler not' derseniz Roku sizin için bu sözleri not olarak kaydedecektir. Örnekleyecek olursak, 'YARIN İKİDE YOLA ÇIKACAĞIM NOT' derseniz 'yarın ikide yola çıkacağım' sözlerini not olarak kaydedecektir.\n3)Notlarınızı okumak için 'NOTLARIMI OKU' diyebilirsiniz, önceden kaydettiğiniz tüm notlar Roku tarafından okunacaktır.\n3)Notlarınızı silmek için 'NOTLARIMI SİL' diyebilirsiniz, bu komutla tüm notlarınız silinecektir.")
    def digerModuller():
        messagebox.showinfo("Roku Asistan V1.0 Diğer Modüller","1)Ayrıca Roku ile sohbet edebilirsiniz. Roku 1000'den fazla kelimeyi bilmektedir ve sizinle 50'den fazla diyalog kurabilir.\n2)Rokunun neleri bildiğini tam olarak öğrenmek için onunla konuşmanız gerekmektedir. Roku bilmediği bir durum olduğunda 'Üzgünüm söylediğin şeyi anlamadım' diyecektir. Bunun dışında size cevap vermeye çalışacaktır. Deneyin ve görün.. 'Nasılsın diyerek başlayabilirsiniz.\n3)Diğer tüm sorularınızı cebecicihat@hotmail.com'a mail atarak öğrenebilirsiniz.")
    def konsolGoruntule():
        dosyakonsol = open("cikti.txt","r")
        dosyagoruntu = dosyakonsol.read()
        messagebox.showwarning("Konsol Kayıtları",dosyagoruntu)
    def konsolTemizle():
        dosyakonsol = open("cikti.txt","w")
        dosyakonsol.write("--Konsol Kayıtları--\n")
        messagebox.showwarning("Konsol Kayıtları","Konsol Kayıtları Başarıyla Temizlendi.")
    pencere = Tk()
    pencere.title("Roku Asistan V1.0")
    uygulama = Frame(pencere)
    uygulama.grid()
    src_img = PhotoImage(file ='icon.png')
    image = Label(uygulama, width=250,height=76,image = src_img)
    image.grid(padx=1, pady=1)
    etiket1 = Label(uygulama,text="Asistan Dinlemede",fg="#6a9d51")
    etiket1.grid(padx=2, pady=2)
    ##BUTON##
    girisButon = Button(uygulama, text = "Giriş Rehberi" , width=20,height=1,command=girisRehber,bg="#D5DBDB")
    girisButon.grid(padx=15, pady=5)
    mikrofonButon = Button(uygulama, text = "Mikrofon Kullanımı" , width=20,height=1,command=mikrofonKullanimi,bg="#D5DBDB")
    mikrofonButon.grid(padx=15, pady=5)
    calButon = Button(uygulama, text = "Çal Modülü Kullanımı" , width=20,height=1,command=calKomutu,bg="#D5DBDB")
    calButon.grid(padx=15, pady=5)
    arastirmaButon = Button(uygulama, text = "Araştırma Modülü Kullanımı" , width=25,height=1,command=arastirmaKomutu,bg="#D5DBDB")
    arastirmaButon.grid(padx=15, pady=5)
    dovizButon = Button(uygulama, text = "Döviz Modülü Kullanımı" , width=20,height=1,command=dovizKomutu,bg="#D5DBDB")
    dovizButon.grid(padx=15, pady=5)
    beklemeButon = Button(uygulama, text = "Bekleme Modu Kullanımı" , width=20,height=1,command=beklemeKomutu,bg="#D5DBDB")
    beklemeButon.grid(padx=15, pady=5)
    saatTarihButon = Button(uygulama, text = "Saat,Tarih ve Hava Durumu Modülü" , width=30,height=1,command=saatTarih,bg="#D5DBDB")
    saatTarihButon.grid(padx=15, pady=5)
    notModulu = Button(uygulama, text = "Not Modülü Kullanımı" , width=20,height=1,command=notAlmaSistemi,bg="#D5DBDB")
    notModulu.grid(padx=15, pady=5)
    digerButon = Button(uygulama, text = "Diğer Modüller" , width=20,height=1,command=digerModuller,bg="#D5DBDB")
    digerButon.grid(padx=15, pady=5)
    hakkimizdaButon = Button(uygulama, text = "Hakkımızda" , width=20,height=1,command=hakkimizda,bg="#D5DBDB")
    hakkimizdaButon.grid(padx=15, pady=5)
    konsolGoruntule = Button(uygulama, text = "Konsol Görüntüle" , width=20,height=1,command=konsolGoruntule,bg="#EC7063",activebackground="#E74C3C")
    konsolGoruntule.grid(padx=15, pady=5)
    konsolTemizle = Button(uygulama, text = "Konsol Temizle" , width=20,height=1,command=konsolTemizle,bg="#CB4335",activebackground="#A93226",)
    konsolTemizle.grid(padx=15, pady=5)
    pencere.resizable(False, False)
    pencere.iconbitmap('favicon.ico')
    def center_window(w=250, h=545):
        ws = pencere.winfo_screenwidth()
        hs = pencere.winfo_screenheight()
        x = (ws/2) - (w/2)    
        y = (hs/2) - (h/2)
        pencere.geometry('%dx%d+%d+%d' % (w, h, x, y))
    center_window(250, 545) 
    pencere.mainloop()
rokuArayuz_run = Thread(target=rokuArayuz)
rokuArayuz_run.start()
rokusistem()
