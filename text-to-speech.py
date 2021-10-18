from gtts import gTTS
import os
name=input("Enter name of notes file: ")
n=name+".txt"
with open(n,'r') as file:
    mytext = file.read()
print(mytext)
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
m=name+".mp3"
myobj.save(m)
os.system("start "+m)
