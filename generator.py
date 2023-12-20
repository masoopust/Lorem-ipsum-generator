import random

Loremtext = ["Accio", "Aquamenti", "Alohomora", "Ascendio", "Avada Kedavra", "Bombarda","Cruciatus", "Descendo", "Erecto", "Expelliarmus","Geminio","Hop", "Imperius", "Lumos", "Obscuro", "Perfendi",
             "Reducto", "Silencio", "Titillando", "Verdillious", "Wingardium Leviosa", "Zapomeň", "Žer slimáky"   ]

numbsent = int(input("How many sentences you want from generator? \n: "))    #number of sentences
wsmin = int(input("What is the minimum of words you want in one sentence? \n: "))   #Minimum words
wsmax = int(input("What is the maximum of words you want in one sentence? \n: "))   #Maximum words
text = []
for i in range(numbsent):
    ws = random.randint(wsmin,wsmax)                                                         #words in sentence
    sentence = " ".join(random.sample(Loremtext, ws))                                #sentence = náhodný počet slov min-max ze seznamu Loremtext a dá je do stringu
    text.append(sentence.capitalize() + ".")                                         #První písmeno udělá velké, na konec přidá tečku a přídá do seznamu text

finish = " ".join(text)
print(finish)

#BONUS

file_name = input("This will be the name of your file : ")
with open(file_name, "w", encoding= "utf-8") as file:
    file.write(finish)

print(f"Your Lorem ipsum text is also in this file : {file_name}")












