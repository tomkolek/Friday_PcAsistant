import speech_recognition as sr

r = sr.Recognizer()


def test():
    with sr.Microphone() as source:
        #r.adjust_for_ambient_noise(source)
        print(r.energy_threshold)
        print("powiedz coś")

        audio = r.listen(source)

        try:
            print("Powiedźiałeś: " + r.recognize_google(audio, language='pl-PL'))

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

while True:
    test()