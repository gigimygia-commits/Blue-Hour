from tunepad.constants import *

# BLUE HOUR - BASS
# this cell creates the low part of the song
# bass supports the chords and makes the R&B groove feel deeper


# INTRO
# rest() means silence
# I leave the first 16 beats empty so the piano starts by itself
# this makes the beginning feel more atmospheric

rest(16)


# these notes match the main roots of my chords

intro_bass = [C2, Ab1, F1, G1]


for note in intro_bass:

    # beats=2 makes the bass note longer
    # velocity=42 keeps the intro bass soft

    playNote(note, beats=2, velocity=42)

    # I use rest() to leave space between bass notes
    # space helps the bass feel relaxed instead of too busy

    rest(2)


# VERSE
for i in range(4):

    # main C bass note

    playNote(C2, beats=1.5, velocity=58)

    rest(1)

    # G is a passing note
    # I added passing notes so the bass has some movement
    # instead of only playing one note for each chord

    playNote(G2, beats=0.5, velocity=44)

    rest(1)


    # Ab bass

    playNote(Ab1, beats=1.5, velocity=56)

    rest(1)

    playNote(Eb2, beats=0.5, velocity=43)

    rest(1)


    # F bass

    playNote(F1, beats=1.5, velocity=58)

    rest(1)

    playNote(C2, beats=0.5, velocity=44)

    rest(1)


    # G bass

    playNote(G1, beats=1.5, velocity=60)

    # B leads back toward C
    # this makes the loop connect more smoothly

    playNote(B1, beats=0.5, velocity=42)

    rest(2)


# CHORUS
for i in range(4):

    # the chorus bass is stronger
    # this helps the chorus feel bigger than the verse

    playNote(Ab1, beats=2, velocity=62)
    playNote(Eb2, beats=1, velocity=46)
    rest(1)

    playNote(Bb1, beats=2, velocity=60)
    playNote(F2, beats=1, velocity=46)
    rest(1)

    playNote(C2, beats=2, velocity=64)
    playNote(G2, beats=1, velocity=48)
    rest(1)

    playNote(G1, beats=2, velocity=62)
    playNote(B1, beats=0.5, velocity=44)
    rest(1.5)


# OUTRO
# the bass becomes simple again
# this helps the song calm down at the end

for note in [C2, Ab1, F1, G1]:

    playNote(note, beats=2, velocity=38)

    rest(2)


# final space with no bass

rest(16)
