import speech_recognition as sr
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Urządzenie z nazwą \"{1}\" znalezione jako `Microphone(device_index={0})`".format(index, name))
input("\nnaciśnij enter")
