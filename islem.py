elif "topla" in data.split():
                    data = data.split()
                    toplama = data
                    sonuc = int(toplama[0])+int(toplama[2])
                    speak("İşlem sonucu:"+str(sonuc))
                elif "çıkart" in data.split():
                    data = data.split()
                    cikarma = data
                    sonuc = int(cikarma[0])-int(cikarma[2])
                    speak("İşlem sonucu:"+str(sonuc))
                elif "çıkar" in data.split():
                    data = data.split()
                    cikarma = data
                    sonuc = int(cikarma[0])-int(cikarma[2])
                    speak("İşlem sonucu:"+str(sonuc))
                elif "böl" in data.split():
                    data = data.split()
                    bolme= data
                    sonuc = int(bolme[0])/int(bolme[2])
                    speak("İşlem sonucu:"+str(sonuc))
                elif "çarp" in data.split():
                    data = data.split()
                    carpma = data
                    sonuc = int(carpma[0])*int(carpma[2])
                    speak("İşlem sonucu:"+str(sonuc))
