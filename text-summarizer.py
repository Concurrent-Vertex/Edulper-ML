from transformers import pipeline
summarization = pipeline("summarization")
c=input("Enter 0 to take text from file and 1 to input directly ")
if(c=="0"):
    name=input("Enter name of notes file: ")
    n=name+".txt"
    with open(n,'r') as file:
        original_text = file.read()
elif(c=="1"):
    original_text=input("Enter the text to summarize: ")
summary_text = summarization(original_text)[0]['summary_text']
print("Summary:", summary_text)