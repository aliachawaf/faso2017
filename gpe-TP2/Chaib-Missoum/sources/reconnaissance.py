import snowboydecoder
import sys
import signal
from  music import *
import random

interrupted = False

playlist = ["un.wav", "deux.wav", "trois.wav", "quatre.wav"]
indice = 0
init()

# Initialisation des variables

indice = random.randrange(4)
load(playlist[indice])

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def interrupt_callback():
    global interrupted
    return interrupted

if len(sys.argv) != 3:
    print("Error: need to specify 2 model names")
    print("Usage: python demo.py 1st.model 2nd.model")
    sys.exit(-1)

models = sys.argv[1:]

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)
init()
sensitivity = [0.6]*len(models)
detector = snowboydecoder.HotwordDetector(models, sensitivity=sensitivity)
callbacks = [lambda: snowboydecoder.play(1),
             lambda: snowboydecoder.pause()]
print('Donnez moi vos ordres maître ')

detector.start(detected_callback=callbacks,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()
