from tunepad.constants import *

# BLUE HOUR CHORDS
# this cell creates the harmony of my song
# harmony is the chords underneath the melody

# I use TunePad constants so I can write note names like C4 and Eb4
# this is easier for me to understand than only using numbers


# INTRO CHORDS
# I use 7th and 9th chords because they sound richer and smoother
# this fits the dreamy R&B feeling of Blue Hour

intro_chords = [
    [C4, Eb4, G4, Bb4, D5],   # Cm9
    [Ab3, C4, Eb4, G4],       # Abmaj7
    [F3, Ab3, C4, Eb4, G4],   # Fm9
    [G3, B3, D4, F4]          # G7
]


# VERSE CHORDS
# these are slightly simpler than the intro chords

verse_chords = [
    [C4, Eb4, G4, Bb4],       # Cm7
    [Ab3, C4, Eb4, G4],       # Abmaj7
    [F3, Ab3, C4, Eb4],       # Fm7
    [G3, B3, D4, F4]          # G7
]


# CHORUS CHORDS
# I change the progression in the chorus
# this stops the whole song from sounding like one repeated loop

chorus_chords = [
    [Ab3, C4, Eb4, G4],
    [Bb3, D4, F4, A4],
    [C4, Eb4, G4, Bb4, D5],
    [G3, B3, D4, F4]
]


# INTRO
# range(2) means repeat the whole intro progression 2 times
# a loop is better than copying and pasting the same chords again

for i in range(2):

    # this loop goes through each chord in the list
    for chord in intro_chords:

        # playNote() plays the notes
        # because "chord" contains several notes, they play together
        # beats=4 means the chord lasts for 4 beats
        # velocity controls how strong the sound is
        # sustain lets the chord ring a little longer
        # I use low velocity because the intro should feel soft and dreamy

        playNote(chord, beats=4, velocity=38, sustain=1)


# VERSE
for i in range(4):

    for chord in verse_chords:

        # slightly stronger than the intro
        # this slowly builds the song

        playNote(chord, beats=4, velocity=44, sustain=1)


# CHORUS
for i in range(4):

    for chord in chorus_chords:

        # higher velocity makes the chorus feel fuller
        # but I still keep it smooth because it is R&B

        playNote(chord, beats=4, velocity=50, sustain=1)


# OUTRO
# I return to the intro chords
# this helps the song finish with the same Blue Hour mood

for i in range(2):

    for chord in intro_chords:

        # softer again for the ending

        playNote(chord, beats=4, velocity=34, sustain=1)
