import threading

import sys


import time



try:

    import pyaudio

    import numpy as np

    import matplotlib.pyplot as plt

    import wave

    import speech_recognition as sr

    from speech_recognition import AudioData


except ImportError as e:


    print (f"🤠❌🪅 Missing library: {e.name}")

    print ("🤠🪅\n???? Install commands:")

    print ("🪅🤠 Windows: pip install SpeechRecognition pyaudio numpy matplotlib")

    print (" 🪅🤠 macOS: brew install portaudio && pip install SpeechRecognition pyaudio numpy matplotlib")

    sys.exit(1)


stop_event = threading.Event()



def wait_for_enter():

    input ("🪅🤠 \n???? Press Enter to stop recording...\n")

    stop_event.set()



def spinner():

    chars = '|/-\\'

    i = 0

    while not stop_event.is_set():

        sys.stdout.write(f'\r???? Recording...🪅🤠{chars[i%4]}')

        sys.stdout.flush()

        i+= 1

        time.sleep(0.1)


    print ("🪅🤠 \r ✔️ Recording complete! Have some sleep!")
    

