import speech_recognition as sr
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Mikrofon z nazwą \"{1}\" znaleziony jako `Microphone(device_index={0})`".format(index, name))
input("naciśnij enter")
