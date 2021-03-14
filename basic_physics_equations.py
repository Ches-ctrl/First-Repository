train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

#Temperature Functions
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

f100_in_celsius = f_to_c(100)
print(f100_in_celsius)
print(f_to_c(30))

def c_to_f(c_temp):
  f_temp = c_temp * 9/5 + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)
print(c_to_f(30))

#Force Functions
def get_force(mass, acceleration):
  force = mass * acceleration
  return force

train_force = get_force(train_mass, train_acceleration)
print(train_force)
print("The GE train supplies %s Newtons of force." % train_force)

#Energy Function
c = 3*10**8
def get_energy(mass, c):
  energy = mass * c
  return energy

bomb_energy = get_energy(bomb_mass, c)
print(bomb_energy)
print("A 1kg bomb supplies %s Joules" % bomb_energy)

#Work Function
def get_work(mass, acceleration, distance):
  work = get_force(mass, acceleration) * distance
  return work

train_work = get_work(train_mass, train_acceleration, train_distance)
print(train_work)
print("The GE train does %s Joules of work over %s meters" % (train_work, train_distance))

