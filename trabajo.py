import numpy as np
import matplotlib.pyplot as plt

# Función para simular la propagación del virus (modelo SIR)
def simular_contagio(poblacion, infectados_iniciales, tasa_contagio, tasa_recuperacion, tasa_mortalidad, dias):
    susceptibles = poblacion - infectados_iniciales
    infectados = infectados_iniciales
    recuperados = 0
    muertos = 0

    s_lista = [susceptibles]
    i_lista = [infectados]
    r_lista = [recuperados]
    m_lista = [muertos]

    # Iterar a lo largo de los días de la simulación
    for dia in range(dias):
        # Calcular nuevos infectados, recuperados y muertos
        nuevos_infectados = (tasa_contagio * infectados * susceptibles) / poblacion
        nuevos_recuperados = tasa_recuperacion * infectados
        nuevos_muertos = tasa_mortalidad * infectados

        # Actualizar las cantidades de susceptibles, infectados, recuperados y muertos
        susceptibles -= nuevos_infectados
        infectados += nuevos_infectados - nuevos_recuperados - nuevos_muertos
        recuperados += nuevos_recuperados
        muertos += nuevos_muertos

        # Guardar los datos en listas para su posterior visualización
        s_lista.append(susceptibles)
        i_lista.append(infectados)
        r_lista.append(recuperados)
        m_lista.append(muertos)

    # Devolver las listas de datos
    return s_lista, i_lista, r_lista, m_lista

# Función para graficar los resultados de la simulación
def graficar(poblacion, infectados_iniciales, tasa_contagio, tasa_recuperacion, tasa_mortalidad, dias):
    # Obtener las listas de datos a partir de la simulación
    s, i, r, m = simular_contagio(poblacion, infectados_iniciales, tasa_contagio, tasa_recuperacion, tasa_mortalidad, dias)

    # Crear una lista de días para el eje x
    dias_lista = np.arange(0, dias+1)

    # Graficar las curvas de susceptibles, infectados, recuperados y muertos
    plt.plot(dias_lista, s, label='Susceptibles')
    plt.plot(dias_lista, i, label='Infectados')
    plt.plot(dias_lista, r, label='Recuperados')
    plt.plot(dias_lista, m, label='Muertos')

    # Etiquetas y título del gráfico
    plt.xlabel('Días')
    plt.ylabel('Población')
    plt.title('Simulación de Contagio de Virus (Modelo SIR)')

    # Mostrar la leyenda
    plt.legend()

    # Mostrar el gráfico
    plt.show()

# Pedir input al usuario con validación
while True:
    try:
        poblacion = int(input("Ingrese el tamaño de la población (debe ser un número entero no negativo): "))
        infectados_iniciales = int(input("Ingrese el número inicial de infectados (debe ser un número entero no negativo): "))
        tasa_contagio = float(input("Ingrese la tasa de contagio (entre 0 y 1): "))
        tasa_recuperacion = float(input("Ingrese la tasa de recuperación (entre 0 y 1): "))
        tasa_mortalidad = float(input("Ingrese la tasa de mortalidad (entre 0 y 1): "))
        dias = int(input("Ingrese la duración de la simulación en días: "))

        if not (0 <= tasa_contagio <= 1) or not (0 <= tasa_recuperacion <= 1) or not (0 <= tasa_mortalidad <= 1):
            raise ValueError("Las tasas deben estar entre 0 y 1.")

        if poblacion < 0 or infectados_iniciales < 0:
            raise ValueError("La población y el número inicial de infectados deben ser no negativos.")

        break
    except ValueError as e:
        print(f"Error: {e}\nPor favor, ingrese valores válidos.")

graficar(poblacion, infectados_iniciales, tasa_contagio, tasa_recuperacion, tasa_mortalidad, dias)





