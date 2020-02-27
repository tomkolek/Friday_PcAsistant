file = open("config.cfg", "r", encoding="utf-8")
text = file.read()

text = text.split("\n")
for a in range(len(text)):
	text[a] = text[a].split("&")
	text[a][2] = text[a][2].split("*")
	
print(text, "\n")