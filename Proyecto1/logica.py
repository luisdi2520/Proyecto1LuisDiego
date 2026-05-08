def load_Personajes(filepath="Personajes.txt"):
    personajes = []

    with open(filepath, "r", encoding="utf-8") as file:
        next(file)

        for line in file:
            line = line.strip()
            if line == "":
                continue

            parts = line.split(",")

            personaje = {
                "nombre": parts[0],
                "hp":     int(parts[1]),
                "max_hp": int(parts[1]),
                "DEF":    int(parts[2]),
                "ATK":    int(parts[3]),
                "KO":     False,
                "imagen": parts[4]
            }
            personajes.append(personaje)

    return personajes

def calDaño(ataque,defensa):
   atk = ataque["ATK"]
   defen = defensa["DEF"]
   return dañoRecibido(atk,defen)

def dañoRecibido(atk, defen):
    if defen <= 0 and atk <= 0:
        return 1
    if defen <= 0:
        return atk
    elif atk <= 1:
        return 1
    else:
        return dañoRecibido(atk-1, defen -1)

#personajes hollows
import random
def Crearhollows(personajes):
    mezcla = personajes.copy()
    random.shuffle(mezcla)
    hollows = [
        {"nombre": "Hollow de Radiador Springs", "personajes": mezcla[0:3], "vencido": False},
        {"nombre": "Hollow de Pride Rock", "personajes": mezcla[3:6], "vencido": False},
        {"nombre": "Hollow de Monstropolis", "personajes": mezcla[6:9], "vencido": False},
        {"nombre": "Hollow de Neverland", "personajes": mezcla[9:12], "vencido": False},
        {"nombre": "Hollow de Arandelle", "personajes": mezcla[12:15], "vencido": False},
    ]
    return hollows
#logica de los turnos de batalla
import random
def turnos(turno, p_jugador, p_hollow, log):
    if p_jugador is None or p_hollow is None:
        return log
    if p_jugador["KO"] or p_hollow["KO"]:
        return log
    if turno % 2 == 0:
        daño = calDaño(p_jugador, p_hollow)
        p_hollow["hp"] -= daño
        log.append(f"{p_jugador['nombre']} atacó a {p_hollow['nombre']} por {daño} de daño")
        if p_hollow["hp"] <= 0:
            p_hollow["hp"] = 0
            p_hollow["KO"] = True
    else:
        daño = calDaño(p_hollow, p_jugador)
        p_jugador["hp"] -= daño
        log.append(f"{p_hollow['nombre']} ataco a {p_jugador['nombre']} por {daño} de daño")
        if p_jugador["hp"] <= 0:
            p_jugador["hp"] = 0
            p_jugador["KO"] = True
    return turnos(turno + 1, p_jugador, p_hollow, log)

def elecc_pjHollow(hollow):
    dispo = [p for p in hollow["personajes"]if not p["KO"]]
    if dispo:
        return random.choice(dispo)
    else:
        return None

def guardarPuntaje(nombre, puntaje, filepath="puntaje.txt"):
    puntaje_act = 0

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            linea = file.read().strip()
            if linea !="":
                puntaje_act = int(linea.split(":")[1].strip())
    except:
        pass

    if puntaje > puntaje_act:
        with open (filepath, "w", encoding="utf-8") as file:
            file.write(f"{nombre}: {puntaje}\n")
    

     
    