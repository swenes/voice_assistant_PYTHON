from re import X
import webbrowser
import speech_recognition as sr
from datetime import datetime
import webbrowser
import sqlite3
from sqlite3 import dbapi2
import time
from gtts import gTTS
from playsound import playsound
import random
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep, time

def instagram():
    
    path = r'C:\Users\ENES\Desktop\chromedriver.exe'
    driver = webdriver.Chrome(path)
    driver.get('https://www.instagram.com/')
    driver.maximize_window()
    sleep(3)

    kullanici_adi = driver.find_element(By.NAME, 'username')
    sifre = driver.find_element(By.NAME, 'password')

    kullanici_adi.send_keys("enes.aydgd")
    sifre.send_keys("1q2w3e4r5t")

    giris_yap = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')

    giris_yap.click()
    sleep(4)

    simdiDegil1 = driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/div/div/div/button')
    simdiDegil1.click()
    sleep(3)    

    simdiDegil2 =  driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div[3]/button[2]')
    simdiDegil2.click()
    sleep(3)

    aramaKutusu = driver.find_element(By.XPATH,'//input[@type="text"]')
    aramaKutusu.send_keys('firatresmihesap')
    sleep(10)
    
    profileGit = driver.find_element(By.XPATH,'//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div')
    profileGit.click()
    sleep(6)

    resmiAc = driver.find_element(By.XPATH , '//*[@id="react-root"]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a/div/div[2]')
    resmiAc.click()
    sleep(3)

    begen1 = driver.find_element(By.XPATH , '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button')

    begen1.click()
    sleep(3)
    

def siteyeGit(url):
    
    webbrowser.get().open(url)  


def record(ask=False):    ## bilgisayardan gelen soru varsa true yoksa false dönüp devam edecek (sadece senin için neyi aramalıyım kısmında kullanıldı.)
    with sr.Microphone() as source: ## mikrofon dinlenmeye başlandı.    tekrar
        if ask:
            speak(ask)  
        audio = r.listen(source) 
        voice = ''  # except devreye girerse voiceyi kapatmadığımızdan boş bir değer atadım hata meydana gelmemesi için
        try:
            voice = r.recognize_google(audio, language='tr-TR')
        except sr.UnknownValueError:   ## algılanan ses kelimeye dökülmediyse
            print('Anlayamadım')

        except sr.RequestError:  ## sistemsel bir hata meydana geldiğinde yakalanır
            speak("sistem çalışmadı")

        return voice


def response(voice):

    if 'Evet' in voice:
        speak('dinliyorum')

    elif 'Hayır' in voice:
        speak('görüşürüz')
        exit()
        
    elif 'nasılsın' in voice:
        speak('idare eder sen nasılsın')

    elif 'saat kaç' in voice:
        speak(datetime.now().strftime('%X'))


    elif 'arama yap' in voice:
        search = record('senin için neyi aramalıyım')
        url = 'https://www.google.com/search?q=' + search
        webbrowser.get().open(url)
        speak(search+' için bulduklarım')

    elif 'Seni kim tasarladı' in voice:
        speak('yaratıcımı tanımıyorum')

    elif 'görüşürüz' in voice:
        speak('görüşürüz')
        exit()

    elif 'İnterneti aç' in voice:
          speak('hallediyorum')
          siteyeGit('www.google.com.tr')
          sleep(3)

    elif "YouTube'u aç" in voice:
        speak('Bir saniye. hallediyorum')
        siteyeGit('www.youtube.com.tr')
        sleep(3)
    elif "Instagram'dan Fırat Üniversitesi'nin en son resmini beğenir misin" in voice:
        speak('Hemen beğeniyorum')
        instagram()  

    elif "Bugün hava nasıl" in voice:
        speak('sonuçlar karşında')
        siteyeGit('https://mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il=Elazig')
    else:
        speak('Bunu öğrenmedim.Başka bir şey söylemek istiyor musun')      ## algılanan ses kelimeye dökülüp anlamsız dizeler oluşturduysa.






def speak(string):
    tts = gTTS(string, lang='tr')
    rand = random.randint(1, 10000)
    file = 'audio-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)





while True:   ## sonsuz döngü yaratıp program başladığı andan itibaren mikrofonu dinlemeye başlıyoruz. Komut ile program harekete geçiyor
    r = sr.Recognizer()
    record()
    if 'sesim geliyor mu' in record():
        
        speak("Evet Enes. Seni dinliyorum")

        sleep(0.2)
        while 0.2:
            voice = record()
            print(voice)
            response(voice) 

        


