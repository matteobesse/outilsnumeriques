import numpy as np
import matplotlib.pyplot as plt

# Définir l'intervalle de -10 à 10 avec 100 points
x = np.linspace(-10, 10, 1000)
a = x
b = x ** 2
c = x ** 3
d = 1/x
e = 1/(x**2)
f= 1/(x**3)

# Tracer la courbe des fonctions
plt.plot(x, a, label="f(x) = x") #fonction linéaire
plt.plot(x, b, label="f(x) = x²")
plt.plot(x, c, label="f(x) = x³")
plt.plot(x, d, label="f(x) = 1/x")
plt.plot(x, e, label="f(x) = 1/x²")
plt.plot(x, f, label="f(x) = 1/x³")

# Ajouter un titre et des labels
plt.title("Représentation des la fonction f(x)")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.xlim(-2,2)
plt.ylim(-1,3)

# Ajouter une grille et une légende
plt.grid(True)
plt.legend()

# Afficher la figure
plt.show()