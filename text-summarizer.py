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

'''
Tropical rainforests are rainforests that occur in areas of tropical rainforest climate in which there is no dry season – all months have an average precipitation of at least 60 mm – and may also be referred to as lowland equatorial evergreen rainforest. True rainforests are typically found between 10 degrees north and south of the equator (see map); they are a sub-set of the tropical forest biome that occurs roughly within the 28-degree latitudes (in the equatorial zone between the Tropic of Cancer and Tropic of Capricorn). Within the World Wildlife Fund's biome classification, tropical rainforests are a type of tropical moist broadleaf forest (or tropical wet forest) that also includes the more extensive seasonal tropical forests.
'''