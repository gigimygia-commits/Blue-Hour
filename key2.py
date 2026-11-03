# New TunePad cell
from tunepad.constants import *

# BLUE HOUR - MELODY
# this cell creates the main emotional melody of the song

# I use Crystal Organ because it has a soft and dreamy sound
# this fits the calm and slightly melancholic feeling of Blue Hour

# repeat the melody 8 times
for i in range(8):

    # playNote() plays one note at a time
    # beats controls how long each note lasts
    # I use different beat lengths so the melody sounds less robotic

    playNote(G4, beats=1, velocity=40)

    # shorter note adds movement
    playNote(Bb4, beats=0.5, velocity=38)

    # longer note creates a more emotional feeling
    playNote(C5, beats=1.5, velocity=44)

    # rest() creates silence
    # I use space because slow R&B melodies should not feel too crowded
    rest(0.5)

    playNote(Bb4, beats=0.5, velocity=38)
    playNote(G4, beats=1, velocity=40)
    playNote(Eb4, beats=1, velocity=36)

    # another pause makes the melody feel relaxed
    rest(0.5)

    # small response phrase
    playNote(F4, beats=0.5, velocity=38)
    playNote(G4, beats=0.5, velocity=42)
    playNote(Bb4, beats=1, velocity=40)

    rest(1)

    # longer ending note finishes the phrase
    playNote(G4, beats=2, velocity=42)

    # space before the melody repeats
    rest(1)


