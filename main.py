import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# data
studie_uren = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
oefentoetsen = np.array([2, 3, 3, 4, 5]).reshape(-1, 1)
cijfers = np.array([3, 4.5, 5, 6.5, 8])

# Combineer de twee variabelen tot een matrix van inputvariabelen
X = np.hstack((studie_uren, oefentoetsen))

# Model aanmaken en trainen
model = LinearRegression()
model.fit(X ,cijfers)

# Voorspellingen maken
predictions = model.predict(X)

# Coëfficiënt en intercept
print("Intercept:", model.intercept_)
print("Coëfficiënts", model.coef_) #  b1 en b2

# Voorspellingen weergeven
print("Voorspelde cijfers:", predictions)

#  Plotten van voorspellingen en werkelijke gegevens
fig, ax = plt.subplots()
ax.scatter(range(len(cijfers)), cijfers, color='purple', label='Werkelijke cijfers')
ax.plot(range(len(cijfers)), predictions, color='green', label='Voorspelde cijfers')
plt.xlabel('Studenten (volgorde)')
plt.ylabel('Cijfers')
plt.legend()
plt.show()
