def contactos(infectados):
    contacto = infectados*random.randint(0,5)
    return contacto

def contagio(contactos):
    contagiados = contactos-random.randint(contactos)
    return contagiados

def simulación():
    while poblacion["día"]<30:
        contactados = contactos(población["infectados"])
        contagiados = contagio(contactados)
        población["sanos"]-=contagiados
        población["infectados"]+=contagiados
        población["día"]+=1

        print("Infectados en el día",poblacion["día"],":"poblacion["infectados"])
        print("Quedan", poblacion["sanos"],"habitantes sanos.")

        if población["día"]>= 30:
            break

población ={
    "sanos": 999,
    "infrctados": 1,
    "día":0
}

simulación()