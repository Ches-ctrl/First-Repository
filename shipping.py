weight = 8.4
#Ground Shipping
if weight <= 2:
  cost_ground = 1.5 * weight + 20
elif weight <= 6:
  cost_ground = 3.0 * weight + 20
elif weight <= 10:
  cost_ground = 4.0 * weight + 20
else:
  cost_ground = 4.75 * weight + 20

print("For a %slb weight, standard ground shipping is $%s" % (weight, cost_ground))

#Premium Ground Shipping
premium_ground = 125.00

print("For a %slb weight, premium ground shipping is $%s" % (weight, premium_ground))

weight = 1.5

#Drone Shipping
if weight <= 2:
  cost_drone = 4.5 * weight
elif weight <= 6:
  cost_drone = 9.0 * weight
elif weight <= 10:
  cost_drone = 12.0 * weight
else:
  cost_drone = 14.25 * weight

print("For a %slb weight, drone shipping is $%s" % (weight, cost_drone))

weight = 4.8
print ("For a %slb weight, standard ground shipping is $%s" % (weight, cost_ground))
print ("For a %slb weight, premium ground shipping is $%s" % (weight, premium_ground))
print ("For a %slb weight, drone shipping is $%s" % (weight, cost_drone))
