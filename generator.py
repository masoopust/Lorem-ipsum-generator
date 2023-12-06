import random

Loremtext = ["Accio", "Aquamenti", "Alohomora", "Ascendio", "Avada Kedavra", "Bombarda","Cruciatus", "Descendo", "Erecto", "Expelliarmus","Geminio","Hop", "Imperius", "Lumos", "Obscuro", "Perfendi",
             "Reducto", "Silencio", "Titillando", "Verdillious", "Wingardium Leviosa", "Zapomeň", "Žer slimáky"   ]

numbsent = int(input("How many sentences you want from generator? \n: "))           #number of sentences

text = []
for i in range(numbsent):
    ws = random.randint(3,8)                                                         #words in sentence
    sentence = " ".join(random.sample(Loremtext, ws))                                #sentence = náhodný počet slov 3-8 ze seznamu Loremtext a dá je do stringu
    text.append(sentence.capitalize() + ".")                                         #První písmeno udělá velké, na konec přidá tečku a přídá do seznamu text

finish = " ".join(text)
print(finish)

#BONUS

file_name = "Loremipsum.txt"
with open(file_name, "w") as file:
    file.write(finish)

print(f"Your Lorem ipsum text is also in this file : {file_name}")












