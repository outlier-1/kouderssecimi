from splinter import Browser
import time
import os

class DersSecimi:
    def __init__(self):
        self.success = False
        os.system("cls")	
        print("**************** KOU DERS SECIMI v1.0 For Windows-64 Bit ****************")
        self.ogrNo = input("Ogrenci Numaraniz: ")
        self.sifre = input("Ogrenci Bilgi Sistemi Sifreniz: ")
        print(self.ogrNo +" Numarası ve " + self.sifre + " sifresi ile giris yapiliyor..")
        self.browser = Browser('chrome')

    url = "https://ogr.kocaeli.edu.tr/koubs/ogrenci/index.cfm"

    def brute_force(self):
        self.browser.find_by_name(name="OgrNo").fill(self.ogrNo)
        self.browser.find_by_name(name="Sifre").fill(self.sifre)
        self.browser.find_by_name('Ara').click()
        if self.browser.is_text_present('Ders İşlemleri'):
            print("Giris Basari Ile Saglandi. Ders Secimini Tamamlamadan Bu Pencereyi Kapamayin.")
            self.success = True
            time.sleep(3600)
        else:
            self.brute_force()
            time.sleep(1)

    def start(self):
        print("--------------------------------------------")
        print("Google Chrome Baslatiliyor...")
        print("--------------------------------------------")
        self.browser.visit(self.url)
        print("Google Chrome Basari Ile Baslatildi.")
        print("--------------------------------------------")
        print("Ogrenci Bilgi Sistemine Giriliyor..")
        self.brute_force()


ders_secimi = DersSecimi()
ders_secimi.start()

