# Definir Termes 
p0 = "De què voldries parlar? "
p1 = "T'agrada la música?"
c0 = "Perfecte! Vols que et recomani algun àlbum? "
c1 = "I això? No t'agrada el heavy?"
c2 = "Aaaa, doncs et podría agradar eh, però tu mateix, vols una recomanació d'àlbum per iniciarte?"
respostes_positives = ["sí", "si", "clar", "vale", "yeah", "yes","evidentment", "òbviament", "molt", "obviament"]
respostes_negatives =  ["no", "que va", "eww", "mai", "No"]
respostes_diccionari = {
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


#definim funcions
 #funció per respotes + i -
def es_si(text):
    text = text.lower()
    return any(paraula in text for paraula in respostes_positives)

def es_no(text):
    text = text.lower()
    return any(paraula in text for paraula in respostes_negatives)

 #funció salutació
def salutació():
    saludar = "Bon dia heavy!!"
    print(saludar)
    nom = input("Em dic Botallica i seré el teu xatbot heavy. Com et dius? ")
    nom = nom.split(" ")[-1]
    print(f"Perfecte {nom}, encantat de conèixer-te!!!")
    return nom
    
 #funció gestionar heavy
def gestionar_heavy(p0_resposta):
    if "heavy" in p0_resposta:
        vol_album = input(c0)
          # Si vol una recomanació recomanem i comencem les preguntes, si no pasem directament a la conversa
        if es_si(vol_album):
             print("Et recomano com un àlbum clàssic el *Ride the Lightning* de Metallica ⚡")
             print("I si vols alguna cosa més heavy, escolta *Burn My Eyes* de Machine Head 🤘 Brutal!!")
        else:
            print("Cap problema, heavy! Parlem d’una altra cosa 🤟")

    elif "res" in p0_resposta.lower():
        c1_resposta = input(c1)
        if es_no(c1_resposta):
            c2_resposta = input(c2)
             #si diu que no altre vegada acaba conversa
            if es_si(c2_resposta):
                print("Perfecte! Et recomano per començar el Paranoid de Black Sabbath, dels primers discos heavys.")
            else:
                print("Ok doncs, ens veiem quan siguis heavy")
                exit()
 #funció gestionar_música
def gestionar_música(p1_resposta):
    
#si alguna resposta positiva està dins de la resposta constestem i determinem si l'agrada la musica
    if es_si(p1_resposta):
        print("Oh yeah! 🤘")
        usuari_agrada_musica = True
    else:
        print("No pots ser heavy i que no t'agradi la música mentider 😤")
        print("Però no pasa res, ya parlarem quan t'agradi la música!")
        usuari_agrada_musica = False
        exit()
    return usuari_agrada_musica

 #funció grup favotri
def gestionar_grup_favorit():
    banda = input("Quin és el teu grup favorit? ")

    heavy = ["Metallica", "Pantera", "Iron Maiden", "Judas Priest", "Megadeth"]
    anti_heavy = ["Bad Bunny", "Rauw Alejandro", "Quevedo"]

    if banda in heavy:
        print("Oooh!! Molt bona banda. A mi també m'agrada " + banda + " 🤟")
        return True
    elif banda in anti_heavy:
        print("Fora del meu chat, adeu. 😤")
        exit()
    else:
        print("Interessant elecció!")
        return None
        
 #funció instrument
def gestionar_instrument():
    resposta = input("Pràctiques algun instrument? ").lower()

    if "guitarra" in resposta:
        print("🔥 QUEÉÉÉ!? GUITARRA!? Respect màxim.")
        print("mira això… et tinc un repte, aquest és el tab del riff Master of Puppets 👇")
        print()
        print("e|---------------------------------------------------|")
        print("B|---------------------------------------------------|")
        print("G|---------------------------------------------------|")
        print("D|---------------------------------------------------|")
        print("A|-------2--------3--------4--------3--------2-2-----|")
        print("E|-0---1----0---1----0---1----0---1----0---1---------|")
        print()
        print("fes palm mute i et surtirà brutal! 🤘😎")
        return "guitarra"

    elif resposta in ["si","sí"]:
        print("Que interessant!! Segur que ets molt bo!! 😎")
        
    else:
        print("Oooh, podries provar-ho, és molt bon hobby!!")
        
 #funció album favorit
def album_favorit():
    album = input("Segur que tens un àlbum favorit, quin és? ")
    print("Aquest àlbum m'encanta!!! És molt heavy!!! 🤘")
    print("El meu favorit és el *Supremacy* de Hatebreed!")
    return album
 #funció conversa amb diccionari
def conversa_diccionari(respostes, nom):
    input("Vols preguntarme alguna cosa?")
    while True:
        pregunta = input("Tu: ").lower()
        
        if "adeu" in pregunta:
            break
        
        resposta = None
        for clau in respostes:
            if clau in pregunta:
                resposta = respostes[clau]
                break
        
        if resposta:
            print(resposta)
        else:
            print("No t’entenc heavy... pots repetir-ho d'altre manera? 😅")
            
#funció despedida
def despedida(nom):
    print("Adeu, " + nom + ", ens veiem un altre dia!!! 🤟")
#--------------------------------------------------------------------------------------------------
def heavybot():
#apliquem funcions
    nom = salutació()

# Preguntar si vol parlar l'usuari
    p0_resposta = input(p0)

# Començament conversa i veure si és o no heavy
    gestionar_heavy(p0_resposta)

# Si vol una recomanació recomanem i comencem les preguntes, si no pasem directament a la conversa
    p1_resposta = input(p1)
    usuari_agrada_musica = gestionar_música(p1_resposta)

#si l'agrada, li preguntem quina banda
    if usuari_agrada_musica:
        usuari_heavy = gestionar_grup_favorit()
    
#seguim conversació i preguntem per instruments
    instrument = gestionar_instrument()

#preguntemlbum favorit
    album = album_favorit()

# Preguntes usuari, fem servir un diccionari
    conversa_diccionari(respostes_diccionari, nom)
    
# Despedida
    despedida(nom)



if __name__ == "__main__":
    heavybot()
