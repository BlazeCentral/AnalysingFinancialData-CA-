Sals Shipping Code


weight = 41.5

gcost = 0
gpcost = 125
dcost = 0

#Ground Shipping
if weight <= 2:
  gcost = 20 + 1.5 * weight
elif weight <= 6:
  gcost = 20 + 3 * weight
elif weight <= 10:
  gcost = 20 + 4 * weight
else:
  gcost = 20 + 4.75 * weight

print("Cost via ground shipping: $" + str(gcost) + " (Package Weight: " + str(weight) + "lb)")

# Ground Shipping Premium

print("Cost via ground shipping premium: $" + str(gpcost) + " (Package Weight: " + str(weight) + "lb)")
# Drone Shipping 

if weight <= 2.0:
  dcost = 0 + 4.5 * weight
elif weight <= 6.0:
  dcost = 0 + 9 * weight
elif weight <= 10:
  dcost = 0 + 12 * weight
else:
  dcost = 0 + 14.25 * weight
print("Cost via drone shipping: $" + str(dcost) + " (Package Weight: " + str(weight) + "lb)")




