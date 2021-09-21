
import scipy.io.wavfile as waves
import pyaudio
import wave
from os import remove
import señal
import time
import random

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 41100
RECORD_SECONDS = 1.6
p_rec = pyaudio.PyAudio()

Muestras = 33
piedras = []
papeles = []
tijeras = []

p_p_t = [ "piedra", "papel", "tijera"]

for i in range(Muestras):
    d = i+1
    filename = 'grabaciones/'+p_p_t[0]+str(d)+'.wav'
    Fs, data = waves.read(filename) 
    data = abs(señal.fft(data))
    data = data[0:65536//2] 
    e = señal.umbrales(data)
    piedras.append(e)
    
    filename = 'grabaciones/'+p_p_t[1]+str(d)+'.wav'
    Fs, data = waves.read(filename) 
    data = abs(señal.fft(data))
    data = data[0:65536//2] 
    e = señal.umbrales(data)
    papeles.append(e)
    
    filename = 'grabaciones/'+p_p_t[2]+str(d)+'.wav'
    Fs, data = waves.read(filename) 
    data = abs(señal.fft(data))
    data = data[0:65536//2] 
    e = señal.umbrales(data)
    tijeras.append(e)


print("BIENVENIDO AL JUEGO DE PIEDRA PAPEL O TIJERA")
print("Acontinuacion diga su opcion")
time.sleep(2)

while True:
    elecc = random.randint(0,2)
    stream = p_rec.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    print("---- Iniciando grabacion ----")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
            
    print("---- Grabacion finalizada ----")

    stream.stop_stream()
    stream.close()

    wf = wave.open("grabacion.wav", 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p_rec.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    Fs, data = waves.read("grabacion.wav")
    remove("grabacion.wav")
    data = abs(señal.fft(data))
    data = data[0:65536//2] 
    vec = señal.umbrales(data)

    contpi = 0
    contpa = 0
    contt = 0
    cpi = 0
    cpa = 0
    cpt = 0
    for i in range(Muestras):
        rock = piedras[i]
        paper = papeles[i]
        tijer = tijeras[i]
        for n in range(16):
            errorp = abs((rock[n]-vec[n])/rock[n])
            errorpa = abs((paper[n]-vec[n])/paper[n])
            errort = abs((tijer[n]-vec[n])/tijer[n])
            if errorp < errorpa :
                if errorp < errort:
                    contpi = contpi + 1
                else :
                    contt = contt + 1
            elif errorpa < errort:
                contpa = contpa + 1
            else:
                contt = contt + 1

        if contpi > contpa :
            if contpi > contt:
                cpi = cpi + 1
            else :
                cpt = cpt + 1
        elif contpa > contt:
            cpa = cpa + 1
        else:
            cpt = cpt + 1

    
    #print("Minimos errores en piedra : "+str(cpi))        
    #print("Minimos errores en papel : "+str(cpa))
    #print("Minimos errores en tijera : "+str(cpt))
    
    elegido = 0
    if cpi > cpa :
        if cpi > cpt:
            print("USTED ELIGIO EL VALOR DE : "+p_p_t[0]+" ----")
            elegido = 0
        else :
            print("USTED ELIGIO EL VALOR DE "+p_p_t[2]+" ----")
            elegido = 2
    elif cpa > cpt:
        print("USTED ELIGIO EL VALOR DE "+p_p_t[1]+" ----")
        elegido = 1
    else:
        print("USTED ELIGIO EL VALOR DE "+p_p_t[2]+" ----")
        elegido = 2

    print("LA MAQUINA ELIGIO EL VALOR DE "+p_p_t[elecc])

    if elegido == 0:
        if elecc == 1:
            print("HAS PERDIDO")
        elif elecc == 2:
            print("HAS GANADO")
        else :
            print("HAS EMPATADO")
    elif elegido == 1:
        if elecc == 2:
            print("HAS PERDIDO")
        elif elecc == 0:
            print("HAS GANADO")
        else :
            print("HAS EMPATADO")
    elif elegido == 2:
        if elecc == 0:
            print("HAS PERDIDO")
        elif elecc == 1:
            print("HAS GANADO")
        else :
            print("HAS EMPATADO")
    
    print("Desea continuar? y / n")
    seleccion = input()
    if seleccion == "n":
        break
p_rec.terminate()