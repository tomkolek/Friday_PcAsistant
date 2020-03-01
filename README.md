# Friday - Osobysty asystent
###### *tylko dla Windows (testowane na Windows 10 i 7, może działać na innych)*

-----

**Friday** to osobisty asystent, który jest we wczesnej fazie rozwoju. Aby go wywołać Powiedz *"Hej Friday"*, po usłyszeniu dźwięku można wypowiedzieć polecenie. Polecenia nie muszą być wypowiadane kropka w kropkę. Można używać innych słów lub je odmieniać. Jeżeli polecenie nie będzie istnieć lub zostanie źle zrozumiane asystent odpowie, że *"nie może odpowiedzieć na to pytanie"* i wyłączy się.
###### *(Jeżeli polecenie zostało powiedziane poprawnie, a asystent nie zrozumiał wypowiedzi zgłoś proszę ten błąd)*

## Funkcje:
* **Godzina** - *"Która godzina"*
* **Dzień tygodnia oraz dzisiejsza data** - *"Jaki jest dzisiaj dzień"*
* **Otwieranie programu/strony www** - Otwiera program lub stronę internetową (pszyszłości możliwość dodania własnych stron i programów. aktualnie dostępne tylko Google i YouTube) *"Otwórz Google"*
* *(Więcej funkcji w trakcie robienia)*

## Wykorzystane biblioteki:
* ctypes *(domyślnie)*
* gTTS
* os *(domyślnie)*
* simpleaudio
* speech_recognition
* webbrowser *(domyślnie)*

---
### Instalacja:
* Jeśli nie masz zainstalowanego środowiska Python lub chcesz skożystać ze skompilowanej wersji, wypakuj wszystkie pliki do dowolnego folderu i otwórz plik `Start.exe`.
* Jeśli masz zainstalowane środowisko Python zainstaluj biblioteki zymienione powyżej i uruchom plik `Start.py`

Wszystkie pliki możesz pobrać [stąd.](https://github.com/tomkolek/Friday_PcAsistant/archive/master.zip "Github Friday repository")

## UWAGA!
Do funkcjonowanie potrzebne jest połączenie z internetem. Jeżeli asystent nie reaguje po wywołaniu go czy wydaniu polecenia, lub reaguje z dużym opóźnieniem, sprawdź połączenie z internetem. Powolne łącze spowolni generowanie mowy.

---

Dostępna jest mapa projektu na stronie [Trello.](https://trello.com/b/NnwU2e8S/friday-osobisty-asystent "Friday roadmap")

Projekt nie jest przystosowany dla systemów MacOS ani Linux. Wykożystane są tu biblioteki niezgodne z tymi systemami. Możliwe, że w trakcie rozwijania projektu zostaną utworzone wersje zgodne z innymi systemami operacyjnymi.

Proszę o zgłaszanie błędów jeżeli takie wystąpią.
