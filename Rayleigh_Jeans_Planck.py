import matplotlib.pyplot as plt

k_B = 1.38 * 10**(-23)
h = 6.626 * 10**(-34)
pi = 3.14
e = 2.718
c = 2.99 * 10**8
T = 5525
maximum = 10*k_B*T/h

nu = 0.01*k_B*T/h
X = []
Y1 = []
Y2 = []

while nu < maximum:
    X.append(nu)
    Y1.append(8 * pi * nu**2 * k_B * T / c**3)
    if c**3 * (pow(e, h * nu / (k_B * T)) - 1) != 0:
        Y2.append(8 * pi * h * nu**3 / (c**3 * (e**(h * nu / (k_B * T)) - 1)))
    else:
        Y2.append(0)
    nu += 0.01*k_B*T/h

fig = plt.figure()
sp1 = fig.add_subplot(1, 1, 1)

rj, = sp1.plot(X, Y1, color="red", label="Theoretical")
planck, = sp1.plot(X, Y2, color="green", label="Observed")
sp1.set_title('Discrepancy in Theory (5525 K)')
sp1.set_xlabel('Frequency')
sp1.set_ylabel('Energy Density')
plt.ylim([0, 1.6 * 10**(-15)])
sp1.legend(handles=[rj, planck])

plt.show()
