import os
import speech_recognition as sr
import ffmpeg

file_name="pm_speech"

command2mp3 = "ffmpeg -i speeches/"+file_name+".mp4 speeches/"+file_name+".mp3"
command2wav = "ffmpeg -i speeches/"+file_name+".mp3 speeches/"+file_name+".wav"

os.system(command2mp3)
os.system(command2wav)

r = sr.Recognizer()
audio = sr.AudioFile('speeches/'+file_name+'.wav')

with audio as source:
    audio = r.record(source, offset=0, duration=100)
    try:
        print("Recognizing: ")
        output_speech=r.recognize_google(audio, language="hi-IN")
        print("Speech is: ", output_speech)
        with open("speeches/"+file_name+".txt", "w", encoding="utf-8") as txt_file:
            print(output_speech, file=txt_file)
            txt_file.close()

    except Exception as e:
        print(e)
        print("Retry!")
