import speech_recognition as sr 
x=sr.Recognizer()
a=0

name=input("Enter the name of notes: ")

while(a==0):
    print("Speak out to make notes")
    with sr.Microphone() as source:
        audio=x.listen(source)
        try:
            txt1=x.recognize_google(audio)
            print("You said:",txt1)
            y=int(input("Enter 1 to repeat or 0 to save: "))
            if(y==1):
                continue
            elif(y==0):				
                text_file=open(name+".txt","a")
                text_file.write(txt1+" ")
                text_file.close()
            else:
                print("Invalid input")
                a=0
                continue
            a=int(input("Enter any key to continue or 1 to stop taking notes: "))
            if(a==1):
                break
        except:
            print("Could not understand audio")
    a=0