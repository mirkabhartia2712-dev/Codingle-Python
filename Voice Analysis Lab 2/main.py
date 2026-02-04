import threading

import sys





try:

    import pyaudio

    import numpy as np

    import matplotlib.pyplot as plt

    import speech_recognition as sr

    from speech_recognition import AudioData

except ImportError as e:

    print(f"❌Missing library: {e.name}")

    print ("\n???? Install commands:")

    print ("  Windows: pip install SpeechRecognition pyaudio numpy matplotlib")

    print("  macOs:   brew install portaudio && pip install SpeechRecognition pyaudio numpy matplotlib")

    sys.exit(1)


stop_event = threading.Event()


def wait_for_enter():

    input()

    stop_event.clear() 

    p = pyaudio.PyAudio()

    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)

    frames = []


