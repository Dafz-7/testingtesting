avogadro = 6.022e23
def num_atoms(amount, atomic_weight=196.97):
    atom = (amount/atomic_weight) * avogadro
    return atom

print(num_atoms(10))
print(num_atoms(10, 12.001))
print(num_atoms(10, 1.008))