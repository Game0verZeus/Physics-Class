# Writing the code based on the instructions

# Temperature conversion functions
def f_to_c(f_temp):
    return (f_temp - 32) * 5/9

def c_to_f(c_temp):
    return c_temp * (9/5) + 32

# Testing the temperature conversion functions
f100_in_celsius = f_to_c(100)
c0_in_fahrenheit = c_to_f(0)

# Force calculation function
def get_force(mass, acceleration):
    return mass * acceleration

# Energy calculation function
def get_energy(mass, c=3*10**8):
    return mass * c**2

# Work calculation function
def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    return force * distance

# Uncommenting the provided variables
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Testing get_force with train data
train_force = get_force(train_mass, train_acceleration)
print(f"The GE train supplies {train_force} Newtons of force.")

# Testing get_energy with bomb data
bomb_energy = get_energy(bomb_mass)
print(f"A 1kg bomb supplies {bomb_energy} Joules.")

# Testing get_work with train data
train_work = get_work(train_mass, train_acceleration, train_distance)
print(f"The GE train does {train_work} Joules of work over {train_distance} meters.")

