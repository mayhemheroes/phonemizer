#!/bin/python3

import sys
import os
import atheris

from phonemizer.backend import EspeakBackend, FestivalBackend

# Initilize the backends separatly
# Running phonemizer repeatly increases the memory usage
espeak = EspeakBackend('en-us')
festival = FestivalBackend('en-us')

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    if len(data) < 1:
        return

    option = fdp.ConsumeBytes(1)[0]
    in_string = fdp.ConsumeUnicodeNoSurrogates(len(data))

    if option % 2 == 0:
        espeak.phonemize(in_string.split(" "))
    else:
        festival.phonemize(in_string.split(" "))

atheris.instrument_all()
atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()