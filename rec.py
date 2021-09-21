import pyaudio
import wave
import struct 

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 41100
RECORD_SECONDS = 1.6


p = pyaudio.PyAudio()
k = 19
while k < 34:
    for i in range(3):
        WAVE_OUTPUT_FILENAME = ""
        if i == 0:
            WAVE_OUTPUT_FILENAME = "piedra"+str(k)+".wav"
        elif i == 1:
            WAVE_OUTPUT_FILENAME = "papel"+str(k)+".wav"
        else:
            WAVE_OUTPUT_FILENAME = "tijera"+str(k)+".wav"

        stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

        print("--- grabando ---"+WAVE_OUTPUT_FILENAME)

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("--- grabacion finalizada ---")

        stream.stop_stream()
        stream.close()
        

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

    k = k + 1

p.terminate()