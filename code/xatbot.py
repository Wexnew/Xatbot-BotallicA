# Salutació
saludar = "Bon dia heavy!!"
print(saludar)

# Preguntar nom
nom = input("Em dic Botallica i seré el teu chatbot heavy. Com et dius? ")
# Separar per espais i quedar-se amb l'última paraula
nom = nom.split(" ")[-1]
print("Perfecte " + nom + ", encantat de conèixer-te" + "!!!")

# Preguntar què vol l'usuari
p0 = "De què voldries parlar? "
p0_resposta = input(p0)

# Començament conversa
c0 = "Perfecte! Vols que et recomani algun àlbum? "
c1 = "Doncs adeu!!"

if "res" in p0_resposta.lower():
    print(c1)
else:
    vol_album = input(c0)

    # minúscules
    resposta_album = vol_album.lower()

    # respostes positives
    respostes_positives = ["sí", "si", "clar", "vale", "yeah", "yes"]

    # Comprovem
    if any(paraula in resposta_album for paraula in respostes_positives):
        print("Et recomano com un àlbum clàssic el *Ride the Lightning* de Metallica ⚡")
        print("I si vols alguna cosa més heavy, escolta *Burn my Eyes* de Machine Head 🤘 Brutal!!")
    else:
        print("Cap problema, heavy! Parlem d’una altra cosa 🤟")
        
# Preguntes
p1_resposta = input("T'agrada la música? ")

#tot a minúscules
resposta_normalitzada = p1_resposta.lower()

#respostes positives
respostes_positives = ["sí", "si", "clar", "vale", "evidentment", "òbviament", "molt", "obviament", "yes", "yeah"]

#alguna d'aquestes paraules està dins de la resposta?
if any(paraula in resposta_normalitzada for paraula in respostes_positives):
    print("Oh yeah! 🤘")
    usuari_agrada_musica = True
else:
    print("Vaja... doncs adeu!")
    usuari_agrada_musica = False
# Extensió p1
if usuari_agrada_musica:
    banda = input("Quin és el teu grup favorit? ")

    if banda in ["Metallica", "Pantera", "Iron Maiden", "Judas Priest", "Megadeth"]:
        print("Oooh!! Molt bona banda. A mi també m'agrada " + banda + " 🤟")
        usuari_heavy = True
    elif banda in ["Bad Bunny", "Rauw Alejandro", "Quevedo"]:
        print("Fora del meu chat, adeu. 😤")
        usuari_heavy = False
    else:
        print("Interessant elecció!")
        usuari_heavy = None

# Preguntar per instruments
p2_resposta = input("Pràctiques algun instrument? ")
if p2_resposta.lower() in ["si", "sí"]:
    print("Que interessant!! Segur que ets molt bo!! 😎")
else:
    print("Oooh, és molt bon hobby, podries provar-ho!!!")

# Àlbum favorit
p3_resposta = input("Quin és el teu àlbum favorit? ")
print("Aquest àlbum m'encanta!!! És molt heavy!!! 🤘")
print("El meu favorit és el Supremacy de Hatebreed!")

# Preguntes usuari, diccionari
input("Vols preguntarme alguna cosa?")
respostes = {
    "qui ets": "Sóc Botallica, el teu chatbot heavy 🤘",
    "què tal": "Sempre a tope amb el metall! 🔥",
    "quin és el teu grup favorit": "Metallica, òbviament 😎",
    "on vius": "Secret secretós",
    "adeu": "Adeu heavy, fins la pròxima! 🤟",
    "noticia": "L'altre día Megadeth va treure una canço nova, Tipping point, podries escoltar-la!!",
    "estils": "hi ha molts estils dins del metal: heavy, thrash, black, death... El meu favorit és el thrash!!",
    "banda": "Et recomano les següents bandes: Hatebreed, Death i Sepultura. Molt bones bandes!!",
    "solo": "El millor solo sense duda és el solo de Tornado of souls, molt bons són també el de Painkiller i el de Cowboys from Hell!!",
    "riff": "Tens que escoltar el riff inicial de Body hammer, És boníssim!!",
    "novetat": "Ha sortit un documental d'Ozyy, podria interessarte heavy!"
}

while True:
    pregunta = input("Tu: ").lower()

    if "adeu" in pregunta:
        print("Botallica: Adeu heavy, fins la pròxima! 🤟")
        break

    resposta = None
    for clau in respostes:
        if clau in pregunta:
            resposta = respostes[clau]
            break

    if resposta:
        print(resposta)
    else:
        print("No t’entenc heavy... pots repetir-ho? 😅")

# Despedida
print("Adeu, " + nom + ", ens veiem un altre dia!!! 🤟")
