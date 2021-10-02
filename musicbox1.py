#import winsound
#winsound.Beep(frequency, duration)

"""sound."""
from __future__ import division
import math

from pyaudio import PyAudio # sudo apt-get install python{,3}-pyaudio

try:
    from itertools import izip
except ImportError: # Python 3
    izip = zip
    xrange = range

def sine_tone(frequency, duration, volume=1, sample_rate=22050):
    n_samples = int(sample_rate * duration)
    restframes = n_samples % sample_rate

    p = PyAudio()
    stream = p.open(format=p.get_format_from_width(1), # 8bit
                    channels=1, # mono
                    rate=sample_rate,
                    output=True)
    s = lambda t: volume * math.sin(2 * math.pi * frequency * t / sample_rate)
    samples = (int(s(t) * 0x7f + 0x80) for t in range(n_samples))
    stream.write(bytes(bytearray(samples)))

    # fill remainder of frameset with silence
    stream.write(b'\x80' * restframes)

    stream.stop_stream()
    stream.close()
    p.terminate()


def A(argument):
    sine_tone(
        # see http://www.phy.mtu.edu/~suits/notefreqs.html
        frequency=440.00,  # Hz, waves per second A4
        duration=1,  # seconds to play sound
        volume=.001,  # 0..1 how loud it is
        # see http://en.wikipedia.org/wiki/Bit_rate#Audio
        sample_rate=22050  # number of samples per second
    )
    return selection(argument)

def B(argument):
    sine_tone(
        # see http://www.phy.mtu.edu/~suits/notefreqs.html
        frequency=440.00,  # Hz, waves per second A4
        duration=1,  # seconds to play sound
        volume=.001,  # 0..1 how loud it is
        # see http://en.wikipedia.org/wiki/Bit_rate#Audio
        sample_rate=22050  # number of samples per second
    )
    return selection(argument)

def selection(argument):
    if argument=='A':
        q=1
    elif argument=='B':
        q=2
    elif argument=='C':
        q=3
    elif argument=='D':
        q=4
    elif argument=='E':
        q=5
    elif argument=='F':
        q=6
    elif argument=='G':
        q=7
    else:
        q=8
    return q;

def actions(q,argument):
    switch ={
        1: A,
        2: B,
        3: C,
        4: D,
        5: E,
        6: F,
        7: G,
        8: S,
    }
    func=switch.get(q,lambda:"invalid state")
    return func(argument)

# entrada de los sensores
nota=['G','G','A','A','B','B']
#tiempo=[1,1,1,1,1,1]


q=7 #  estado inicial
for x in nota:
    q=actions(q,x) # actalizacion del estado

