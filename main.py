

import os
import sys
import time

header={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36"}

def b():
    print("Kopyalanmasını İstediğiniz URL'yi Girin")
    url = input("URL Gir:")
    r = requests.get(url,headers=header)
    if r.status_code == 200:
        win32api.MessageBox(0,"İşlem Başarılı. URL Doğrulandı Ve Bağlanıldı","HTMLCopy 0.7")
    elif r.status_code == 204:
        win32api.MessageBox(0,"İşlem Başarılı Fakat İçerik Yok. Devam Ediliyor","HTMLCopy 0.7")
    elif r.status_code == 301:
        win32api.MessageBox(0,"İçerik Kalıcı Olarak Taşınmış !","HTMLCopy 0.7")
        sys.exit()
    elif r.status_code == 302:
        win32api.MessageBox(0,"İçerik Geçici Olarak Taşınmış !","HTMLCopy 0.7")
        sys.exit()
    elif r.status_code == 400:
        win32api.MessageBox(0,"İçeriğe Ulaşılamıyor !","HTMLCopy 0.7")
        sys.exit()
    elif r.status_code == 404:
        win32api.MessageBox(0,"İçerik Bulunamadı !!!","HTMLCopy 0.7")
        sys.exit()
    elif r.status_code == 408:
        win32api.MessageBox(0,"Zaman Aşımına Uğradı/Bağlanılamadı","HTMLCopy 0.7")
        sys.exit()
    elif r.status_code == 502:
        win32api.MessageBox(0,"Geçersiz Ağ Geçidi !","HTMLCopy 0.7")
        sys.exit()
    else:
        win32api.MessageBox(0,'Bilinmeyen Bir Hata Oluştu !','HTMLCopy 0.7')
        sys.exit()
    time.sleep(5)
    s = BeautifulSoup(r.content,"html.parser")
    code = f"{s}"
    kdos = input("Kodlar Kaydedildi. Kaydedilecek HTML Dosya Adı Girin (Uzantısız):")
    open(f"{kdos}.html","x")
    try:
        file = open(f"{kdos}.html","a")
        file.write(f"{code}")
        file.close()
    except:
        win32api.MessageBox(0,"İşlem Tamamlanamadı !","HTMLCopy 0.7")
    win32api.MessageBox(0,"Dosya Kaydedildi !","HTMLCopy 0.7")
    print("Kodlara Bakmak İstiyorsan 1 Yaz Çıkmak İçin 2")
    soru = int(input("Seç:"))
    if soru == 2:
        sys.exit()
    elif soru == 1:
        print(code)
    else:
        win32api.MessageBox(0,'Ne Dediğini Anlamadım ?','HTMLCopy 0.7')
        sys.exit()

os.system('title HTML Copy')
print("Modüller Kurulacak (Önceden Kurmadıysanız Program Hatalı Çalışır)")
print("1-Ben Kurmadım Bekle Kurayım\n2-Ben Zaten Kurdum")
s = int(input("Seç:"))
if s == 1:
    os.system('py -3 -m pip install --upgrade pip >nul')
    os.system('py -3 -m pip install requests >nul')
    os.system('py -3 -m pip install BeautifulSoup4 >nul')
    os.system('py -3 -m pip install pywin32 >nul')
    import requests
    from bs4 import BeautifulSoup
    import win32api
    vercont = requests.get("https://htmlcopy-version-control.glitch.me/hcs.txt")
    time.sleep(3)
    if vercont.status_code != 200:
        win32api.MessageBox(0,"Versiyonunuz Günceldir","HTMLCopy 0.7")
    else:
        win32api.MessageBox(0,"Versiyonunuz Güncel Değildir !","HTMLCopy 0.7")
    b()
elif s == 2:
    import requests
    from bs4 import BeautifulSoup
    import win32api
    vercont = requests.get("https://htmlcopy-version-control.glitch.me/hcs.txt")
    time.sleep(3)
    if vercont.status_code != 200:
        win32api.MessageBox(0,"Versiyonunuz Günceldir","HTMLCopy 0.7")
    else:
        win32api.MessageBox(0,"Versiyonunuz Güncel Değildir Lütfen Güncelleyin","HTMLCopy 0.7")
    b()

