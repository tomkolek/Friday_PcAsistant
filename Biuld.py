import os
os.system("pyinstaller --onefile Start.py")
print("\nKOMPILOWANIE ZAKOŃCZONE\n")

os.system("move dist\Start.exe")
os.system('rmdir dist /s /q')
os.system('rmdir build /s /q')
os.remove("Start.spec")

input("\n Skompilowano pomyślnie")
