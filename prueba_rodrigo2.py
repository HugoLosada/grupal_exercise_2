import random

def contactos(infectados):
    contacto = infectados * random.randint(0, 5)
    return contacto

def contagio(contactos):
    contagiados = random.randint(0, contactos)
    return contagiados

def recuperaciones(infectados):
    recuperados = infectados - random.randint(0, infectados)
    return recuperados

def simulacion(ambiente):
    while ambiente["día"] < 30 and ambiente["sanos"]>0 and ambiente["infectados"]<1000:
        contactados = contactos(ambiente["infectados"])
        contagiados = contagio(contactados)
        ambiente["sanos"] -= contagiados
        ambiente["infectados"] += contagiados
        ambiente["día"] += 1

        if ambiente["día"]>7:
            recuperados = recuperaciones(ambiente["infectados"])
            return recuperados
        
        ambiente["infectados"]-= recuperados
        ambiente["sanos"]+= recuperados

        print("Infectados en el día", ambiente["día"], ":", ambiente["infectados"])
        print("Quedan", ambiente["sanos"], "habitantes sanos.")

        if ambiente["día"] >= 30:
            print("Simulación completada.")
            break

        elif ambiente["sanos"] == 0:
            print("Todos los habitantes han sido infectados.")
            break

        elif ambiente["infectados"] == 1000:
            print("Todos los habitantes han sido infectados.")
            break

poblacion = {
    "sanos": 999,
    "infectados": 1,
    "día": 0
}

simulacion(poblacion)