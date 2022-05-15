#!/bin/python3

import sys
import os
import atheris
# old_stdout = sys.stdout # backup current stdout
# sys.stdout = open(os.devnull, "w")
with atheris.instrument_imports():
    from phonemizer.backend import EspeakBackend, FestivalBackend
# sys.stdout = old_stdout
# from phonemizer import phonemize
# from phonemizer.backend import EspeakBackend, FestivalBackend

# Initilize the backends separatly
# Running phonemizer repeatly increases the memory usage
espeak = EspeakBackend('en-us')
festival = FestivalBackend('en-us')

@atheris.instrument_func
def TestOneInput(data):
    barray = bytearray(data)
    # espeak.phonemize(str(data).split(" "))
    if len(barray) > 0:
        # Choose the backend to use based on the first input byte
        r = barray[0]
        if r % 2 == 0:
            # Make sure to remove the first byte otherwise this will only every test this backend with the first byte being even
            del barray[0]
            espeak.phonemize(str(data).split(' '))
        else:
            del barray[0]
            festival.phonemize(str(data).split(' '))
    else:
        espeak.phonemize(str(data).split(' '))
        festival.phonemize(str(data).split(' '))

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()