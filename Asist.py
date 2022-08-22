from datetime import datetime
import speech_recognition as sr
from datetime import datetime
from playsound import playsound
from gtts import gTTS
import random
import os
from time import sleep
import main


#print(sr.Microphone.list_microphone_names())

r = sr.Recognizer()
mic = sr.Microphone()


print("Çalışıyor...")
def mic_text_doc():
    text = ''
    with mic as m:
        audio = r.listen(m,5,5)
        try:
            text = r.recognize_google(audio,language='tr-TR')
            print(text)
        except sr.UnknownValueError:
            text_to_speak("Seni anlayamadım.")
    
    return text


def text_to_speak(veri):
    tts = gTTS(veri,lang='tr')
    rand = random.randint(1,1000000)
    file = "ses" + str(rand) + ".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

text_to_speak("Merhaba ben Bot:Oto-Bot")
text_to_speak("Seni dinliyorum")

while True:
    text = mic_text_doc().lower()
    # text_to_speak("Seni dinliyorum")
    if "bot" in text or "otobot" in text or "robot" in text or "hey" in text:
        if "tamamdır" in text:
            text_to_speak("Uygulamadan Çıkılıyor")
            break
        elif "oynat" in text:
            text_to_speak("Oynatıyorum")
            text_to_speak("Sayfayı kapatmak için panele harf girin")
            main.playyoutube(text)
            sleep(1.5)
        elif "şuan saat kaç" in text or "saat" in text or "şu an saat kaç" in text:
            text_to_speak(datetime.now().strftime("%H:%M:%S"))
        elif "arama yap" in text:
            text_to_speak("Arama yapıyorum")
            text_to_speak("Sayfayı kapatmak için panele harf girin")
            main.aramayap(text)
            sleep(1.5)
        # elif "mesaj at" in text:
        #     text_to_speak("Mesaj atıyorum")
        #     text_to_speak("Sayfayı kapatmak için panele harf girin")
        #     sleep(1.5)
        elif "teşekkürler" in text:
            text_to_speak("Rica ederim ben Bot:Oto-Bot")
        elif "siri" in text:
            text_to_speak("")
        elif "merhaba" in text or "selam" in text:
            text_to_speak("merhaba")    
        else:
            text_to_speak("Şuan tekrar modundayım.Seni tekrar edicem.")
            text_to_speak(text)
    elif "uygulamadan çık" in text:
        text_to_speak("Uygulamadan Çıkılıyor")
        break
    else:
        pass

