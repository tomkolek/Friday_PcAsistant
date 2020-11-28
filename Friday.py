import speech_recognition as sr
#from gtts import gTTS
import webbrowser as wb
from datetime import datetime
import simpleaudio as sa
import os
import ctypes
import requests
#import time

r = sr.Recognizer()


class config:
    file = open("res/config.cfg", "r", encoding="utf-8")
    text = file.read()
    
    text = text.split("\n#\n")

    softList = text[0].split("\n")
    for a in range(len(softList)):
        softList[a] = softList[a].split("&")
        softList[a][2] = softList[a][2].split("*")

    del text

class info:
    assistantName = ['HEJ FRIDAY', 'HEY FRIDAY', 'HIFI DAY', 'HEJ FAJNEJ', 'FIVE A DAY', 'HAY DAY', 'PLAY FRIDAY', 'HIGH FAMILY', 'TEJ FAJNEJ', 'NAJFAJNIEJ', 'HEJ HEJ', 'I FAJNEJ']

    months = [
                ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'Octobel', 'November', 'December'], # po angielsku
                ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec', 'Lipiec', 'Sierpień', 'Wrzesień', 'Październik', 'Listopad', 'Grudzień'], # po polsku
                ['Stycznia', 'Lutego', 'Marca', 'Kwietnia', 'Maja', 'Czerwca', 'Lipca', 'Sierpnia', 'Września', 'Października', 'Listopada', 'Grudnia'] # po polsku, odmienione
             ]
    
    daysOfTheWeek = [
                ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
                ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']
               ]

    dayNumbers = [
                    ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28',
                    '29', '30', '31'],
                    ['pierwszy', 'drugi', 'trzeci', 'czwarty', 'piąty', 'szósty', 'siódmy', 'ósmy', 'dzwiewiąty', 'dziesiąty', 'jedenasty', 'dwunasty', 'trzynasty', 'czternasty',
                    'piętnasty', 'szesnasty', 'siedemnasty', 'osiemnasty', 'dziewiętnsty', 'dwudziesty', 'dwudziesty pierwszy', 'dwudziesty drugi', 'dwudziesty trzeci',
                    'dwudziesty czwarty', 'dwudziesty piąty', 'dwudziesty szósty', 'dwudziesty siódmy', 'dwudziesty ósmy', 'dwudziesty dzwiewiąty', 'trzydziwsty',
                    'trzydziesty pierwszy']
                 ]

class do:
    # Przechwytuje głos
    def captureVoice():
        global capturedVoice
        with sr.Microphone() as source:
            audio = r.listen(source)
        capturedVoice = r.recognize_google(audio, language='pl-PL',)


    # Włącza / wyłącza konsolę
    def console(NUM):
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), NUM)
    

    def date(DAY):
        if DAY == "today":
            date = datetime.now().strftime('%A %d %B').split(" ")
            for a in range(0,12):
                if date[2] == info.months[0][a]:
                    date[2] = info.months[2][a]
            for b in range(0,30):
                if date[1] == info.dayNumbers[0][b]:
                    date[1] = info.dayNumbers[1][b]
            for c in range(0,7):
                if date[0] == info.daysOfTheWeek[0][c]:
                    date[0] = info.daysOfTheWeek[1][c]
            
            date = f"Jest {date[0]}, {date[1]} {date[2]}."
            do.say(date)


    # Wypowiada aktualną godzinę
    def hour():
        x = 'jest ' + datetime.now().strftime('%H:%M')
        x = str(x)
        do.say(x)


    # Otwiera plik który znajduje się w podanej frazie
    def open(NAME):
        text = NAME.split(" ")
        del text[0]
        if len(text) > 1:
            text = " ".join(text)

        for a in range(0, len(config.softList)):
            #print(f"a = {a}")
            for b in range(0, len(config.softList[a][2])):
                #print(f"b = {b}")
                if config.softList[a][2][b] in text:
                    
                    if config.softList[a][0] == 'WEB':
                        
                        wb.open_new_tab(config.softList[a][3])
                        do.say(str('Otwieram ' + config.softList[a][1]))
                        
                    elif config.softList[a][0] == 'SOFT':
                        
                        os.startfile(config.softList[a][3])
                        do.say(str('Otwieram ' + config.softList[a][1]))
                    else:
                        print("ZLE ZDEFINIOWANY RODZAJ OPROGRAMOWANIA W PLIKIU config.softList.py")
                #else:
                #    print("b nie")


    # Odtważa dzwięk
    def playSound(FILE):
        wave_obj = sa.WaveObject.from_wave_file(FILE).play()
        wave_obj.wait_done()
    

    # Generuje, włącza plik i usuwa go
    def say(SAY):
        print(SAY)
        print('generowanie')
        url = 'https://translate.google.com/translate_tts?ie=UTF-8&q=' + SAY + '&tl=pl&ttsspeed=1&total=1&idx=0&client=tw-ob&textlen=23&tk=58620.403981'
        r = requests.get(url, allow_redirects=True)
        open('res/Sounds/SAIDi.mp3', 'wb').write(r.content)
        print('wygenerowano')
        
        os.chdir('res/Sounds')
        os.system('start CONVERT.vbs')
        os.chdir('..')
        os.chdir('..')
    
        while 1:
            try:
                do.playSound('res/Sounds/SAIDo.wav')
                break
            except:
                pass
    
        os.remove('res/Sounds/SAIDi.mp3')
        os.remove('res/Sounds/SAIDo.wav')


    # Szuka w google URL
    def searchGoogle(sr):
        url = str("https://www.google.com/search?q=") + str(sr)
        wb.open(url)
    

    # Szuka w google URL
    def searchYoutube(sr):
        url = str("https://www.youtube.com/search?q=") + str(sr)
        wb.open(url)

class assistant:
    # Wyczekuje wywołania
    def listenToTrigger():
        while True:
            try:
                do.captureVoice()
                if any(x in capturedVoice.upper() for x in info.assistantName):
                    do.playSound("res/Sounds/start_recognition.wav")
                    break
                else:
                    pass 
            except:
                print('błąd')
                pass
            print("następna próba")

    # Wyszukuje polecenia w wypowiedzi
    def searchForCommand():
        global capturedVoice


        # Polecenie "Otwórz"
        if any(a in capturedVoice for a in ["Otwórz", "Włącz", "Uruchom", "Pokaż", "odpal", "odpalaj"]):
            do.open(capturedVoice)

        elif "która godzina" in capturedVoice or "Podaj godzinę" in capturedVoice or "Jaka jest godzina" in capturedVoice:
            do.hour()

        elif "nieważne" == capturedVoice:
            do.playSound("res/Sounds/stop_recognition.wav")

        elif "Który" in capturedVoice or "Jaki" in capturedVoice or "dzień" in capturedVoice or "Co" in capturedVoice or "dzień" in capturedVoice:
            if "dzisiaj" in capturedVoice or "dziś" in capturedVoice:
                do.date("today")


        else:
            do.playSound("res/Sounds/sorry.wav")



do.playSound("res/Sounds/Startup.wav")

while True:
    assistant.listenToTrigger()
    try:
        do.captureVoice()
        print(capturedVoice)
        assistant.searchForCommand()
    except:
        do.playSound("res/Sounds/stop_recognition.wav")
	
do.playSound("res/Sounds/Shutdown.wav")



