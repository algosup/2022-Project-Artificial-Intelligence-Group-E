import pyaudio
import wave
import os
import librosa as lr
import numpy as np
import matplotlib.pyplot as plt
import cv2

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 8
WAVE_OUTPUT_FILENAME = "output.wav"

IMAGE_HEIGHT = 128
IMAGE_WIDTH = 500

def recordAudio():
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()



def spectrogram():

    audio_segment, sample_rate = lr.load('./output.wav')

    h1 = audio_segment.shape[0] / IMAGE_WIDTH
    print(h1)
    spec = lr.feature.melspectrogram(audio_segment, n_mels=IMAGE_HEIGHT, hop_length=int(h1))

    image = lr.core.power_to_db(spec)

    image_np = np.asmatrix(image)

    image_np_scaled_temp = (image_np - np.min(image_np))

    image_np_scaled = image_np_scaled_temp / np.max(image_np_scaled_temp)

    return image_np_scaled[:, 0:IMAGE_WIDTH]

while True:
    recordAudio()
    a = spectrogram()
    os.remove("./output.wav")
    plt.imsave("foo.png", a, cmap='gray', format="png")

    img = cv2.imread('foo.png')
    os.remove('foo.png')
    greyImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('imageSource.png', greyImage)
