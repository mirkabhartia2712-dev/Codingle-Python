import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import pyttsx3
import json
import datetime


model = Model("Model")
recognizer = KaldiRecognizer(model, 16000)
audio_queue = queue.Queue()
tts_engine = pyttsx3.init()


def callback(indata, frames, time, status):
    if status:
        print(status)
    audio_queue.put(bytes(indata))


def process_query(query):
        query = query.lower()
        if "time" in query:
            now = datetime.datetime.now().strftime("%H:%M")
            response = f"The current time is {now}."
        elif "date" in query:
            today = datetime.datetime.now().strftime("%B %d, %Y")
            response = f"Today's sate is {today}."
        else:
            response = "I'm sorry, I didnt understand that."
        return response
    

with sd.RawInputStream(
    samplerate=16000,
    blocksize=8000,
    dtype='int16',
    channels=1,
    callback=callback
):
    print("🤠🎤🎙️🪅Listening... Press Ctrl+C to stop")

    while True:
        data= audio_queue.get()

        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            text = result.get("text", "")

            if text:
                print("You said:", text)
                response = process_query(text)
                print("Assistant:", response)

                tts_engine.say(response)
                tts_engine.runAndWait()
                 




