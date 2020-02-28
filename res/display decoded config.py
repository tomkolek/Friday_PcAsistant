class config:
	file = open("config.cfg", "r", encoding="utf-8")
	text = file.read()
	
	text = text.split("\n#\n")

	softList = text[0].split("\n")
	for a in range(len(softList)):
		softList[a] = softList[a].split("&")
		softList[a][2] = softList[a][2].split("*")

	cal = text[1]

	del text
