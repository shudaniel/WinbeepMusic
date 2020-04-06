import winsound
from time import sleep

def quarter():
    return 1000

def half():
    return quarter() * 2

def whole():
    return quarter() * 4

def eigth():
    return quarter() // 2

def sixteenth():
    return quarter() // 4

def dotted(duration):
    # Dotted music notes
    return int(1.5 * duration)

def rest(duration):
    sleep(duration / 1000.0)


def lowE(duration):
    winsound.Beep(165, duration)

def lowF(duration):
    winsound.Beep(175, duration)

def lowFsharp(duration):
    winsound.Beep(185, duration)

def lowG(duration):
    winsound.Beep(196, duration)

def lowA(duration):
    winsound.Beep(220, duration)  

def lowAsharp(duration):
    winsound.Beep(233, duration)  # Low A#

def lowBflat(duration):
    lowAsharp(duration)

def lowB(duration):
    winsound.Beep(247, duration)  

def C(duration):
    winsound.Beep(262, duration)

def D(duration):
    winsound.Beep(294, duration)  # D

def E(duration):
    winsound.Beep(329, duration)  

def F(duration): 
    winsound.Beep(349, duration)

def G(duration):
    winsound.Beep(392, duration)  # G

def Gsharp(duration):
    winsound.Beep(415, duration)

def Aflat(duration):
    Gsharp(duration)

def A(duration):
    winsound.Beep(440, duration)  

def B(duration):
    winsound.Beep(494, duration)

def highD(duration):
    winsound.Beep(587, duration)  # High D