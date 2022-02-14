# RokuAssistant
<center><p><img src="https://i.hizliresim.com/1cmgomk.png" alt="Roku Assistant"></p></center>

Siri ve Google Asistan'dan örnek alınarak hazırlanan, Windows ve Raspian işletim sistemleri ile uyumlu basit yapay zekaya sahip kişisel asistan. Python yazılım diliyle oluşturuluyor. 2019 yılında başlattığım ve küçük küçük geliştirmeler uyguladığımız Roku Asistan, temel olarak Google Asistan ve Siri gibi yazılımları örnek alıyor. Ancak başlattığım zamanlarda herhangi bir yapay zeka tecrübem bulunmadığı için, program tamamen analog olarak çalışıyor.


%100 Python ile oluşturulan ve 2000+ satıra sahip olan Roku Asistan, temel olarak bir sesli asistanın çalışma mantığını gözler önüne seriyor. Python yazılım dilinde yeni çalışmaya başlayan kişilerin bir çoğu böyle bir sistem geliştirerek hem birçok kütüphane hakkında fikir sahibi olabilir hem de kendilerini geliştirebilirler. Benim projeyi hazırlamam ise yaklaşık 1 hafta sürdü ve sonrasında geliştirerek ilerleme sağladım.


<b>"rokusistem.pyw"</b> dosyası, programın başlatıldığı ve kodların büyük bölümünün yer aldığı dosyadır. Bu dosya içerisinde yüklenen kütüphaneleri görüntüleyebilir, Roku Assistanın Windows için tasarlanan arayüzünü inceleyebilir ve if else yapısı ile nasıl bir mantık oluşturulduğunu anlayabilirsiniz. Bunun yanında Selenium ve Urllib gibi kütüphanelerle internete nasıl bağlandığını ve buradan verileri nasıl çekip kullanıcıya sunduğumu görebilirsiniz. Projede kullanılan Python kütüphanelerini şöyle sıralayabiliriz:

> <b>Tkinter</b> - Roku Assistant temel bilgilendirmeleri ve konsol gibi ögelerin görüntülenmesinin sağlanması için arayüz oluşturma amacıyla kullanıldı. Yazılım her çalıştırıldığını giriş efektinden sonra kullanıcının ekranında görüntülenebilir.

> <b>gTTS</b> - Sanal asistanın sesi Google Developers üzerinden gTTS kütüphanesi ile çekildi. Google Translate üzerinde duyduğumuz Türkçe sesin aynısı olan bu ses metinleri okuyabilir ve söylenenleri metine çevirebilir.

> <b>Selenium</b> - Tarayıcıların otomatik bir şekilde çalışmasını sağlayan ve oldukça kullanışlı bir yazılım olan Selenium, asistan tarafından Youtube, Hava durumu, Döviz hesaplamaları ve internet araştırmaları gibi amaçlar doğrultusunda kullanıldı.

> <b>BeautifulSoup</b> - Selenium tarafından açılan web sitelerinin yazılım tarafından ayıklanması gerekmektedir. Örneğin asistandan bir bilgiyi araştırmasını istediğinizde Wikipedia'ya girecektir ve tüm sayfanın kodlarını çekecektir. BeautifulSoup sayesinde sayfa içerisinde hangi alanların ayıklanması ve kullanıcıya iletilmesi gerektiği gibi ayarların yapılması sağlandı. Döviz hesaplaması, hava durumu paylaşımı gibi özelliklerde de bu kütüphane kullanıldı.

> <b>PlaySound</b> - Asistan içerisinde açılışta, kapanışta, ses almak istediğinde, belli ayarlar yapıldığında kullanılacak olan ses efektleri bulunmaktadır. Bu ses efektlerini sorunsuz bir şekilde çalıştırmak için ise PlaySound kütüphanesi kullanıldı.

> Tüm bunların yanında verilerin işlenmesi, işlemcinin gücünün ayarlanması, cihaz sesinin değiştirilmesi, asistanın bekleme ve kapatma gibi modlarının yüklenmesi ve benzeri amaçlar doğrultusunda isimsiz kütüphaneler ve kaynaklardan yardım alındı. Örneğin bilgisayarın ses seviyesini asistanla konuşarak arttırmak veya azaltmak için Keyboard.py, sesayari.py, sound.py gibi ayrı programlar birleştirildi. Asistanda bulunan hesap makinesi gibi (islem.py) basit uygulamalar için de ayrı sayfalar bulunmaktadır. 

Program içerisinde söylediğiniz tüm kelimeler ve yaptığınız tüm işlemler konsol isimli .txt dosyası üzerine kaydedilmektedir ve Tkinter ile hazırlanan arayüz üzerinden görüntülenebilmektedir. Programı kapatsanız dahi silinmeyen bu veriler, yine arayüzde bulunan "Konsol Temizle" butonu sayesinde temizlenebilmektedir. Bunun yanında verilen komutların sonunda "not" ifadesini kullanmanız halinde söylediğiniz tüm kelimeler not.txt isimli dosyaya kaydedilecektir. "Notlarımı Sil" demeniz halinde ise dosya içerisinde bulunan tüm veriler temizlenecektir. Bunlara benzer özellikleri de içerisinde barındıran Roku Assistant'ı daha iyi anlamak için tüm kod dosyalarını inceleyebilir ve bilgisayarınızda bu yazılımı çalıştırabilirsiniz. Arayüz üzerinden de yapabileceğiniz işlemlerin büyük çoğunluğu paylaşılmış durumdadır.

<center><p><img src="https://i.hizliresim.com/d1k4sx1.png" alt="Roku Assistant Arayüzü"></p></center>
