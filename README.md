# Friday - Osobysty asystent
###### *tylko dla Windows (testowane na Windows 10, może działać na innych)*

-----

**Friday** to osobisty asystent, który jest we wczesnej fazie rozwoju. Aby go wywołać Powiedz *"Hej Friday"*, po usłyszeniu dźwięku można wypowiedzieć polecenie. Polecenia nie muszą być wypowiadane kropka w kropkę. Można zamieniać słowa albo powiedzieć różne odmiany słów. Jeżeli polecenie nie będzie istnieć lub zostanie źle zrozumiane asystent odpowie, że *"nie może odpowiedzieć na to pytanie"*
###### *(Jeżeli polecenie zostało powiedziane poprawnie, a asystent nie zrozumiał wypowiedzi zgłoś proszę ten błąd)*

## Funkcje:
* Godzina - *"Która godzina"*
* Dzień tygodni oraz dzisiejsza data - *"Jaki jest dzisiaj dzień"*
* *(Więcej funkcji w trakcie robienia)*

## Wykorzystane biblioteki:
* ctypes
* gTTS
* os
* simpleaudio
* speech_recognition
* webbrowser

---
### Instalacja:
* Jeśli nie masz zainstalowanego środowiska Python otwórz plik *"Start exe.exe"*. Został skompilowany za pomocą biblioteki "pyinstaller"* i spakowany do archiwum *"Start exe rar.part1.rar"* i *"Start exe rar.part2.rar"*. Wypakuj go do tego samego folderu. Aby asystent działał poprawnie przejdź do folderu `res/Sounds` i rozpakuj ffmpeg do tego samego folderu w którym się znajduje. 
* Jeśli masz zainstalowane środowisko Python zaoinstaluj biblioteki zymienione powyżej i uruchom plik `Start.py`

Wszystkie pliki możesz pobrać [stąd.](https://github.com/tomkolek/Friday_PcAsistant/archive/master.zip "Github Friday repository")

Dostępna jest mapa projektu na stronie [Trello.](https://trello.com/b/NnwU2e8S/friday-osobisty-asystent "Friday roadmap")

Projekt nie jest przystosowany dla systemów MacOS ani Linux. Wykożystane są tu biblioteki niezgodne z tymi systemami. Możliwe, że w trakcie rozwijania projektu zostaną utworzone wersje zgodne z innymi systemami operacyjnymi.

Proszę o zgłaszanie błędów jeżeli takie wystąpią.
