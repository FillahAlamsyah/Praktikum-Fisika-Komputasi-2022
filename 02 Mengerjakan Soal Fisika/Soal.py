# Soal 1
'''Rumus Fokus Lensa
    1/f = (n-1)[1/R1 + 1/R2]
'''
n  = 1.5    #Indeks Bias
R1 = 20     #Jari-jari kelengkungan, satuan cm
R2 = 18

F = (n-1)*((1/R1)+(1/R2))
F = 1/F

print("-"*40)
print("Jarak Fokus Lensa = ",F)


#Soal 2
import numpy as np
import matplotlib.pyplot as plt
''' Rumus Jarak Maksimum Gerak Parabola
    x = ( (v0^2)*sin(2*alpha) ) / 2g
    Rumus Ketinggian 
'''
X0 = 0
Y0 = 0
V0 = 10     # m/s
alpha = 45  #derajat
g = 9.8     # m/s^2 (Percepatan Gravitasi)
t = np.arange(0,10,0.1)

xt , yt, vyt = [] , [] , []

while t.any() < t.max():
    #Arah Sumbu X
    vx = V0*np.cos(alpha)
    x = X0 + vx*t
    #Arah Sumbu Y
    vy = V0*np.sin(alpha) - g*t
    y = Y0 + vy*t - (0.5)*g*t**2
    xt.append(x)
    yt.append(y)
    vyt.append(vy)

Xmaks = (V0**2*np.sin(2*alpha))/(2*g)

print("-"*40)
print("Posisi x = ",x)
print("Posisi y = ",y)
print("Kecepatan pada Sumbu X = ",vx)
print("Kecepatan pada Sumbu Y = ",vy)
print("Jarak horizontal = ",Xmaks)
print(x,y)
print(vyt)

plt.plot(xt,yt,'o',t,yt,'-')
plt.grid(True)
plt.title(' Grafik Gerak Jatuh dengan Gesekan Udara')
plt.xlabel('Waktu,t (s)'); plt.ylabel('Kecepatan, v (m/s)')
plt.legend(('Euler','Exact'),loc=0)
plt.show()

