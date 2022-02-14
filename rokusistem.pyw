import speech_recognition as sr
import os
import time
from selenium import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from gtts import gTTS
from bs4 import BeautifulSoup
from string import punctuation
from speak import *
from veri import *
from giris import *
from playsound import playsound
import locale
import urllib.request
from sesayari import *
from threading import Thread
import sys
from tkinter import *
from tkinter import messagebox
import subprocess
### Giriş ###
isik="acik"
def rokuArayuz():
    def hakkimizda():
        messagebox.showinfo("Roku Asistan V2.0 Hakkımızda","Program Üreticisi: Cihat Cebeci\nİletişim: cebecicihat@hotmail.com\nBu program Python ile kodlanmıştır.\n2021 Kasım ROKU ASSISTANT V.2.0")
    def girisRehber():
        messagebox.showinfo("Roku Asistan V2.0 Giriş Rehberi","1)Roku Assistant sesli komutlar ile size hizmet eden bir asistandır.\n2)'Ben Roku, hizmetinizdeyim' cümlesini duyduktan sonra 'ROKU' diyerek beep sesini bekleyin. Sesten sonra komut verebilirsiniz.\n3)Komut verdikten sonra mikrofonun sesini kesmeniz tepki süresini hızlandıracak, yoksa sistem mikrofonu dinlemeye devam edecektir. BKZ:Mikrofon Kullanımı")
    def mikrofonKullanimi():
        messagebox.showinfo("Roku Asistan V2.0 Mikrofon Kullanımı","1)Bu programı kullanmak için önerilen android yazılımı VO Mic'tir.Hem telefona hem de bilgisayarınıza VO Mic'i yükleyerek WiFi üzerinden cihazları birbirine bağlayın.\n2)Wo Mic Android ekranı oldukça basittir, 'Mute' tuşu işaretli iken mikrofon dinlenmeyecek tiki kaldırdığınızda dinlenecektir.\n3)Bir şey söyledikten sonra 'mute' tuşunu tiklemeniz sistem tepki süresini hızlandıracaktır, mutlaka kullanın.Kullanmamanız durumda hem programın tepki vermesi çok uzun sürecek, hemde asistan kendi sesini duyarak döngüye girecektir.")
    def calKomutu():
        messagebox.showinfo("Roku Asistan V2.0 Çal Modülü Kullanımı","1)Sisteme eğer ki giriş yaptıysanız(BKZ:Giriş Rehberi) istediğiniz şarkıyı veya diziyi oynatmak için 'istediğiniz şarkı çal' diyin. Örnekleyecek olursak, 'CEZA SUSPUS ÇAL' derseniz sistem Ceza'nın suspus şarkısını çalacaktır.\n2)Şarkı çalmaya başladıktan sonra 'KAPAT' derseniz sistem şarkıyı kapatacaktır.\n3)Ayrıca sesi arttırıp azatmanız mümkündür. 'SESİ AZALT' ve benzeri şeyler söylerseniz ses azalacak, 'SESİ ARTTIR' ve benzeri şeyler söylerseniz ses artacak, 'SESİ FULLE' ve benzeri şeyler söylerseniz ses %100 düzeyinde olacak, 'SESİ SIFIRLA' ve benzeri şeyler söylerseniz ses %0 düzeyinde olacaktır. Sesin artıp azaldığını duyacağınız beep sesinden anlayabilirsiniz.")
    def arastirmaKomutu():
        messagebox.showinfo("Roku Asistan V2.0 Araştırma Modülü Kullanımı","1)Sisteme eğer ki giriş yaptıysanız(BKZ:Giriş Rehberi) istediğiniz bilgiyi arayabilirsiniz. Arama yapmak için 'arama terimi bilgi' diyin. Örnekleyecek olursak, 'GÜNEŞ SİSTEMİ BİLGİ' derseniz Wikipedia'da güneş sistemi araştırılacak ve asistan sizin için araştırma sonucunu okuyacaktır.\n2)Bilgi komutunu bir kez verdikten sonra dönüş yoktur, asistan araştırma sonucunu okumayı bitirinceye kadar komut vermeniz mümkün değildir.")
    def dovizKomutu():
        messagebox.showinfo("Roku Asistan V2.0 Döviz Modülü Kullanımı","1)Sisteme eğer ki giriş yaptıysanız(BKZ:Giriş Rehberi) istediğiniz dövizin veya kripto paranın güncel durumu öğrenebilirsiniz.\n2)'aradığınız terim kripto' diyerek kripto paraların güncel durumunu öğrenebilirsiniz, örnekleyecek olursak 'BİTCOİN KRİPTO' derseniz sistem bitcoin'in güncel fiyatını söyleyecektir.\n3)'aradığınız terim döviz' diyerek aradığınız dövizin güncel durumunu öğrenebilirsiniz. Örnekleyecek olursak 'DOLAR DÖVİZ' derseniz sistem doların güncel fiyatını size söylecektir.")
    def beklemeKomutu():
        messagebox.showinfo("Roku Asistan V2.0 Bekleme Modu Kullanımı","1)Sisteme eğer ki giriş yaptıysanız(BKZ:Giriş Rehberi) ve programın bir sonraki girişe kadar bekleme moduna girmesini istiyorsanız, 'BEKLE' ve benzeri komutları söylerek Roku'nun bekleme moduna girmesini sağlayabilirsiniz. LOGOUT SESİNİ DUYDUĞUNUZDA SİSTEM BEKLEME MODUNA GEÇMİŞ DEMEKTİR. Bu komuttan sonra tekrar komut verebilmek için tekrar giriş yapmanız gerekir. Yani 'ROKU' diyerek sistemi tekrar devreye sokmalısınız.")
    def saatTarih():
        messagebox.showinfo("Roku Asistan V2.0 Saat ve Tarih Modülü","1)Roku'ya soracağınız 'Saat kaç','Hangi aydayız','Hangi yıldayız' gibi sorulara Roku cevap verebilir.\n2)Roku'ya 'şehir hava' derseniz söylediğiniz şehrin hava durumunu size söyleyecektir. Örnekleyecek olursak 'İZMİR HAVA' derseniz sistem size İzmir'in hava durumunu söyleyecektir.")
    def notAlmaSistemi():
        messagebox.showinfo("Roku Asistan V2.0 Not Modülü Kullanımı","1)Roku sizin için not tutabilir, notlarınızı okuyabilir ve notlarınızı silebilir.\n2)'Söyleceğiniz sözler not' derseniz Roku sizin için bu sözleri not olarak kaydedecektir. Örnekleyecek olursak, 'YARIN İKİDE YOLA ÇIKACAĞIM NOT' derseniz 'yarın ikide yola çıkacağım' sözlerini not olarak kaydedecektir.\n3)Notlarınızı okumak için 'NOTLARIMI OKU' diyebilirsiniz, önceden kaydettiğiniz tüm notlar Roku tarafından okunacaktır.\n3)Notlarınızı silmek için 'NOTLARIMI SİL' diyebilirsiniz, bu komutla tüm notlarınız silinecektir.")
    def digerModuller():
        messagebox.showinfo("Roku Asistan V2.0 Diğer Modüller","1)Ayrıca Roku ile sohbet edebilirsiniz. Roku 1000'den fazla kelimeyi bilmektedir ve sizinle 50'den fazla diyalog kurabilir.\n2)Rokunun neleri bildiğini tam olarak öğrenmek için onunla konuşmanız gerekmektedir. Roku bilmediği bir durum olduğunda 'Üzgünüm söylediğin şeyi anlamadım' diyecektir. Bunun dışında size cevap vermeye çalışacaktır. Deneyin ve görün.. 'Nasılsın diyerek başlayabilirsiniz.\n3)Diğer tüm sorularınızı cebecicihat@hotmail.com'a mail atarak öğrenebilirsiniz.")
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
def interface():
    pencere = Tk()
    uygulama = Frame(pencere)
    while(True):
        playsound("interface.mp3")
        continue
    center_window(250, 545) 
    pencere.mainloop()
def roku():
    while(True):
        isik="kapali"
        giris()
        while(True):
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print("Veri bekleniyor..")
                audio = r.listen(source)
                r.adjust_for_ambient_noise(source)
                print("Arka plan gürültüsü:" + str(r.energy_threshold))
                data = ""
            try:
                data = r.recognize_google(audio, language='tr-tr')
                data=data.lower()
                print("Bunu Söyledin :" + data)
                if data in merhaba:
                    speak(merhabacevap)
                elif data in ad:
                    speak(adcevap)              
                elif data in cihatcebeci:
                    speak(cihatcebecicevap)
                elif data in ses :
                    speak(sescevap)
                elif data in naber:
                    speak(nabercevap)
                elif data in iyidir:
                    speak(iyidircevap)
                elif data in kotudur:
                    speak(kotudurcevap)
                elif data in nerelisin:
                    speak(nerelisincevap)
                elif data in calismak:
                    speak(calismakcevap)
                elif data in hobi:
                    speak(hobicevap)
                elif data in boszaman:
                    speak(boszamancevap)
                elif data in duymak:
                    speak(duymakcevap)
                elif data in kayit:
                    speak(kayitcevap)
                elif data in soru:
                    speak(sorucevap)
                elif data in yas:
                    speak(yascevap)
                elif data in neleryaparsin:
                    speak(neleryaparsincevap)
                elif data in aclik:
                    speak(aclikcevap)
                elif data in aclik1:
                    speak(aclik1cevap)
                elif data in uyku:
                    speak(uykucevap)
                elif data in uyku1:
                    speak(uyku1cevap)
                elif data in arkadas:
                    speak(arkadascevap)
                elif "onhan" in data.split():
                    speak(onhancevap)
                ###SES###
                elif data in sesazalt:
                    dusur()
                    playsound("sesayari.mp3")
                    continue
                elif data in sesarttir:
                    yukselt()
                    playsound("sesayari.mp3")
                    continue
                elif data in seskapat:
                    sifir()
                    continue
                elif data in sesac:
                    full()
                    playsound("sesayari.mp3")
                    continue
                ###ZAMAN###
                elif data in saat:
                    zaman = time.strftime("%H:%M:%S")
                    speak("Saat şuan"+ str(zaman))
                elif data in tarih:
                    locale.setlocale(locale.LC_ALL, 'turkish')
                    tarihzaman = time.strftime("%d:%B:%Y:%A")
                    speak("Bugün"+ str(tarihzaman))
                ##HAVA DURUMU#
                elif 'hava' in data.split():
                    data = data.split()
                    havadurumu= ""
                    for i in data[:-1]:
                        havadurumu = havadurumu + i
                    speak("Lütfen bekle,"+havadurumu+"ilinin hava durumuna bakıyorum")
                    chrome_options = Options()
                    chrome_options.add_argument("--headless")
                    chrome_options.add_argument("--window-size=1920x1080")
                    driver = webdriver.Chrome(chrome_options=chrome_options,executable_path="C:/Users/chromedriver.exe")
                    driver.get("https://www.mgm.gov.tr/?il="+havadurumu)
                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    havadurumuguncel = [span.text for span in soup.section('span',class_="pull-left")]
                    noktalama = str.maketrans("","","\n")
                    noktalama1 = str.maketrans("","","n")
                    havadurumuguncel = str(havadurumuguncel).translate(noktalama)
                    havadurumuguncel = str(havadurumuguncel).translate(noktalama1)
                    havadurumuguncel = havadurumuguncel.lower()
                    speak(havadurumu + "ilinde sıcaklık şu an" +str(havadurumuguncel).strip())
                    driver.close()
                #BEKLEME MODU#
                elif data in bekleme:
                    playsound("logout.mp3")
                    break
                #BEKLEME MODU SONU#
                #YOUTUBE#
                elif "çal" in data.split():
                    data = data.split()
                    parcaismi = ""
                    for i in data[:-1]:
                        parcaismi = parcaismi + i
                    speak("Lütfen bir kaç saniye bekle, şimdi "+ parcaismi +" isimli parçayı çalacağım")
                    driver = webdriver.Chrome("C:/Users/chromedriver.exe")
                    driver.get("https://www.youtube.com/results?search_query="+parcaismi);
                    select_element = driver.find_elements_by_xpath('//*[@id="video-title"]')
                    for option in select_element:
                        option.find_element_by_xpath('//*[@id="video-title"]').click()
                        print("Video Açılıyor!!")
                        break
                #YOUTUBE SONU#
                #YOUTUBE KAPATMA#
                elif "kapat" in data.split():
                    data = data.split()
                    driver.close()
                    speak("İsteğin üzerine şuan çalan şeyi durdurdum")
                    continue
                #YOUTUBE KAPATMA SONU#
                #NOT ALMA SİSTEMİ#
                elif "not" in data.split():
                    data = data.split()
                    notkonusmasi= ""
                    for i in data [:-1]:
                        notkonusmasi = notkonusmasi + i
                    dosya = open("not.txt","a",encoding="utf-8")
                    dosya.write("Notun Başı \n")
                    dosya.write(notkonusmasi+"Notun Sonu")
                    dosya.close()
                    speak("Söylediğin cümleler not olarak kaydedildi")
                    continue
                elif data in notoku:
                    dosya = open("not.txt","r",encoding="utf-8")
                    oku = dosya.read()
                    speak("Notlarınızı okuyorum,"+oku)
                    dosya.close()
                    continue
                elif data in notsil:
                    dosya = open("not.txt","w",encoding="utf-8")
                    dosya.write("")
                    dosya.close()
                    speak("Notlarınız tamamen temizlendi")
                    continue
                #NOT ALMA SİSTEMİ SONU#
                #BİLGİ ARAMA SİSTEMİ#
                elif "bilgi" in data.split():
                    data = data.split()
                    bilgiterimi= ""
                    for i in data[:-1]:
                        bilgiterimi = bilgiterimi + i
                    speak("Seni birkaç saniye bekleteceğim Wikipedia'da arıyorum,"+bilgiterimi)
                    chrome_options = Options()
                    chrome_options.add_argument("--headless")
                    chrome_options.add_argument("--window-size=1920x1080")
                    driver = webdriver.Chrome(chrome_options=chrome_options,executable_path="C:/Users/chromedriver.exe")
                    driver.get("https://duckduckgo.com/?q="+bilgiterimi+"+wikipedia")
                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    yazi1 = [div.text for div in soup.findAll('div',id="r1-0")]
                    yazi = [div.text for div in soup.findAll('div',class_="result__snippet js-result-snippet")]
                    for yazi1 in yazi:
                        speak(bilgiterimi + " aradınız, "+str(yazi1))
                        break
                    driver.close()
                #BİLGİ ARAMA SİSTEMİ SONU#
                #KRİPTO PARA SORGULAMA#
                elif "kripto" in data.split():
                    data = data.split()
                    kriptoadi= ""
                    for i in data[:-1]:
                        kriptoadi = kriptoadi + i
                    speak("Şimdi"+kriptoadi+"güncel kurunu araştırıyorum")
                    driver = webdriver.Chrome("C:/Users/cebec/Desktop/Roku/driver/chromedriver.exe")
                    driver.get("https://www.worldcoinindex.com/coin/"+kriptoadi)
                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    noktalama = str.maketrans("","","\n")
                    noktalama1 = str.maketrans("","","n")
                    kriptoguncel = [span.text for span in soup.findAll('span',class_="span-coinprice")]
                    kriptoguncel = str(kriptoguncel).translate(noktalama)
                    kriptoguncel = str(kriptoguncel).translate(noktalama1)
                    kriptoguncel = kriptoguncel.lower()
                    print(str(kriptoguncel).strip()) 
                    speak(kriptoadi + "şuan" +str(kriptoguncel).strip())
                    driver.close()
                #DÖVİZ SORGULAMA# #YAPIM AŞAMASINDA#
                elif "döviz" in data.split():
                    data = data.split()
                    dovizadi= ""
                    for i in data[:-1]:
                        dovizadi = dovizadi + i
                    speak("Şimdi"+dovizadi+"güncel kurunu araştırıyorum")
                    driver = webdriver.Chrome("C:/Users/cebec/Desktop/Roku/driver/chromedriver.exe")
                    driver.get("https://canlidoviz.com/doviz-kurlari/"+dovizadi)
                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    noktalama = str.maketrans("","","\n")
                    noktalama1 = str.maketrans("","","n")
                    dovizguncel = [div.text for div in soup.findAll('div',class_="status")]
                    dovizguncel = str(dovizguncel).translate(noktalama)
                    dovizguncel = str(dovizguncel).translate(noktalama1)
                    dovizguncel = dovizguncel.lower()
                    print(str(dovizguncel).strip()) 
                    speak(dovizguncel + "şuan" +str(dovizguncel).strip())
                    driver.close()
                else:
                    speak("Maalesef söylediğin şey veritabanımda bulunmuyor, ne demek istediğini anlayamadım")
                    continue
            except sr.UnknownValueError:
                print("Veri Alınamadı.")
                continue
        sys.stdout = orig_stdout
        f.close()
rokuArayuz_run = Thread(target=rokuArayuz)
rokuArayuz_run.start()
interface_run = Thread(target=interface)
interface_run.start()
roku()
