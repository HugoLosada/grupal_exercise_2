import random
import matplotlib.pyplot as plt

class ContagionSimulation:
    def __init__(self, population_size, initial_infected_percentage, contagion_probability, recovery_rate, interactions_per_day, simulation_days):
        self.population_size = population_size
        self.infected_percentage = initial_infected_percentage / 100.0
        self.contagion_probability = contagion_probability / 100.0
        self.recovery_rate = recovery_rate / 100.0
        self.interactions_per_day = interactions_per_day
        self.simulation_days = simulation_days

        self.susceptible = int(self.population_size * (1 - self.infected_percentage))
        self.infected = int(self.population_size * self.infected_percentage)
        self.recovered = 0

    def simulate_spread(self):
        susceptible_list = [self.susceptible]
        infected_list = [self.infected]
        recovered_list = [self.recovered]

        for day in range(1, self.simulation_days + 1):
            new_infected = 0

            for _ in range(self.interactions_per_day):
                contacts = random.randint(0, self.susceptible)
                new_infected += int(contacts * self.contagion_probability)

            self.susceptible -= new_infected
            self.infected += new_infected
            self.recovered += int(self.infected * self.recovery_rate)

            susceptible_list.append(self.susceptible)
            infected_list.append(self.infected)
            recovered_list.append(self.recovered)

            print(f"Day {day}: Susceptible={self.susceptible}, Infected={self.infected}, Recovered={self.recovered}")

        self.plot_results(susceptible_list, infected_list, recovered_list)

    def plot_results(self, susceptible_list, infected_list, recovered_list):
        days = list(range(self.simulation_days + 1))

        plt.plot(days, susceptible_list, label='Susceptible')
        plt.plot(days, infected_list, label='Infected')
        plt.plot(days, recovered_list, label='Recovered')
        plt.xlabel('Days')
        plt.ylabel('Population')
        plt.title('Contagion Spread Simulation')
        plt.legend()
        plt.show()

# Entrada del usuario para seleccionar el tamaño de la población
population_size = int(input("Ingrese el tamaño de la población: "))

# Entrada del usuario para seleccionar el tipo de virus (por probabilidad de contagio y tasa de recuperación)
virus_choice = int(input("Seleccione el tipo de virus (1, 2, o 3): "))
if virus_choice == 1:
    contagion_probability = 15
    recovery_rate = 10
elif virus_choice == 2:
    contagion_probability = 20
    recovery_rate = 15
elif virus_choice == 3:
    contagion_probability = 25
    recovery_rate = 20
else:
    print("Opción de virus no válida. Se utilizará el virus predeterminado con probabilidad de contagio del 15% y tasa de recuperación del 10%.")
    contagion_probability = 15
    recovery_rate = 10

# Crear una instancia de la simulación con los parámetros seleccionados por el usuario
simulation = ContagionSimulation(
    population_size=population_size,
    initial_infected_percentage=1,
    contagion_probability=contagion_probability,
    recovery_rate=recovery_rate,
    interactions_per_day=10,
    simulation_days=30
)

# Ejecutar la simulación
simulation.simulate_spread()

