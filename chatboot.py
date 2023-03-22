from cleverbotfree import Cleverbot
from googletrans import Translator
from gtts import gTTS  
import random
import os
from playsound import playsound
import speech_recognition as sr


translator = Translator()
rec = sr.Recognizer()

def record():
    with sr.Microphone()  as source:
        voice_rec = ''
        audio =  rec.listen(source, 5,5)
        try :
            voice_rec = rec.recognize_google(audio,language ='tr-TR')
        except sr.UnknownValueError:
            speak('anlayamadım')
        except sr.Recognizer:
            speak('sistem hata aldı')
        return voice_rec
            

def speak(text):
    tts = gTTS(text,lang = 'tr')
    rand = random.randint(1,1000)
    file = 'audio' + str(rand) + '.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)
    
    
    
    


def translate_text(who, text, lang):
    text_tranlated = translator.translate(text, dest = lang)
    print(who, "(" , lang , "):" ,  text_tranlated.text)
    return text_tranlated.text


@Cleverbot.connect
def chat(bot, user_prompt, bot_prompt):
    while True:
        user_input = record()
        print(user_prompt,user_input)
        user_input_en = translate_text(user_prompt, user_input, 'en')
        if user_input =="quit":
            break
        reply = bot.single_exchange(user_input_en)
        print(bot_prompt, reply)
        bot_reply_tr = translate_text(bot_prompt, reply ,'tr')
        speak(bot_reply_tr)
        
    bot.close()
    
chat("You:", "Cleverbot:")




