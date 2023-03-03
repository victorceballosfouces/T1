
import sys

print(sys.version)


import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from numpy.fft import fft            # Importem la funció fft

## EXERCICI 1

# Exemple 1 sinusoide:
T= 2.5                               # Durada de T segons
fm=8000                              # Freqüència de mostratge en Hz
fx=4000                              # Freqüència de la sinusoide
A=4                                  # Amplitud de la sinusoide
pi=np.pi                             # Valor del número pi
L = int(fm * T)                      # Nombre de mostres del senyal digital
Tm=1/fm                              # Període de mostratge
t=Tm*np.arange(L)                    # Vector amb els valors de la variable temporal, de 0 a T
x = A * np.cos(2 * pi * fx * t)      # Senyal sinusoidal
sf.write('so_exemple4k.wav', x, fm)  # Escriptura del senyal a un fitxer en format wav

Tx=1/fx                                   # Període del senyal
Ls=int(fm*5*Tx)                           # Nombre de mostres corresponents a 5 períodes de la sinusoide

plt.figure(0)                             # Nova figura
plt.plot(t[0:Ls], x[0:Ls])                # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide')   # Títol del gràfic
plt.show()                                # Visualització de l'objecte gràfic.

# Ejemple 2 sinusoide:
T= 2.5                               # Durada de T segons
fm=8000                              # Freqüència de mostratge en Hz
fx=1000                              # Freqüència de la sinusoide
A=4                                  # Amplitud de la sinusoide
pi=np.pi                             # Valor del número pi
L = int(fm * T)                      # Nombre de mostres del senyal digital
Tm=1/fm                              # Període de mostratge
t=Tm*np.arange(L)                    # Vector amb els valors de la variable temporal, de 0 a T
x = A * np.cos(2 * pi * fx * t)      # Senyal sinusoidal
sf.write('so_exemple1k.wav', x, fm)  # Escriptura del senyal a un fitxer en format wav

Tx=1/fx                                   # Període del senyal
Ls=int(fm*5*Tx)                           # Nombre de mostres corresponents a 5 períodes de la sinusoide

plt.figure(0)                             # Nova figura
plt.plot(t[0:Ls], x[0:Ls])                # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide')   # Títol del gràfic
plt.show()                                # Visualització de l'objecte gràfic.

# Ejemple 3 sinusoide:
T= 2.5                               # Durada de T segons
fm=8000                              # Freqüència de mostratge en Hz
fx=220                               # Freqüència de la sinusoide
A=4                                  # Amplitud de la sinusoide
pi=np.pi                             # Valor del número pi
L = int(fm * T)                      # Nombre de mostres del senyal digital
Tm=1/fm                              # Període de mostratge
t=Tm*np.arange(L)                    # Vector amb els valors de la variable temporal, de 0 a T
x = A * np.cos(2 * pi * fx * t)      # Senyal sinusoidal
sf.write('so_exemple220.wav', x, fm) # Escriptura del senyal a un fitxer en format wav

Tx=1/fx                                   # Període del senyal
Ls=int(fm*5*Tx)                           # Nombre de mostres corresponents a 5 períodes de la sinusoide

plt.figure(0)                             # Nova figura
plt.plot(t[0:Ls], x[0:Ls])                # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide')   # Títol del gràfic
plt.show()                                # Visualització de l'objecte gràfic.




## EXERCICI 2

x_r, fm = sf.read('so_exemple4k.wav')     # Llegim l'exemple prèviament creat

fx = 4000                                 # Freqüència de la sinusoide
Tx=1/fx                                   # Període del senyal
Ls=int(fm*5*Tx)                           # Nombre de mostres corresponents a 5 períodes de la sinusoide

plt.figure(0)                             # Nova figura
plt.plot(t[0:Ls], x_r[0:Ls])              # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide')   # Títol del gràfic
plt.show()                                # Visualització de l'objecte gràfic.

#Transformada

N=5000                                # Dimensió de la transformada discreta
X=fft(x_r[0 : Ls], N)                 # Càlcul de la transformada de 5 períodes de la sinusoide

k=np.arange(N)                        # Vector amb els valors 0≤  k<N

plt.figure(1)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(k,abs(X))                    # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(X)))    # Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()                            # Per mostrar els grafics




## EXERCICI 3

T= 2.5                               # Durada de T segons
fm=8000                              # Freqüència de mostratge en Hz
fx=440                               # Freqüència de la sinusoide
A=4                                  # Amplitud de la sinusoide
pi=np.pi                             # Valor del número pi
L = int(fm * T)                      # Nombre de mostres del senyal digital
Tm=1/fm                              # Període de mostratge
t=Tm*np.arange(L)                    # Vector amb els valors de la variable temporal, de 0 a T
x = A * np.cos(2 * pi * fx * t)      # Senyal sinusoidal
sf.write('so_exemple440.wav', x, fm) # Escriptura del senyal a un fitxer en format wav

Tx=1/fx                                   # Període del senyal
Ls=int(fm*5*Tx)                           # Nombre de mostres corresponents a 5 períodes de la sinusoide

plt.figure(0)                             # Nova figura
plt.plot(t[0:Ls], x[0:Ls])                # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide')   # Títol del gràfic
plt.show()                                # Visualització de l'objecte gràfic. 

N=5000                                    # Dimensió de la transformada discreta
X=fft(x[0:L], N)                          # Càlcul de la transformada de 5 períodes de la sinusoide
k=np.arange(N)                            # Vector amb els valors 0≤  k<
Y = 20*np.log10(np.abs(X)/max(np.abs(X)))
fk = k[0:N//2+1]*fm/N

plt.figure(1)                              # Nova figura
plt.subplot(211)                           # Espai per representar el mòdul
plt.plot(fk,Y[0:N//2+1])                   # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={L} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('dB')                           # Etiqueta de mòdul
plt.subplot(212)                           # Espai per representar la fase
plt.plot(fk,np.unwrap(np.angle(X[0:N//2+1])))   # Representació de la fase de la transformad, desenroscada
plt.xlabel('Hz')                                # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')                       # Etiqueta de la fase en Latex
plt.show()                                      # Per mostrar els grafics



## EXERCICI 4

x_p, fm = sf.read('luzbel44.wav')         # Llegim l'exemple prèviament creat
T = 0.025                                 # Periode
Ls=int(fm*T)                              # Nombre de mostres corresponents a T = 0.025 període

plt.figure(0)                             # Nova figura
plt.plot(t[0:Ls], x_p[0:Ls])              # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('luzbel44')                     # Títol del gràfic
plt.show()                                # Visualització de l'objecte gràfic.

#Transformada

N=5000                                    # Dimensió de la transformada discreta
X=fft(x_p[0 : Ls], N)                     # Càlcul de la transformada de 5 períodes de la sinusoide
k=np.arange(N)
Y2 = 20*np.log10(np.abs(X)/max(np.abs(X)))
fk = k[0:N//2+1]*fm/N

plt.figure(1)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(fk,Y2[0:N//2+1])             # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('dB')                      # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(fk,np.unwrap(np.angle(X[0:N//2+1])))    # Representació de la fase de la transformad, desenroscada
plt.xlabel('Hz')                      # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show() 