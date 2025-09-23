def calc_weight_on_planet(weight, gravity=23.1):
    weightnew = (weight/9.8) * gravity
    return weightnew

print(calc_weight_on_planet(120, 9.8))
print(calc_weight_on_planet(120))
print(calc_weight_on_planet(120, 23.1))