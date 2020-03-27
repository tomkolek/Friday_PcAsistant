import os
os.system("cls")

file = open("res\config.cfg", "r", encoding="utf-8")
text = file.read()
file.close()

text = text.split("\n#\n")
softList = text[0].split("\n")
for a in range(len(softList)):
    softList[a] = softList[a].split("&")
    softList[a][2] = softList[a][2].split("*")
del text

def getType(TYPEa):
	try:
		TYPEb = int(TYPEa)
	except:
		TYPEb = TYPEa
	TYPEc = str(type(TYPEb)).split("'")
	return TYPEc[1]


def getCommand():
	TEXT = input("\n> ")
	TEXT = TEXT.split(" ")

	if "EDYTUJ" in TEXT[0].upper():
		edit(TEXT)

	elif "USUŃ" in TEXT[0].upper() or "USUN" in TEXT[0].upper():
		remove(TEXT)

	elif "DODAJ" in TEXT[0].upper():
		add(TEXT)

	elif "ZAPISZ" in TEXT[0].upper():
		save()

	elif "WYJDŹ" in TEXT[0].upper() and len(TEXT) == 1 or  "ZAMKNIJ" in TEXT[0].upper() and len(TEXT) == 1:
		exit()
		#save()

	elif "POMOC" in TEXT[0].upper():
		help(TEXT)

	elif "LISTA" in TEXT[0].upper():
		print("\n   Rodzaj - Nazwa - Sposoby wypowiadania - Ścieżka/Adres strony\n")
		for a in range(0, len(softList)):
			print(f"	{a+1}. {softList[a][0]}, {softList[a][1]} - {softList[a][2]}, \"{softList[a][3]}\"")

	else:
		print('Nieprawidłowe polecenie. Użyj "pomoc"')


def edit(CMD):
	if len(CMD) == 2:
		try:
			number = int(CMD[1])
		except:
			number = CMD
			#TYPEb = TYPEa
	
		if getType(number) == 'int':
			if number >= 1 and number <= len(softList):
				#print("poprawna składnia")

				getInput = input("\nPodaj rodzaj WEB lub SOFT.\n> ").upper()
				if getInput != "":
					softList[number-1][0] = getInput

				getInput = input("\nPodaj nazwę, którą ma powiedzieć asystent.\n> ")
				if getInput != "":
					softList[number-1][1] = getInput

				getInput = input('\nWypisz po przecunku możliwe sposoby wypowiedzenia nazwy programu, np. "przeglądarkę, chrome"\n> ')
				if getInput != "":
					getInput = ",".join(getInput.split(", "))
					softList[number-1][2] = getInput.split(",")

				getInput = input("\nPodaj ścieżkę do pliku/adres strony.\n> ")
				if getInput != "":
					softList[number-1][3] = getInput

			else:
				print("Zły numer")
		else:
			print('Błędna składnia. Użyj "pomoc edytuj"')
	else:
		print('Błędna składnia. Użyj "pomoc edytuj"')

def save():
	softlist_process = softList

	for a in range(0, len(softList)):
		softlist_process[a][2] = "*".join(softlist_process[a][2])
		softlist_process[a] = "&".join(softlist_process[a])
	softlist_process = "\n".join(softlist_process)

	file = open("res\config.cfg", "w", encoding="utf-8")
	file.write(softlist_process)
	file.close()

def remove(CMD):
	if len(CMD) == 2:
		try:
			number = int(CMD[1])
		except:
			number = CMD
	
		if getType(number) == 'int':
			if number >= 1 and number <= len(softList):
				del softList[number-1]

			else:
				print("Zły numer")
		else:
			print("Błędna składnia")
	else:
		print("Błędna składnia")

def help(CMD):
	if len(CMD) == 2:
		if CMD[1].upper() == "EDYTUJ":
			print('\n    Polecenia "edytuj" używa się aby edyować listę programów i stron.\n' +
				  '    Użyj polecenia "lista" aby wyświetlić listę programów i stron.\n\n' +
				  '    Użycie: "edytuj NUMER"\n' +
				  '    Dalej pozostawiając puste miejsca (klikając enter) ustawienie nie zostanie zmienione.')

		elif CMD[1].upper() == "LISTA":
			print('\n    Wyświetla listę programów / stron intenetowych\n\n' +
				  '    Użycie: "lista"')

		elif any(x in CMD[1].upper() for x in ["USUŃ", "USUN"]):
			print('\n    Usuwa program/stronę z listy.\n' +
				  '    Użyj polecenia "lista" aby wyświetlić listę programów i stron.\n\n' +
				  '    Użycie: "usuń NUMER"')

		elif CMD[1].upper() == "ZAPISZ":
			print('    Zapisuje zmiany.\n\n' +
				  '    Użycie: "zapisz"')
		
		elif CMD[1].upper() == "DODAJ":
			print('    Dodaje nowy progam/stronę do listy.\n\n' +
				  '    Użycie: "dodaj"')

		elif CMD[1].upper() == "POMOC":
			print("\n    Dostępne polecenia:\n        dodaj, edytuj, lista, pomoc, usuń, zapisz\n\n    Po więcej szczegółów: \"pomoc POLECENIE\"")


		else:
			print("Nie ma tekigo polecenia")

	elif len(CMD) == 1:
		print("\n    Dostępne polecenia:\n        dodaj, edytuj, lista, pomoc, usuń, zapisz\n\n    Po więcej szczegółów: \"pomoc POLECENIE\"")

	else:
		print("Błędna składnia")

def add(CMD):
	if len(CMD) == 1:
		softList.append([0,0,0,0])
		getInput = input("\nPodaj rodzaj WEB lub SOFT.\n> ").upper()
		if getInput != "":
			softList[len(softList)-1][0] = getInput

		getInput = input("\nPodaj nazwę, którą ma powiedzieć asystent.\n> ")
		if getInput != "":
			softList[len(softList)-1][1] = getInput

		getInput = input('\nWypisz po przecunku możliwe sposoby wypowiedzenia nazwy programu, np. "przeglądarkę, chrome"\n> ')
		if getInput != "":
			getInput = ",".join(getInput.split(", "))
			softList[len(softList)-1][2] = getInput.split(",")

		getInput = input("\nPodaj ścieżkę do pliku/adres strony.\n> ")
		if getInput != "":
			softList[len(softList)-1][3] = getInput

	else:
		print('Błędna składnia. Użyj "pomoc edytuj"')


print('    Ten program ułatwia edycję pliku config.sfg\n' +
	  '    Plik config.sfg przechowuje informacje dla asystenta o programach i stronach do polecenia "otwórz".\n\n' +

	  '    Program lub strona zapisany jest na liście za pomocą 4 danych:\n' +
	  '     - rodzaj: program (SOFT) lub strona internetowa (WEB)\n' +
	  '     - nazwa programu lub strony którą wypowie asystent (np. "jutjuba" zostanie wypowiedziane "Otwieram Jutjuba")' +
	  '     - możliwe warianty które użytkownik może wypowiedzieć (np. "Google, gogle")' +
	  '     - adres strony (np. "google.com") lub ścieżka do programu lub pliku (np. "C:\\Programy\\Word.exe")\n\n' +

	  '    Kiedy powiesz do asystenta "Otwórz Google" lub "Otwórz gogle" ten wyszuka "Google" lub "gogle"\n' +
	  '    w całym spisie programów i stron .\n' +

	  '\n    Użyj polecenia "pomoc"')
while 1:
	getCommand()