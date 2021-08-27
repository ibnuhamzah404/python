import pyttsx3 
import speech_recognition as sr 
import datetime
import random
import os
import wikipedia
from googletrans import Translator
import glob

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Selamat Pagi!")

    elif hour>=12 and hour<18:
        speak("Selamat Siang!")   

    else:
        speak("Selamat Mallam")  

    speak("Saya adalah ultron asisten pribadi anda, katakan sesuatu saya akan membantu anda?") 
   

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=3, phrase_time_limit=5)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='id')
        print(f"User said: {query}\n")
        

    except Exception as e:
        # print(e)    
        katakanUlang = ['katakan ulang saya tidak mendengar', 'suara kamu tidak jelas, coba katakan ulang', 'eh apa tadi saya tidak dengar', 'maaf bisa katakan ulang suara gakedengeran nih', 'kamu ngomong apa coba deh ulang', 'aku gadenger nih coba ulang dong']
        randno = random.randint(0,5)
  
        speak(katakanUlang[randno])     
        return "None"
    return query

    
    


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query

        turnof = ['daya', 'matikan', 'mati', 'turnoff', 'off', 'matikan daya', 'keluar aplikasi']
        intro = ['kamu siapa', 'perkenalkan dirimu']
        musik = ['musik', 'putar musik dong', 'setel musik', 'aku bosen nih', 'putar']
        jam = ['sekarang jam berapa', 'jam', 'pukul berapa sekarang']
        jokes = ['kamu punya jokes ga', 'coba dong ngelawak', 'hibur aku dong']
        if musik.count(query) > 0:
            speak('aku putarin musik ya biar kamu ga bosen lagi')
            music_dir = 'D:\\Folder Mang_Iyan\\Music\\yani baru'
            songs = os.listdir(music_dir)
            rd = random.choice(songs) 
            os.startfile(os.path.join(music_dir, rd))
            speak('musik kamu sudah diputar, jangan bosen lagi ya.')
        elif intro.count(query) > 0:
            speak('aku adalah asisten pribadimu, kamu bisa memanggilku ultron')
        elif  jam.count(query) > 0:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sekarang jam {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif jokes.count(query) > 0:
            
            lucu = ['tau ga kamu huruf yang selalu kedinginan itu apa? bingung ya ni aku kasih tau ya huruf b karena ditengan tengah ac hahahaha']
            
            speak(lucu[0])

           

        elif turnof.count(query) > 0:
            speak('sampai berjumpa kembali')
            exit()

        elif 'wikipedia' in query:
            speak('kamu ingin cari apa di wikipedia')
            queryWiki = takeCommand().lower()
            wikipedia.set_lang("id")
            result = wikipedia.summary(queryWiki, sentences = 2) 
  
            # printing the result
            speak(result)
        elif 'main game yuk' in query:
            while True:
                suwit = ['gunting', 'batu', 'kertas']

                speak('kamu pilih apa? batu, gunting atau kertas?')
                suwitno = random.randint(0,2)
                querySuwit = takeCommand().lower()
                
                print(suwitno)
            
                

                if suwit[suwitno] == 'gunting' and querySuwit == 'batu':
                    speak('aku pilih gunting, kamu pemenangnya!')
                    print(querySuwit)
                elif suwit[suwitno] == 'kertas' and querySuwit == 'batu':
                    speak('aku pilig batu, kamu kalah')
                    print(querySuwit)
                elif suwit[suwitno] == 'batu' and querySuwit == 'kertas':
                    speak('aku pilig batu, kamu kalah')
                elif suwit[suwitno] == 'gunting' and querySuwit == 'kertas':
                    speak('aku pilig batu, kamu kalah')
                    print(querySuwit)
                elif suwit[suwitno] == 'kertas' and querySuwit == 'gunting':
                    speak('aku pilih kertas, kamu pemenangnya!')
                elif suwit[suwitno] == 'batu' and querySuwit == 'gunting':
                    speak('aku pilih kertas, kamu pemenangnya!')
                    print(querySuwit)

                elif suwit[suwitno] == querySuwit:
                    speak('kita seri aku memilih' + querySuwit)
                else:
                    speak('tidak ada untuk pilihan' + querySuwit)

            
                speak('apa kamu ingin main lagi ? ') 

                querySuwit = takeCommand().lower()
                if 'iya' in querySuwit:
                    continue
                elif 'tidak' in querySuwit:
                    
                    speak('kamu hebat, lain kali main lagi ya')
                    exit()
      
           
            