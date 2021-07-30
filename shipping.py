# this project checks shipping cost per item against ground, premium and drone shipping
weight = 41.5

# Ground Shipping plus flat charge of 20
if weight <= 2:
  cost_ground = weight * 1.50 + 20
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3 + 20
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20

# variables for total cost
cost = cost_ground
print(cost)

# Premium shipping cost is a flat charge regardless of weight
cost_premium_shipping = 125
print(cost_premium_shipping)

# Drone Shippingn no flat charge
if weight <= 2:
  cost_drone = weight * 4.50
elif weight > 2 and weight <= 6:
  cost_drone = weight * 9
elif weight > 6 and weight <= 10:
  cost_drone = weight * 12
else:
  cost_drone = 14.25

# assigned the drone variable the cost of drone
drone = cost_drone
print(drone)