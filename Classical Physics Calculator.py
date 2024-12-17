# Setup
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1
c = 3*10**8

# Write your code below: 

# Farenheit to Celsius
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp
# Example
f100_in_celsius = f_to_c(100)
print("For example, 100 F in Celsius is: " + str(round(f100_in_celsius,2 )) + " Degrees")

def c_to_f(c_temp):
  f_temp = (c_temp) * (9/5) + 32
  return f_temp

# Example
c0_in_farenheit = c_to_f(0)
print("For example, 0 C in Farenheit is: " + str(round(c0_in_farenheit,2)) + " Degrees")

# Force Calculation
def get_force(mass, acceleration):
  force = mass * acceleration
  return force

# Test force
train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force")


# Energy
def get_energy(mass, c)
  energy = mass * c
  return energy
  

